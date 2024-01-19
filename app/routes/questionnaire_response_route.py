from flask import Blueprint, request, jsonify
from app.models.questionnaire_response import QuestionnaireResponse
from app.repository.questionnaire_response_repository import create_response, search
from app.routes.auth.auth import require_auth
from app.routes.constants.constants import base_route

questionnaire_response_blueprint = Blueprint('questionnaire_response', __name__)

@questionnaire_response_blueprint.route( base_route + '/<id>/<version>/responses/', methods=['POST'])
def create_response_endpoint(id,version):
    data = request.get_json()
    try:
        questionnaire_response = QuestionnaireResponse(**data)
        print(questionnaire_response)
    except TypeError as e:
        return jsonify({'message':f"invalid data {e}",}), 400
    
    response = create_response(questionnaire_response,id,int(version))

    return jsonify({"_id": response.inserted_id}), 201

@questionnaire_response_blueprint.route( base_route + "/<id>/<version>/responses", methods=["GET"])
@require_auth
def search_response_endpoint(id,version):
    try:
        foundResponses = search(request.args,id,int(version))
        return jsonify({'data':foundResponses}), 200
    except Exception as e:
        print(e)
        return jsonify({"error":"There was an error while searching"}), 400
    