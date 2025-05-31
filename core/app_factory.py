from flask import Flask
from controllers.dashboard_controller import dashboard_blueprint

class AppFactory:
    @staticmethod
    def create_app():
        """Initialize the Flask application, configure extensions, and register blueprints."""
        app = Flask(__name__)
        
        # Configuration (e.g., secret key, database URI)
        app.config['SECRET_KEY'] = 'your_secret_key'
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///lms.db'
        
        # Register blueprints
        #app.register_blueprint(book_blueprint, url_prefix='/books')
        #app.register_blueprint(member_blueprint, url_prefix='/members')
        #app.register_blueprint(author_blueprint, url_prefix='/authors')
        app.register_blueprint(dashboard_blueprint, url_prefix='/')
        
        return app