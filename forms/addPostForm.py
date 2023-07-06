
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, validators, TextAreaField


class AddPostForm(FlaskForm):
    title = StringField(
        'Title: ', [validators.InputRequired(), validators.Length(min=1, max=35)])
    author = StringField(
        'Author: ', [validators.InputRequired(), validators.Length(min=1, max=35)])
    content = TextAreaField(
        'Content: ', [validators.InputRequired(), validators.Length(min=5, max=3000)])
    images = FileField('Image: ', validators=[
                       FileAllowed(['jpg', 'jpeg', 'png', 'gif'])])
