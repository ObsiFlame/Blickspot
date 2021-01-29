from flask import render_template,url_for, redirect, request, session, flash, g
from blickspot import app , db , bcrypt
import secrets
from blickspot.models import User
from blickspot.posthandler import h_post, getDate
from blickspot import login_manager
from flask_login import logout_user, current_user
from sqlalchemy.exc import IntegrityError

@app.before_request
def before_request():
    if 'user_username' and 'user_email' in session:
        g.ProfileUsername = session['user_username']
        g.ProfileEmail = session['user_email']


@app.route("/")
@app.route("/home")
def home():
    return render_template('Home.html')

# This is the route for the login page and for the users, users will have a dynamic login route
@app.route("/Login", methods = ["POST", "GET"])
def login():
    if "user_id" in session:
        return redirect('user')

    if request.method == 'POST':
        user1 = User.query.filter_by(email=request.form["InputEmail2"]).first()
        if user1 and bcrypt.check_password_hash(user1.password, request.form["InputPassword2"]):
            session['user_id'] =  secrets.token_hex(16)
            session['user_username'] = str(user1.username)
            session['user_email'] = str(user1.email)
            return redirect('user')
        else:
            flash('Login Unsuccessful, Please check the email and Password', 'warning')  

    return render_template('Sign-in.html')

@app.route("/signup", methods=['GET', 'POST'])
def signup():
    if "user_id" in session:
        return redirect('user')
    try:
        if request.method == 'POST':
            hashed_password = bcrypt.generate_password_hash(request.form["InputPassword"]).decode('utf-8')
            user = User(username= request.form["InputUsername"], email=request.form["InputEmail"], password=hashed_password)
            db.session.add(user)
            db.session.commit()
            flash('Your Account has been created!, you are now able to login', 'success')
            return redirect('Login')
    except IntegrityError:
        db.session.rollback()
        flash('The User Already exists!', 'success')
        return redirect('signup')

   
    return render_template('Sign-up.html')

@app.route('/logout')
def logout():
    session.pop("user_id", None)
    flash("You have been logged out", "warning")
    return redirect('home')

@app.route("/user")
def user():
    if 'user_id' in session:
        return render_template('user-Profile.html')
    else:
        return redirect(url_for('login'))

@app.route("/cyber-attacks")
def cyber_attack():
    return render_template('cyber-attack.html', data=h_post ,currentDate = getDate() )

@app.route("/report")
def report():
    return render_template('report.html')

@app.route("/support")
def support():
    return "Support-page"

@app.route("/about")
def about_us():
    return render_template('About-us.html')

# @app.context_processor
