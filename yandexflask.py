from flask import Flask, url_for

app = Flask(__name__)


@app.route('/index')
def index():
    return '<h1>Привет, Яндекс! Я - Дмитрий</h1>'


@app.route('/image_sample')
def image():
    return '''
    <!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width,
                    initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet"
                    href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"
                    integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm"
                    crossorigin="anonymous">
                    
                  </head>
                  <body>
                    <nav class='navbar'>
                        <button type='button', class='btn-danger'>Красная кнопка</button>
                        <button type='button', class='btn-info'>Инфомация</button>
                        
                    </nav>
                    <div data-ride="carousel" class='carousel slide' data-ride="carousel">
                        <div class="carousel-inner">
                            <div class="carousel-item active">
                            <img src="''' + url_for('static', filename='img/slide1.jpg') + '''">
                        </div>
                        <div class="carousel-item">
                            <img src="''' + url_for('static', filename='img/slide2.png') + '''">
                        </div>
                        <div class="carousel-item">
                            <img src="https://habrastorage.org/webt/8w/rq/7v/8wrq7vfhyqv2saamr2d5z2jha5o.png">
                        </div>
                        
                        
                    </div>
                    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
                    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
                    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>

                    <script>
                        $('.carousel').carousel({
                            interval: 2000
                        })
                    </script>
                  </body>
                </html>
    '''

@app.route('/text_in_alert/<alert>')
def alert(alert):
    return'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width,
                    initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet"
                    href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"
                    integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm"
                    crossorigin="anonymous">
                    
                  </head>
                  <body>
                    
                    <div class='alert alert-primary' role='alert'>
                        '''+alert+'''
                    </div>
                    
                    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
                    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
                    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>

                    <script>
                        
                    </script>
                  </body>
                </html>
    '''

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
