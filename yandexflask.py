from flask import Flask, render_template, request, redirect, session
from forms import *
from models import *

app = Flask(__name__)
app.config['SECRET_KEY'] = '1515dd15dd3d5d1a51b5af515ca'
db = DB()
user_model = UserModel(db.get_connection())
user_model.init_table()
nm = UserModel(db.get_connection())
nm.init_table()


@app.route('/')
@app.route('/index')
def index():
    try:
        if not session['username']:
            return redirect('/login')
        news = NewsModel(db.get_connection()).get_all(session['user_id'])
        return render_template('index.html', username=session['username'], news=news)
    except KeyError as err:
        return redirect('/login')



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
    return render_template('login.html', title='Авторизация', form=form)

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
