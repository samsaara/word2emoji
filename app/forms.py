from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired

class SearchForm(Form):
    search_word = StringField('search_word', validators=[DataRequired()])
