from app import app
from flask import render_template,request
from app.model import User


@app.route('/')
def index():
    return render_template('index.html')
    pass

@app.route('/regist',methods=['GET','POST'])
def regist():
    if request.form:
        form = request.form
        user = User(email=form['email'],username=form['username'])
        err = user.save()
        if err:
            return err
        return render_template('index.html')
    return render_template('regist.html')
