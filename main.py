from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return "Миссия Колонизация Марса"


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def promotion():
    return "Человечество вырастает из детства.</br>Человечеству мала одна планета.</br>Мы сделаем обитаемыми безжизненные пока планеты.</br>И начнем с Марса!</br>Присоединяйся!"


@app.route('/image_mars')
def image_mars():
    return f"""
                <!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="/static/img/mars.png" alt="здесь должна была быть картинка, но не нашлась">
                    <div>Вот она какая, красная планета.</div>
                  </body>
                </html>
"""


@app.route('/promotion_image')
def promotion_image():
    return f"""
                <!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Колонизация</title>
                    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
                    <link rel="stylesheet" type="text/css" href="static/css/style.css"/>
                  </head>
                  <body>
                    <h1 class="header">Жди нас, Марс!</h1>
                    <img src="/static/img/mars.png" alt="здесь должна была быть картинка, но не нашлась">
                    <div class="alert alert-secondary">Человечество вырастает из детства.</div>
                    <div class="alert alert-success">Человечеству мала одна планета.</div>
                    <div class="alert alert-secondary">Мы сделаем обитаемыми безжизненные пока планеты.</div>
                    <div class="alert alert-warning">И начнем с Марса!</div>
                    <div class="alert alert-danger">Присоединяйся!</div>
                  </body>
                </html>
"""


@app.route('/choice/<planet>')
def choice(planet):
    return f"""
                <!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Колонизация</title>
                    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
                    <link rel="stylesheet" type="text/css" href="static/css/style.css"/>
                  </head>
                  <body>
                    <h1 class="header">Моё предложение: {planet}</h1>
                    <div class="alert alert-secondary">Есть кислород</div>
                    <div class="alert alert-success">Нет инопланетян</div>
                    <div class="alert alert-secondary">Множество неизвестных ресурсов</div>
                    <div class="alert alert-warning">Находится в соседней галактике</div>
                  </body>
                </html>
"""


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def results(nickname, level, rating):
    return f"""
                <!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Результаты</title>
                    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
                    <link rel="stylesheet" type="text/css" href="static/css/style.css"/>
                  </head>
                  <body>
                    <h1 class="header">Результаты отбора</h1>
                    <div class="alert alert-secondary">Претендента на участие в миссии {nickname}:</div>
                    <div class="alert alert-success">Поздравляем! Ваш рейтинг после {level} этапа отбора составляет {rating}!</div>
                    <div class="alert alert-secondary">Желаем удачи!</div>
                  </body>
                </html>
"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')