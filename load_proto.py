from flask import Flask, url_for, request

app = Flask(__name__)


@app.route('/load_photo', methods=['POST', 'GET'])
def astronaut_selection():
    if request.method == 'GET':
        return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <title>Отбор астронавтов</title>
                  </head>
                  <body>
                    <h1 align="center">Загрузка фотографии</h1>
                    <h3 align="center">для участия в миссии</h3>
                    <div>
                        <form class="login_form"  enctype="multipart/form-data" method="post">
                            <div class="form-group">
                                <label for="photo">Приложите фотографию</label>
                                <input type="file" class="form-control-file" id="photo" name="file">
                            </div>
                            <button type="submit" class="btn btn-primary">Отправить</button>
                        </form>
                    </div>
                  </body>
                </html>'''
    elif request.method == 'POST':
        f = request.files['file']
        with open('static/img/mars.jpg', 'wb') as file_1:
            file_1.write(f.read())
        return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <title>Отбор астронавтов</title>
                  </head>
                  <body>
                    <h1 align="center">Загрузка фотографии</h1>
                    <h3 align="center">для участия в миссии</h3>
                    <div>
                        <form class="login_form"  enctype="multipart/form-data" method="post">
                            <div class="form-group">
                                <label for="photo">Приложите фотографию</label>
                                <input type="file" class="form-control-file" id="photo" name="file">
                            </div>
                            <img src="{url_for('static', filename='img/mars.jpg')}">
                            <button type="submit" class="btn btn-primary">Отправить</button>
                        </form>
                    </div>
                  </body>
                </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')