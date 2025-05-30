from flask import Flask
from controllers.book_controller import book_blueprint
from controllers.member_controller import member_blueprint
from controllers.dashboard_controller import dashboard_blueprint

def create_app():
    app = Flask(__name__)
    app.register_blueprint(book_blueprint, url_prefix='/books')
    app.register_blueprint(member_blueprint, url_prefix='/members')
    app.register_blueprint(dashboard_blueprint, url_prefix='/')
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
    