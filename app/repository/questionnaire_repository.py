from app.models.questionnaire import Questionnaire
from app.config.mongo import MongoSingleton
from datetime import datetime
from uuid import uuid4
from dataclasses import asdict

def create_questionnare(questionnaire: Questionnaire):
    questionnaire.createdAt = datetime.utcnow()
    id = uuid4()
    questionnaire.versionedId = {
        "_id":str(id),
        "version":1
    }
    questionnaire._id = str(id)
    return MongoSingleton.get_instance().flask_db.questionnaires.insert_one(asdict(questionnaire))

def update_questionnaire(questionnaire: Questionnaire,id:str):
    questionnaire.createdAt = datetime.utcnow()
    latest_questionnaire = MongoSingleton.get_instance().flask_db.questionnaires.find({'versionedId._id':id}).sort({'versionedId.version':-1}).limit(1).next()
    pk_id = uuid4()
    questionnaire.versionedId = {
        "_id":str(id),
        "version": latest_questionnaire['versionedId']['version'] + 1
    }
    questionnaire._id = str(pk_id)
    return MongoSingleton.get_instance().flask_db.questionnaires.insert_one(asdict(questionnaire))

def get_latest_questionnaire(id:str):
    query = {'versionedId._id':id}
    return MongoSingleton.get_instance().flask_db.questionnaires.find(query).sort({'versionedId.version':-1}).limit(1).next()

def get_questionnaire_version(id:str,version:int):
    query = {"versionedId":{
        "_id":id,
        "version": version
    }}
    return MongoSingleton.get_instance().flask_db.questionnaires.find_one(query)
