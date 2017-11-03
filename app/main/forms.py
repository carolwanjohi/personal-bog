from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required

class CommentForm(FlaskForm):
    '''
    Class to create a wtf form for creating a feedback on a pitch
    '''
    comment_content =  TextAreaField('Comment', validators=[Required()])
    submit = SubmitField('Submit')

