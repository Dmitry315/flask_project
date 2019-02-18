from flask import Flask, render_template, request
from os import getcwd

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

@app.route('/file_sample', methods=['POST', 'GET'])
def file_sample():
    if request.method == 'GET':
        return render_template('file.html')
    elif request.method == 'POST':
        f = request.files['file']
        with open('file.txt', mode='w') as new:
            for i in f.readlines():
                new.write(str(i))
        return 'success'

@app.route('/odd_even', methods=['POST', 'GET'])
def odd_even():
    if request.method == 'GET':
        return render_template('odd_even.html')
    elif request.method == 'POST':
        num = request.form['number']
        try:
            new_num = int(num)
            return num + ' - ' + ('нечётное' if new_num % 2 else 'чётное')
        except:
            return num + ' не является корректным целым числом'


if __name__ == '__main__':
    app.run(port=8000, host='127.0.0.1')
