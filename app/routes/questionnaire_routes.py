from flask import Blueprint, request, jsonify
from app.routes.auth.auth import require_auth
from datetime import datetime
from uuid import uuid4
from app.config.mongo import MongoSingleton
from app.models.questionnaire import Questionnaire
from dataclasses import asdict
from app.routes.constants.constants import base_route
from app.repository.questionnaire_repository import create_questionnare, update_questionnaire, get_latest_questionnaire, get_questionnaire_version

questionnaire_blueprint = Blueprint('questionnaire', __name__)

@questionnaire_blueprint.route( base_route + '/', methods=['POST'])
@require_auth
def create_questionnaire():
    data = request.get_json()
    try:
        questionnaire = Questionnaire(**data)
    except TypeError as e:
        return jsonify({'message':f"invalid data {e}",}), 400
    
    create_questionnare(questionnaire)
    
    return jsonify({'versionedId': questionnaire.versionedId}), 201

@questionnaire_blueprint.route( base_route + '/<id>', methods=['PUT'])
@require_auth
def update(id):
    data = request.get_json()
    try:
        questionnaire = Questionnaire(**data)
    except TypeError as e:
        return jsonify({'message':f"invalid data {e}",}), 400
    
    update_questionnaire(questionnaire,id)
    
    return jsonify({'versionedId': questionnaire.versionedId}), 200

@questionnaire_blueprint.route( base_route + '/<id>', methods=['GET'])
def get_questionnaire_latest(id):
    questionnaire = get_latest_questionnaire(id)
    if questionnaire:
        return jsonify(questionnaire), 200
    return jsonify({'error': 'Questionnaire not found'}), 404

@questionnaire_blueprint.route( base_route + '/<id>/<version>', methods=['GET'])
def get_questionnaire_by_version(id,version):
    questionnaire = get_questionnaire_version(id,int(version))
    if questionnaire:
        return jsonify(questionnaire), 200
    return jsonify({'error': 'Questionnaire not found'}), 404
