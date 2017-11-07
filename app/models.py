from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime, timezone

@login_manager.user_loader
def load_user(user_id):
    '''
    @login_manager.user_loader Passes in a user_id to this function
    Function queries the database and gets a user's id as a response
    '''
    return User.query.get(int(user_id))

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

    # relationship between user and comment class
    comments = db.relationship('Comment', backref='user', lazy='dynamic')

    # subscribe column for user to subcribe to new post updates
    subscribe = db.Column(db.Boolean, default=False)

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

    @classmethod
    def subcribe_user(cls,user_id):
        '''
        Function that queries the database and set subscribe to True for a user with the specified id

        Args:
            user_id : specific user id
        '''
        user = User.query.filter_by(id=user_id).update({
            'subscribe':True
            })
        db.session.commit()

    @classmethod
    def get_subscribers(cls):
        '''
        Function that queries the Users Table in the database and returns only users who have subscribe set to True

        Returns:
            users emails: list of email addresses for users who have subscribe set to True
        '''
        users = User.query.filter_by(subscribe=True).all()
        users_emails = []
        for user in users:
            users_emails.append(user.email)
        return users_emails



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
    post_date = db.Column(db.DateTime, default=datetime.now())

    # user_id column for linking a post with a user
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    # relationship between post and comment class
    comments = db.relationship('Comment', backref='post', lazy='dynamic', cascade="all, delete-orphan")

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

    @classmethod
    def delete_post(cls,post_id):
        '''
        Function that deletes a specific post from the posts table and database and also delete its comments

        Args:
            post_id : specific post id
        '''
        comments = Comment.query.filter_by(post_id=post_id).delete()
        post = Post.query.filter_by(id=post_id).delete()
        db.session.commit()

class Comment(db.Model):
    '''
    Comment class to define the feedback from users
    '''

    # Name of the table
    __tablename__ = 'comments'

    # id column that is the primary key
    id = db.Column(db.Integer, primary_key = True)

    # comment_content for the feedback a user gives to a post
    comment_content = db.Column(db.String)

    # post_id column for linking a comment to a specific post
    post_id = db.Column(db.Integer, db.ForeignKey("posts.id",ondelete='CASCADE') )

    # user_id column for linking a comment to a specific user
    user_id = db.Column(db.Integer, db.ForeignKey("users.id") )

    def save_comment(self):
        '''
        Function that saves a new comment given as feedback to a post
        '''
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(cls,post_id):
        '''
        Function that queries the Comments Table in the database and returns only information with the specified post id

        Args:
            post_id : specific post_id

        Returns:
            comments : all the information for comments with the specific post id 
        '''
        comments = Comment.query.filter_by(post_id=post_id).all()

        return comments 

    @classmethod
    def delete_single_comment(cls,comment_id):
        '''
        Function that deletes a specific single comment from the comments table and database

        Args:
            comment_id : specific comment id
        '''
        comment = Comment.query.filter_by(id=comment_id).delete()
        db.session.commit()















