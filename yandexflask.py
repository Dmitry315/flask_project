from flask import Flask, render_template, request, redirect, session
from forms import *
from models import *

app = Flask(__name__)
app.config['SECRET_KEY'] = '1515dd15dd3d5d1a51b5af515ca'
db = DB()
user_model = UserModel(db.get_connection())
user_model.init_table()
nm = NewsModel(db.get_connection())
nm.init_table()
user_model.insert('admin', 'admin')

@app.route('/')
@app.route('/index')
def index():
    try:
        if not session['username']:
            return redirect('/login')
        news = nm.get_all(session['user_id'])
        news = sorted(news, key=lambda item: item[1])
        news = sorted(news, key=lambda item: item[0])
        return render_template('index.html', username=session['username'], news=news)
    except KeyError as err:
        return redirect('/login')


@app.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    form = LoginForm()
    if form.validate_on_submit():
        login = request.form['login']
        password = request.form['password']
        user = user_model.exists(login)
        if not user[0]:
            session['username'] = login
            session['user_id'] = user[1][0]
            user_model.insert(login, password)
            return redirect("/index")
    return render_template('login.html', title='Регистрация', form=form)

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    try:
        if session['username'] == 'admin':
            return render_template('admin.html', users=user_model.get_all(), news=nm)
    except KeyError as err:
        pass
    return redirect('/admin/login')

@app.route('/sign_in', methods=['GET', 'POST'])
def sign_in():
    form = LoginForm()
    if form.validate_on_submit():
        login = request.form['login']
        password = request.form['password']
        user = user_model.exists(login)
        if not user[0]:
            session['username'] = login
            session['user_id'] = user[1][0]
            user_model.insert(login, password)
            return redirect("/index")
    return render_template('login.html', title='Регистрация', form=form)

@app.route('/logout')
def logout():
    session['username'] = []
    return redirect('/login')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        login = request.form['login']
        password = request.form['password']
        user = user_model.exists(login)
        if user[0]:
            session['username'] = login
            session['user_id'] = user[1][0]
            return redirect("/index")
    return render_template('login.html',title='Авторизация' , form=form)

@app.route('/add_news', methods=['GET', 'POST'])
def add_news():
    if 'username' not in session:
        return redirect('/login')
    form = AddNewsForm()
    if form.validate_on_submit():
        title = form.title.data
        content = form.content.data
        nm.insert(title,content,session['user_id'])
        return redirect("/index")
    return render_template('add_news.html', title='Добавление новости',
                           form=form, username=session['username'])

@app.route('/delete_news/<int:news_id>', methods=['GET'])
def delete_news(news_id):
    if 'username' not in session:
        return redirect('/login')
    nm.delete(news_id)
    return redirect("/index")


if __name__ == '__main__':
    app.run(port=8000, host='127.0.0.1')
