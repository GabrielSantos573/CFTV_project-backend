from flask import render_template, Response
from backend import app
from backend.rostos import load_trained_model, gen_frames

@app.route("/login", methods=['GET', 'POST'])
def hello_world():
    return "Hello, World!!!!"

@app.route('/video_feed/<camera_id>')
def video_feed(camera_id):
    model, label_dict = load_trained_model()
    return Response(gen_frames(model, label_dict, int(camera_id)), mimetype='multipart/x-mixed-replace; boundary=frame')