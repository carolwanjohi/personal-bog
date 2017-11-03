from flask import render_template,redirect,url_for,request,flash
from . import auth
from ..models import User, Role
from .forms import RegistrationForm,LoginForm
from .. import db
from flask_login import login_user,logout_user,login_required


@auth.route('/login', methods=["GET", "POST"])
def login():
    login_form = LoginForm()

    if login_form.validate_on_submit():

        user = User.query.filter_by( email=login_form.email.data).first()

        if user is not None and user.verify_password(login_form.password.data):

            login_user(user, login_form.remember.data)

            return redirect(request.args.get('next') or url_for('main.index'))

        flash('Invalid username or password')

    title="Login"

    return render_template('auth/login.html', login_form=login_form, title=title)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))


@auth.route('/register', methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    role = Role.query.filter_by(id = 2).first()

    if form.validate_on_submit():
        user = User( email=form.email.data, username=form.username.data, password=form.password.data, role=role)

        db.session.add(user)

        db.session.commit()

        return redirect(url_for('auth.login'))

    title="New Account"

    return render_template('auth/register.html', registration_form=form, title=title)




