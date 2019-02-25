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

@app.route('/send')
def send():
    try:
        if session['username']:
            form = SolutionForm
            if form.validate_on_submit():
                task = request.form['task']
                code = request.form['code']
                solution = SolutionAttempt(task=task, code=code, status='check', student_id=)
    except Exception as err:
        pass
    return redirect('/')

@app.route('/status/<int:id>/<stat>')
def status(id, stat):
    try:
        if session['username'] == 'admin':
            solution = SolutionAttempt.query.filter_by(id=id).first()
            solution.status = stat
            db.session.commit()
    except Exception as err:
        return redirect('/')


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
            return render_template('admin.html', solutions=SolutionAttempt.query.filter_by(status='check'))
    except KeyError as err:
        pass
    return redirect('/admin/login')

@app.route('/sign_in', methods=['GET', 'POST'])
def sign_in():
    form = SignInForm()
    if form.validate_on_submit():
        login = request.form['login']
        name = request.form['login']
        surname = request.form['login']
        email = request.form['login']
        group = request.form['login']
        year = request.form['login']
        user = YandexLyceumStudent.query.filter_by(username=login).first()
        if not bool(user):
            new_user = YandexLyceumStudent(username=login, year=year, name=name, email=email,
                                           group=group, surname=surname)
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
        user = YandexLyceumStudent.query.filter_by(username=login).first()
        if bool(user):
            session['username'] = login
            session['user_id'] = user.id
            return redirect("/index")
    return render_template('login.html',title='Авторизация' , form=form)



if __name__ == '__main__':
    app.run(port=8000, host='127.0.0.1')
