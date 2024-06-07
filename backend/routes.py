from flask import render_template, Response, redirect, url_for, flash, request
from backend import app, db, bcrypt
from backend.models import Usuario 
from backend.forms import FormCriarConta, FormLogin
from flask_login import login_user
from backend.rostos import load_trained_model, gen_frames

@app.route("/login", methods=['GET', 'POST'])
def login():
    form_login = FormLogin()
    form_criarconta = FormCriarConta()
    if form_login.validate_on_submit() and 'botao_submit_login' in request.form:
        usuario = Usuario.query.filter_by(email=form_login.email.data).first()
        if usuario and bcrypt.check_password_hash(usuario.senha, form_login.senha.data):
            login_user(usuario, remember=form_login.lembrar_dados.data)
            flash(f'Login feito com sucesso no e-mail: {form_login.email.data}', 'alert-success')
            return redirect(url_for('home'))
        else:
            flash(f'FALHA NO LOGIN: {form_login.email.data}', 'alert-danger')
    if form_criarconta.validate_on_submit() and 'botao_submit_criarconta' in request.form:
        senha_crypt = bcrypt.generate_password_hash(form_criarconta.senha.data)
        usuario = Usuario(username=form_criarconta.username.data, email=form_criarconta.email.data, senha=senha_crypt)
        db.session.add(usuario)
        db.session.commit()
        flash(f'Conta criada para o e-mail: {form_criarconta.email.data}', 'alert-success')
        return redirect(url_for('home'))
    return render_template('login.html', form_login=form_login, form_criarconta=form_criarconta)

@app.route('/video_feed/<camera_id>')
def video_feed(camera_id):
    model, label_dict = load_trained_model()
    return Response(gen_frames(model, label_dict, int(camera_id)), mimetype='multipart/x-mixed-replace; boundary=frame')