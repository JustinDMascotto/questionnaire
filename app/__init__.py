from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['MONGODB_SETTINGS'] = {
        'db': 'questionnaire_db',
        'host': 'localhost',
        'port': 27017
    }

    # Register routes
    from .routes.questionnaire_routes import questionnaire_blueprint
    app.register_blueprint(questionnaire_blueprint)

    return app