from flask import Flask

def create_app(env: str):
    app = Flask(__name__)
    app.config['ENV'] = env

    # Register routes
    from .routes.questionnaire_routes import questionnaire_blueprint
    app.register_blueprint(questionnaire_blueprint)

    return app