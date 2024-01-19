from app.models.questionnaire_response import QuestionnaireResponse
from dataclasses import asdict
from app.config.mongo import MongoSingleton
from uuid import uuid4
from datetime import datetime
from werkzeug.datastructures import ImmutableMultiDict
from datetime import datetime
import re

def create_response(response: QuestionnaireResponse,
                    id:str,
                    version:int):
    response.createdAt = datetime.utcnow()
    response._id = str(uuid4())
    response.questionnaireVersionedId = {
        "_id":id,
        "version":int(version)
    }
    return MongoSingleton.get_instance().flask_db.questionnaire_responses.insert_one(asdict(response))


def search(params:ImmutableMultiDict,
           id:str,
           version:int):

    # Initialize search criteria
    idAndVersionCriteria = {
        'questionnaireVersionedId':{
            "_id":id,
            "version":version
        }
    }
    criteria = [idAndVersionCriteria]

    filters = [CreatedAtFilter(),CreatedByFilter(),OrganizationIdFilter()]

    for filter in filters:
        criteria.extend(filter.parse(params))
                
    return list(MongoSingleton.get_instance().flask_db.questionnaire_responses.find({'$and':criteria}))



class SearchFilter:
    def parse(self,paramValue):
        raise NotImplemented("This is a base class and this method should be implemented in extending classes")
    
class CreatedAtFilter(SearchFilter):
    def parse(self,paramValue):
        created_dates = paramValue.getlist('createdAt')
        criteria = []
        if created_dates:
            for date_param in created_dates:
                match = re.match(r'(gte|lte|gt|lt|eq):(.+)', date_param)
                if match:
                    operator, date_str = match.groups()
                    
                    # Parse date
                    date = datetime.strptime(date_str,"%Y-%m-%dT%H:%M:%S.%f%z")
                    # Update search criteria based on operator
                    criteria.append({'createdAt':{'$'+operator: date}})

        return criteria
    
    
class CreatedByFilter(SearchFilter):
    def parse(self,paramValue):
        created_by = paramValue.get('createdBy')
        criteria = []
        if created_by:
            match = re.match(r'(eq):(.+)', created_by)
            if match:
                operator, created_by_str = match.groups()
                
                # Update search criteria based on operator
                criteria.append({'createdBy':{'$'+operator: created_by_str}})

        return criteria

class OrganizationIdFilter(SearchFilter):
    def parse(self,paramValue):
        created_by = paramValue.get('organizationId')
        criteria = []
        if created_by:
            match = re.match(r'(eq):(.+)', created_by)
            if match:
                operator, created_by_str = match.groups()
                
                # Update search criteria based on operator
                criteria.append({'organizationId':{'$'+operator: created_by_str}})

        return criteria
