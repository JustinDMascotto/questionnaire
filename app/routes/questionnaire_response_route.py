from flask import Blueprint, request, jsonify
from datetime import datetime
from uuid import uuid4
from app.config.mongo import MongoSingleton
from app.models.questionnaire_response import QuestionnaireResponse
from dataclasses import asdict
from app.routes.constants.constants import base_route

questionnaire_response_blueprint = Blueprint('questionnaire_response', __name__)

@questionnaire_response_blueprint.route( base_route + '/<id>/<version>/responses/', methods=['POST'])
def create_response(id,version):
    data = request.get_json()
    try:
        questionnaire_response = QuestionnaireResponse(**data)
        print(questionnaire_response)
    except TypeError as e:
        return jsonify({'message':f"invalid data {e}",}), 400
    questionnaire_response.createdAt = datetime.utcnow()
    questionnaire_response._id = str(uuid4())
    questionnaire_response.questionnaireVersionedId = {
        "_id":id,
        "version":version
    }
    questionnaire_id = MongoSingleton.get_instance().flask_db.questionnaire_responses.insert_one(asdict(questionnaire_response))
    return jsonify({"_id": questionnaire_id.inserted_id}), 201