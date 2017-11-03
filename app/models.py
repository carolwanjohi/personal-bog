from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager

@login_manager.user_loader
def load_user(user_id):
    '''
    @login_manager.user_loader Passes in a user_id to this function
    Function queries the database and gets a user's id as a response
    '''
    return User.query.get(int(user_id))

class User(UserMixin,db.Model):
    '''
    User class to define a user in the database
    '''

    # Name of the table
    __tablename__ = 'users'

    # id column that is the primary key
    id = db.Column(db.Integer, primary_key = True)

    # username column for usernames
    username = db.Column(db.String(255))

    # email column for a user's email address
    email = db.Column(db.String(255), unique=True, index=True)

    # password_hash column for passwords
    password_hash = db.Column(db.String(255))

    # role_id column for a User's role
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self,password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)


    def __repr__(self):
        return f'User {self.username}'

    @classmethod
    def check_role(cls,user_id,role_id):
        get_role = User.query.filter_by(id=user_id).filter_by(role_id=role_id).first()
        return get_role

    def save_user(self):
        '''
        Save instance of Review model to the session and commit it to the database
        '''
        db.session.add(self)
        db.session.commit()

class Role(db.Model):
    '''
    Role class to define a User's role in the database
    '''

    # Name od the table
    __tablename__ = 'roles'

    # id column that is the primary key
    id = db.Column(db.Integer, primary_key = True)

    # name column for the name of the roles
    name = db.Column(db.String)

    # virtual column to connect with foriegn key
    users = db.relationship('User', backref='role', lazy='dynamic')

    def __repr__(self):
        return f'User {self.name}'



