from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required

class CommentForm(FlaskForm):
    '''
    Class to create a wtf form for creating a feedback on a post
    '''
    comment_content =  TextAreaField('Comment', validators=[Required()])
    submit = SubmitField('Submit')

class PostForm(FlaskForm):
    '''
    Class to create a wtf form for creating a post
    '''
    post_title = StringField('Post Title')
    post_content = TextAreaField('Post Content')
    submit = SubmitField('Submit')

