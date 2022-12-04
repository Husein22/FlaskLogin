from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField
from wtforms.validators import Length,DataRequired,Email,ValidationError

class LoginForm(FlaskForm):
    email=StringField(label="email",validators=[Length(min=2,max=30),DataRequired()])
    pasword=PasswordField(label="pasword",validators=[Length(min=2,max=30),DataRequired()])
    submit=SubmitField(label="Log In")
