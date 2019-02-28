from forms import *
from models import *

db.create_all()

@app.route('/')
@app.route('/index')
def index():
    try:
        if not session['username']:
            return redirect('/login')
        return render_template('index.html', username=session['username'])
    except KeyError as err:
        return redirect('/login')

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.route('/news', methods=['GET'])
def get_news():
    news = NewsModel.query.all()
    return jsonify({'news': news})

@app.route('/news', methods=['POST'])
def add_news():
    if not request.json:
        return jsonify({'error': 'Empty request'})
    elif not all(key in request.json for key in ['title', 'content', 'user_id']):
        return jsonify({'error': 'Bad request'})
    news = NewsModel(title=request.json['title'], content=request.json['content'])
    user = UserModel.query.filter_by(id=request.json['user_id']).first()
    if not user:
        return jsonify({'error': 'User not found'})
    user.NewsModel.append(news)
    db.session.commit()
    return jsonify({'success': 'OK'})

@app.route('/news/<int:news_id>', methods=['DELETE'])
def delete_news(news_id):
    news = NewsModel.query.filter_by(id = news_id).first()
    if not news:
        return jsonify({'error': 'Not found'})
    db.session.delete(news)
    db.session.commit()
    return jsonify({'success': 'OK'})

@app.route('/news/<int:news_id>',  methods=['GET'])
def get_one_news(news_id):
    news = NewsModel.query.filter_by(id=news_id)
    if not news:
        return jsonify({'error': 'Not found'})
    return jsonify({'news': news})

@app.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    form = LoginForm()
    if form.validate_on_submit():
        login = request.form['login']
        password = request.form['password']
        if login == 'admin' and password == 'nimda':
            session['username'] = login
            return redirect("/admin")
    return render_template('login.html', title='Регистрация', form=form)

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    try:
        if session['username'] == 'admin':
            return render_template('admin.html')
    except KeyError as err:
        pass
    return redirect('/admin/login')

@app.route('/sign_in', methods=['GET', 'POST'])
def sign_in():
    form = SignInForm()
    if form.validate_on_submit():
        login = request.form['login']
        password = request.form['password']
        user = UserModel.query.filter_by(username=login).first()
        if not bool(user):
            new_user = UserModel(username=login, password=password)
            db.session.add(new_user)
            db.session.commit()
            return redirect("/")
    return render_template('login.html', title='Регистрация', form=form)

@app.route('/logout')
def logout():
    session['username'] = []
    session['user_id'] = []
    return redirect('/login')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        login = request.form['login']
        password = request.form['password']
        user = UserModel.query.filter_by(username=login).first()
        if bool(user) and user.passoword == password:
            session['username'] = login
            session['user_id'] = user.id
            return redirect("/index")
    return render_template('login.html',title='Авторизация' , form=form)



if __name__ == '__main__':
    app.run(port=8000, host='127.0.0.1')
