from flask import Blueprint, request, jsonify
from app.auth.auth import require_auth
from datetime import datetime
from uuid import uuid4
from app.config.mongo import MongoSingleton
from app.models.questionnaire import Questionnaire
from dataclasses import asdict
from app.routes.constants.constants import base_route

questionnaire_blueprint = Blueprint('questionnaire', __name__)

@questionnaire_blueprint.route( base_route + '/', methods=['POST'])
@require_auth
def create_questionnaire():
    data = request.get_json()
    try:
        questionnaire = Questionnaire(**data)
    except TypeError as e:
        return jsonify({'message':f"invalid data {e}",}), 400
    questionnaire.createdAt = datetime.utcnow()
    id = uuid4()
    questionnaire.versionedId = {
        "_id":str(id),
        "version":"1"
    }
    questionnaire._id = str(id)
    questionnaire_id = MongoSingleton.get_instance().flask_db.questionnaires.insert_one(asdict(questionnaire))
    return jsonify({'versionedId': questionnaire.versionedId}), 201

@questionnaire_blueprint.route( base_route + '/<id>', methods=['PUT'])
@require_auth
def update_questionnaire(id):
    data = request.get_json()
    try:
        questionnaire = Questionnaire(**data)
    except TypeError as e:
        return jsonify({'message':f"invalid data {e}",}), 400
    questionnaire.createdAt = datetime.utcnow()
    latest_questionnaire = MongoSingleton.get_instance().flask_db.questionnaires.find({'versionedId._id':id}).sort({'versionedId.version':-1}).limit(1).next()
    pk_id = uuid4()
    questionnaire.versionedId = {
        "_id":str(id),
        "version": str(int(latest_questionnaire['versionedId']['version']) + 1)
    }
    questionnaire._id = str(pk_id)
    questionnaire_id = MongoSingleton.get_instance().flask_db.questionnaires.insert_one(asdict(questionnaire))
    return jsonify({'versionedId': questionnaire.versionedId}), 200

@questionnaire_blueprint.route( base_route + '/<id>', methods=['GET'])
def get_questionnaire_versions(id):
    questionnaires = list(MongoSingleton.get_instance().flask_db.questionnaires.find({"versionedId._id":id}))
    if questionnaires:
        return jsonify(questionnaires), 200
    return jsonify({'error': 'Questionnaire not found'}), 404

@questionnaire_blueprint.route( base_route + '/<id>/<version>', methods=['GET'])
def get_questionnaire(id,version):
    if version == 'latest':
        query = {'versionedId._id':id}
    else:
        query = {"versionedId":{
        "_id":id,
        "version":version
    }}
    questionnaire = MongoSingleton.get_instance().flask_db.questionnaires.find(query).sort({'versionedId.version':-1}).limit(1).next()
    if questionnaire:
        return jsonify(questionnaire), 200
    return jsonify({'error': 'Questionnaire not found'}), 404

# @questionnaire_blueprint.route('/get/<id>', methods=['GET'])
# @require_auth
# def get_questionnaire(id):
#     questionnaire = Questionnaire.objects(id=id).first()
#     if questionnaire:
#         return jsonify(questionnaire.to_json()), 200
#     return jsonify({'error': 'Questionnaire not found'}), 404

# @questionnaire_blueprint.route('/submit', methods=['POST'])
# @require_auth
# def submit_answers():
#     data = request.json
#     response = Response(**data)
#     response.save()
#     return jsonify({'id': str(response.id)}), 201

# @questionnaire_blueprint.route('/responses/<id>', methods=['GET'])
# @require_auth
# def get_responses(id):
#     responses = Response.objects(questionnaire_id=id)
#     return jsonify(responses.to_json()), 200