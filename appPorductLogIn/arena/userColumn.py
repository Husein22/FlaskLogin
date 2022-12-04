from arena import db,bcrypt,login_manager
from flask_login import UserMixin
from werkzeug.security import check_password_hash

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model,UserMixin):
    id=db.Column(db.Integer(),primary_key=True)
    email = db.Column(db.String(length=50), nullable=False)
    pasword_hash=db.Column(db.String(length=60), nullable=False)

    def __repr__(self) -> str:
        return f'Item{self.email}'

   
    @property
    def pasword(self):
        return self.pasword
       
    @pasword.setter
    def pasword(self,plain_text):
        self.pasword_hash=bcrypt.generate_password_hash(plain_text).decode('utf-8')
    
    def provjeraPasworda(self,pokuajPaswoda):
        return bcrypt.check_password_hash(self.pasword_hash,pokuajPaswoda)
    
        
class Pacijent(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False)
    description = db.Column(db.String(length=1024), nullable=False)
    vrijemePocetkaPregleda = db.Column(db.String(), nullable=False)
    datum = db.Column(db.Integer(), nullable=False)
   
    
    def __repr__(self) -> str:
        return f'Item{self.name}'