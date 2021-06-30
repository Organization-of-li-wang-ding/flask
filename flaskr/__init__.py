import os

from flask import Flask


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return '<!doctype html>\
                <html lang="en">\
                    <head>\
                        <meta name="viewport" content="width=device-width, initial-scale=1">\
                        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css" integrity="sha384-HSMxcRTRxnN+Bdg0JdbxYKrThecOKuH5zCYotlSAcp1+c8xmyTe9GYg1l9a69psu" crossorigin="anonymous">\
                        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap-theme.min.css" integrity="sha384-6pzBo3FDv/PJ8r2KRkGHifhEocL+1X2rVCTTkUfGk7/0pbek5mMa1upzvWbrUbOZ" crossorigin="anonymous">\
                        <script src="https://stackpath.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js" integrity="sha384-aJ21OjlMXNL5UyIl/XNwTMqvzeRMZH2w8c5cRVpzpU8Y5bApTppSuUkhZXN0VxHd" crossorigin="anonymous"></script>\
                        <title>hello,world!</title>\
                    </head>\
                    <body style="background:grey">\
                        <h1>hello,world!</h1>\
                        <div class="row">\
                            <div class="col-md-1">第一行</div>\
                        </div>\
                        <div class="row">\
                            <div class="col-md-8">第二行</div>\
                            <div class="col-md-4">第二行</div>\
                        </div>\
                        <div class="row">\
                            <div class="col-md-4">第三行</div>\
                            <div class="col-md-4">第三行</div>\
                            <div class="col-md-4">第三行</div>\
                        </div>\
                        <div class="row">\
                            <div class="col-md-6">第四行</div>\
                            <div class="col-md-6">第四行</div>\
                            <div class="col-md-6">第四行</div>\
                            <div class="col-md-6">第四行</div>\
                        </div>\
                    </body>\
                </html>'

    from . import db
    db.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)

    from . import blog
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')

    return app
