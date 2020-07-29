import os

from flask import Flask

from sif import bcrypt, jwt
from sif.model import db


def create_app(config=None):
    app = Flask(__name__, template_folder='templates')

    if config:
        app.config.from_object(config)

    # if os.getenv('CONFIG_PATH'):
    #     app.config.from_envvar(os.getenv('CONFIG_PATH'))

    with app.app_context():
        from sif.api.v1.movie import bp as movie_bp
        app.register_blueprint(movie_bp, url_prefix='/v1')
        from sif.api.v1.health import bp as health_bp
        app.register_blueprint(health_bp, url_prefix='/v1')
        from sif.api.v1.auth import bp as auth_bp
        app.register_blueprint(auth_bp, url_prefix='/v1')

    app.config['MONGODB_SETTINGS'] = {
        'db': os.getenv('MONGO_DB'),
        'host': os.getenv('MONGO_HOST'),
        'port': int(os.getenv('MONGO_PORT')),
        'username': os.getenv('MONGO_USER'),
        'password': os.getenv('MONGO_PASSWORD'),
        'connect': False,
    }
    app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')
    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)
    return app
