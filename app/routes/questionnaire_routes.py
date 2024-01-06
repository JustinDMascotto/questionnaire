from flask import Blueprint, request, jsonify
from app.auth.auth import require_auth

questionnaire_blueprint = Blueprint('questionnaire', __name__)

@questionnaire_blueprint.route('/create', methods=['POST'])
@require_auth
def create_questionnaire():
    data = request.json
    data["createdAt"] = datetime.datetime.utcnow()
    questionnaire_id = mongo.db.questionnaires.insert_one(data).inserted_id
    return jsonify({"message": "Questionnaire created successfully", "id": str(questionnaire_id)}), 201

@questionnaire_blueprint.route('/get/<id>', methods=['GET'])
@require_auth
def get_questionnaire(id):
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