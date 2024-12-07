from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.config import Config

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    # Register blueprints
    from app.api.employee_api import employee_bp

    app.register_blueprint(employee_bp, url_prefix="/api/employees")

    return app


# http://127.0.0.1:5000/api/employees