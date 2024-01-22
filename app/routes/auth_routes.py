from flask import Blueprint, request, jsonify
from app.models.questionnaire_response import QuestionnaireResponse
from app.repository.questionnaire_response_repository import create_response, search
from app.routes.auth.auth import require_auth
from app.routes.constants.constants import base_route

auth_blueprint = Blueprint('auth', __name__)

@auth_blueprint.route('/v1/auth/basic', methods=['GET'])
@require_auth
def create_response_endpoint():
    return '', 200

    