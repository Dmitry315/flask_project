from flask import Flask, url_for

app = Flask(__name__)

@app.route('/index')
def index():
    return 'Привет, Яндекс! Я - Дмитрий'

@app.route('/image_sample')
def image():
    return '''
    <h1>Картинка<h1>
    <img src="{}">
    '''.format(url_for('static', filename='img/my_img.jpg'))

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
