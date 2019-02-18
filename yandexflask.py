from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/form_sample', methods=['POST', 'GET'])
def sample():
    if request.method == 'GET':
        return render_template('sample.html')
    elif request.method == 'POST':
        print(request.form['username'])
        print(request.form['password'])
        print(request.form['about'])
        print(request.form['select'])
        print(request.form['sex'])
        print(request.form['memorize'])
        return 'success'

if __name__ == '__main__':
    app.run(port=8000, host='127.0.0.1')
