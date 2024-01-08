from flask.json.provider import DefaultJSONProvider
from datetime import datetime

class CustomJsonProvider(DefaultJSONProvider):

    def default(self, o):
        if(isinstance(o,datetime)):
            return o.strftime('%Y-%m-%dT%H:%M:%S')
        return super().default(o)

    def dumps(self,obj,**kw):
        """
        Define how to serialize objects that aren't natively serializable by json.dumps.

        Returns:
        - A dictionary if the object is a FireO model
        - A list of dictionaries if the object is a FireO QueryIterator or list of models
        - Datetime objects are serialized to iso strings
        - All other clases are delegated back to DefaultJSONProvider
        """
        if(isinstance(obj,datetime)):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        
        return super().dumps(obj,**kw)