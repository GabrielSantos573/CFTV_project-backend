import os
import cv2
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Input
from tensorflow.keras.utils import to_categorical

def preprocess_image(img):
    img = cv2.resize(img, (128, 128))
    img = np.expand_dims(img, axis=0)
    return img

def load_trained_model():
    model = tf.keras.models.load_model('face_recognition_model.keras')
    label_dict = np.load('label_dict.npy', allow_pickle=True).item()
    return model, label_dict

def gen_frames(model, label_dict, camera_index=0):
    cap = cv2.VideoCapture(camera_index)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            face = frame[y:y+h, x:x+w]
            img = preprocess_image(face)
            prediction = model.predict(img)
            predicted_label = np.argmax(prediction)
            confidence = prediction[0][predicted_label]
            name = label_dict[predicted_label] if confidence > 0.3 else 'Unknown'
            cv2.putText(frame, name, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
        
        