from flask import flash
from flask_wtf import FlaskForm
from wtforms import SubmitField, IntegerField, HiddenField
from wtforms.validators import DataRequired, EqualTo, NumberRange, InputRequired


class GetArgs(FlaskForm):
    lower_cnt = IntegerField('Number of Lowercase letters', default=9, validators=[NumberRange(min=0,message='Please enter a value >= 0')])
    upper_cnt = IntegerField('Number of Uppercase letters',default=4,validators=[NumberRange(min=0,message='Please enter a value >= 0')])
    digit_cnt = IntegerField('Number of Digits', default=2, validators=[NumberRange(min=0,message='Please enter a value >= 0')])
    symbol_cnt = IntegerField('Number of Symbols', default=1, validators=[NumberRange(min=0,message='Please enter a value >= 0')])
    pass_cnt = IntegerField('Number of Passwords to Generate', default=5, validators=[DataRequired("Please enter a value > 0"), NumberRange(min=1)])
    hpwords = HiddenField('Stored Passwords')

    def validate(self):

#        result = super(GetArgs, self).validate()
        if not super(GetArgs, self).validate():
            return False
        return True

    submit = SubmitField('Generate')
