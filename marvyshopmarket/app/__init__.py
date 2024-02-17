from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:nidian56@localhost/marvy_shopmarket'
    app.config['SQLALCHEMY_BINDS'] = {
        'image':'mysql://root:nidian56@localhost/images'
    }
    db.init_app(app)
    
    from.routes import main_bp
    app.register_blueprint(main_bp)

    return app