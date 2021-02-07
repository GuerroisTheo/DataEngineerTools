from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class SearchBar(Form):
	""" Créer la bar de recherche """
	typing = StringField('Looking for:', validators=[DataRequired()])
	search = SubmitField('Go')