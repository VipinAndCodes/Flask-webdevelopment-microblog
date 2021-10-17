from app import app
from flask import render_template,redirect,flash
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username':'vipin'}
    posts=[{"author":{"username":"john"},"body":"the book about the lions"},
        {"author":{"username":"red"},"body":"the book about the cars"},
        {"author":{"username":"sam"},"body":"the book about the rings"}

    ]
    return render_template('index.html',title="Home",user=user,posts=posts)


@app.route('/login',methods=['GET','POST'])
def login():
    form=LoginForm()
    if form_validate_on_submit():
        flash('Login for {} and remember me {}'.format(form.username.data,form.remember_me.data))
        return redirect('/index')
    return render_template('login.html',form=form)


