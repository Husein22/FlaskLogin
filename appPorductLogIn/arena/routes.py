from arena import app
from flask import render_template,flash,redirect,url_for
from arena.forms import LoginForm
from arena.userColumn import User,Pacijent
from flask_login import login_user,logout_user,login_required,current_user

@app.route("/login",methods=["GET","POST"])
def login_page():
    forma=LoginForm()
    if forma.validate_on_submit():
        print("dosao sam")
        pokusajUsera=User.query.filter_by(email=forma.email.data).first()
        if pokusajUsera and pokusajUsera.provjeraPasworda(
            pokuajPaswoda=forma.pasword.data):
            return redirect( url_for('home_page') )
        else:
            flash('Pogresan email ili sifra',category='danger')


    return render_template("login.html",forma=forma)

@app.route('/home')
def home_page():
    pacijent = Pacijent.query.all()

    return render_template("home.html",pacijent=pacijent)

@app.errorhandler(502)
def internal_error(error):
    return flash("Nema internet konekcije")

@app.errorhandler(404)
def not_found(error):
    return "404 error,provjerite rutu do lokacije"

@app.errorhandler(500)
def not_found(error):
    return flash("Internal server error")

@app.route("/logout")
def logout_page():
    logout_user()
    return redirect (url_for("login_page"))
    
    
    
  