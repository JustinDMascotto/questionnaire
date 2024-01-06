from flask import Blueprint, request, jsonify
from app.auth.auth import require_auth
from datetime import datetime
from uuid import uuid4
from app.config.mongo import MongoSingleton

questionnaire_blueprint = Blueprint('questionnaire', __name__)

base_route = '/v1/questionnaire'

@questionnaire_blueprint.route( base_route + '/', methods=['POST'])
@require_auth
def create_questionnaire():
    data = request.json
    data["createdAt"] = datetime.utcnow()
    data["_id"] = str(uuid4())
    questionnaire_id = MongoSingleton.get_instance().flask_db.questionnaires.insert_one(data)
    return jsonify({"message": "Questionnaire created successfully", "id": str(questionnaire_id)}), 201

@questionnaire_blueprint.route( base_route + '/<id>', methods=['GET'])
@require_auth
def get_questionnaire(id):
    questionnaire = MongoSingleton.get_instance().flask_db.questionnaires.find_one({"_id":id})
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