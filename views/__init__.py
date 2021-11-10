from flask import render_template, request, redirect, url_for, session,flash
from app import app
from model import *





@app.route('/', methods=["GET"])
def home():
    if "username" in session:
        return render_template('index.html')
    else:
        sections=section_items.find_one({"Status":"created"})
        return render_template('login.html',sections=sections)

# Register new user
@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    elif request.method == "POST":
        registerUser()
        return redirect(url_for("login"))

#Check if email already exists in the registratiion page
@app.route('/checkusername', methods=["POST"])
def check():
    return checkusername()

# Everything Login (Routes to renderpage, check if username exist and also verifypassword through Jquery AJAX request)
@app.route('/login', methods=["GET"])
def login():
    if request.method == "GET":
        if "username" not in session:
            return render_template("login.html")
        else:
            return redirect(url_for("home"))


@app.route('/checkloginusername', methods=["POST"])
def checkUserlogin():
    return checkloginusername()

@app.route('/checkloginpassword', methods=["POST"])
def checkUserpassword():
    return checkloginpassword()

#The admin logout
@app.route('/logout', methods=["GET"])  # URL for logout
def logout():  # logout function
    session.pop('username', None)  # remove user session
    return redirect(url_for("home"))  # redirect to home page with message

#Forgot Password
@app.route('/forgot-password', methods=["GET"])
def forgotpassword():
    return render_template('forgot-password.html')

#404 Page
@app.route('/404', methods=["GET"])
def errorpage():
    return render_template("404.html")

# #Blank Page
# @app.route('/blank', methods=["GET"])
# def blank():
#     return render_template('blank.html')

# #Buttons Page
# @app.route('/buttons', methods=["GET"])
# def buttons():
#     return render_template("buttons.html")

# #Cards Page
# @app.route('/cards', methods=["GET"])
# def cards():
#     return render_template('cards.html')

#Charts Page
@app.route('/charts', methods=["GET"])
def charts():
    return render_template("charts.html")

#Tables Page
@app.route('/tables', methods=["GET"])
def tables():
    return render_template("tables.html")

#Tables Page
@app.route('/table_items', methods=["GET"])
def table_items():
    return render_template("table_items.html")


#Tables Page
@app.route('/table_users', methods=["GET"])
def table_users():
    return render_template("table_users.html")

#Tables Page
@app.route('/table_sections', methods=["GET"])
def table_sections():
    return render_template("table_sections.html")


@app.route('/add_section', methods=['GET','POST'])
def addsection():
   if request.method=='POST':
        add_section()
        flash('you successfully create a section')
   return redirect(url_for("home"))
