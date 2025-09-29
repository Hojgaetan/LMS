from flask import Flask
from flask_cors import CORS
from controllers.dashboard_controller import dashboard_blueprint
from controllers.book_controller import book_blueprint
from controllers.member_controller import member_blueprint


def create_app():
    app = Flask(__name__)
    
    # Configuration CORS pour permettre les requêtes depuis React
    CORS(app, origins=["http://localhost:3000"])
    
    app.register_blueprint(dashboard_blueprint, url_prefix="/")
    app.register_blueprint(book_blueprint, url_prefix="/books")
    app.register_blueprint(member_blueprint, url_prefix="/members")
    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
