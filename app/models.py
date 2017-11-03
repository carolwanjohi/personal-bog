from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

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

    # relationship between post and user class
    posts = db.relationship('Post', backref='user', lazy='dynamic')

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

    # Name of the table
    __tablename__ = 'roles'

    # id column that is the primary key
    id = db.Column(db.Integer, primary_key = True)

    # name column for the name of the roles
    name = db.Column(db.String)

    # virtual column to connect with foriegn key
    users = db.relationship('User', backref='role', lazy='dynamic')

    def __repr__(self):
        return f'User {self.name}'

class Post(db.Model):
    '''
    Post class to define a blog post by a user with Writer role
    '''

    # Name of the table
    __tablename__ = 'posts'

    # id column that is the primary key
    id = db.Column(db.Integer, primary_key = True)

    # post_title column for the post's title
    post_title = db.Column(db.String)

    # post_content column for the post's content
    post_content = db.Column(db.String)

    # post_date column for the post's posting date 
    post_date = db.Column(db.Time, default=datetime.utcnow())

    # user_id column for linking a post with a user
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    def save_post(self):
        '''
        Function that saves a new blog post to the posts table and database
        '''
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_posts(cls):
        '''
        Function that queries the Posts Table in the database and returns all the information from the Posts Table

        Returns:
            posts : all the information in the posts table
        '''
        posts = Post.query.order_by(Post.id.desc()).all()
        return posts

    def delete_post(self):
        '''
        Function that deletes a specific post from the posts table and database
        '''
        db.session.delete(self)
        db.session.commit()














