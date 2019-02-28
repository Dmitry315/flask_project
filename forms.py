from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    login = StringField('Логин', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    submit = SubmitField('Войти')

class SignInForm(FlaskForm):
    login = StringField('Логин', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    submit = SubmitField('Зарегестрироваться')

class NewsForm(FlaskForm):
    title = StringField('Заголовок', validators=[DataRequired()])
    content = TextAreaField('Контент', validators=[DataRequired()])
    submit = SubmitField('Создать новость')