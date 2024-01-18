from flask import Flask
from app.routes.serialization.custom_json_provider import CustomJsonProvider

def create_app(env: str):
    app = Flask(__name__)
    app.config['ENV'] = env

    # Register routes
    from .routes.questionnaire_routes import questionnaire_blueprint
    app.register_blueprint(questionnaire_blueprint)
    from .routes.questionnaire_response_route import questionnaire_response_blueprint
    app.register_blueprint(questionnaire_response_blueprint)
    app.json_provider_class = CustomJsonProvider
    app.json = CustomJsonProvider(app)

    return app