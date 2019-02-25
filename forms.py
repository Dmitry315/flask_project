from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    login = StringField('Логин', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    submit = SubmitField('Войти')

class SignInForm(FlaskForm):
    login = StringField('Логин', validators=[DataRequired()])
    name = StringField('Имя', validators=[DataRequired()])
    surname = StringField('Фамилия', validators=[DataRequired()])
    email = StringField('Почта', validators=[DataRequired()])
    group = IntegerField('Группа', validators=[DataRequired()])
    year = IntegerField('Год', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    re_password = PasswordField('Повторите пароль', validators=[DataRequired()])
    submit = SubmitField('Зарегестрироваться')

class SolutionForm(FlaskForm):
    task = StringField('Задача', validators=[DataRequired()])
    code = TextAreaField('Код', validators=[DataRequired()])
    submit = SubmitField('Отправить')