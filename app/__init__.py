from flask import Flask, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy

# Create database object globally
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # ✅ Required Configuration
    app.config['SECRET_KEY'] = 'your-secret-key'  # Replace with a secure one in production
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # ✅ Initialize DB
    db.init_app(app)

    # ✅ Optional: Default route
    @app.route('/')
    def index():
        if 'user' in session:
            return redirect(url_for('tasks.view_tasks'))
        return redirect(url_for('auth.login'))

    # ✅ Register Blueprints
    from app.routes.auth import auth_bp
    from app.routes.tasks import tasks_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(tasks_bp)

    return app
