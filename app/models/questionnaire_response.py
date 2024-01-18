from dataclasses import dataclass
from app.models.response import Response
from app.models.versioned_id import VersionedId
from typing import List, Optional
from datetime import datetime


@dataclass
class QuestionnaireResponse:
    responses: List[Response]
    questionnaireVersionedId: VersionedId
    organizationId: str
    createdBy: str
    _id: Optional[str] = None
    createdAt: Optional[datetime] = None
