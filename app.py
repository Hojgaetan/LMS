from flask import Flask
from controllers.dashboard_controller import dashboard_blueprint
from controllers.book_controller import book_blueprint


def create_app():
    app = Flask(__name__)
    app.register_blueprint(dashboard_blueprint, url_prefix='/')
    app.register_blueprint(book_blueprint, url_prefix='/books')
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
