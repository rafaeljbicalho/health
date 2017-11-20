from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

class User(db.Model):
    id = db.Column('user_id',db.Integer , primary_key=True)
    username = db.Column('username', db.String(20), unique=True , index=True)
    password = db.Column('password' , db.String(250))
    cpf = db.Column('cpf',db.Integer , unique=True)
    sexo = db.Column('sexo' , db.String(250))
    data_nascimento = db.Column('data_nascimento' , db.String(250))
    peso = db.Column('peso' , db.String(250))
    altura = db.Column('altura' , db.String(250))
    registered_on = db.Column('registered_on' , db.DateTime)


    def __init__(self , username ,password, cpf, sexo, data_nascimento, peso, altura):
        self.username = username
        self.set_password(password)
        self.registered_on = datetime.utcnow()
        self.cpf = cpf
        self.sexo = sexo
        self.data_nascimento = data_nascimento
        self.peso = peso
        self.altura = altura

    def set_password(self , password):
        self.password = generate_password_hash(password)

    def check_password(self , password):
        return check_password_hash(self.password , password)

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)

    def __repr__(self):
        return "<User(username='%s', password='%s', cpf='%s', sexo='%s', data_nascimento='%s',\
    peso='%s',altura='%s',registered_on='%s')>" % (self.username,
        self.password, self.cpf,self.sexo,self.data_nascimento,self.peso,self.altura,self.registered_on)
