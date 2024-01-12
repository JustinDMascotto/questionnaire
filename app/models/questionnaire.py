from dataclasses import dataclass
from app.models.versioned_id import VersionedId
from app.models.question import Question
from typing import List, Optional
from datetime import datetime

@dataclass
class Questionnaire:
    title: str
    questions: List[Question]
    organizationId: str
    createdBy: str
    _id: Optional[str] = None
    versionedId: Optional[VersionedId] = None
    groups: Optional[List[str]] = None
    createdAt: Optional[datetime] = None


