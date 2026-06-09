from flask import Flask

from config import Config
from extensions import db

from routes.auth_routes import auth_bp
from routes.dashboard_routes import dashboard_bp
from routes.hostel_routes import hostel_bp


def create_app():

    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)

    app.register_blueprint(auth_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(hostel_bp)

    with app.app_context():
        db.create_all()

    return app


app = create_app()


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )