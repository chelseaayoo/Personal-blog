from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField,TextAreaField
from wtforms.validators import Required,Email,EqualTo


class UpdateProfileForm(FlaskForm):
    bio = TextAreaField('Give more information aboit you.',validators = [Required()])
    submit = SubmitField('Update bio')

class UploadBlogForm(FlaskForm):
    title = TextAreaField('Blog Title',validators=[Required()])
    blog =  TextAreaField('Your blog',validators=[Required()])
    submit = SubmitField('Post Blog')

class CommentsForm(FlaskForm):
    comment = TextAreaField('Type comment:',validators=[Required()])
    submit = SubmitField('Comment')
    
