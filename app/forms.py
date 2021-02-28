from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed

class UploadForm(FlaskForm):
    
    photo_test = FileField('Photo', validators=[
        FileRequired(),
        FileAllowed(['jpg', 'png'])
    ])
