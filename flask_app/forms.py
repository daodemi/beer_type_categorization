from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class beer_recipe_form(FlaskForm):
    abv = StringField('ABV', validators=[DataRequired()], default=int(0))
    ibu = StringField('IBU', validators=[DataRequired()], default=int(0))
    color = StringField('Color', validators=[DataRequired()], default=int(0))
    boil_size = StringField('Boil Size', validators=[DataRequired()], default=int(0))
    boil_time = StringField('Boil Time', validators=[DataRequired()], default=int(0))
    boil_gravity = StringField('Boil Gravity', validators=[DataRequired()], default=int(0))
    efficiency = StringField('Efficiency', validators=[DataRequired()], default=int(0))
    wort_change = StringField('Change In Wort', validators=[DataRequired()], default=int(0))
    submit = SubmitField('submit')




 


