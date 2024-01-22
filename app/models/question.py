from dataclasses import dataclass
from typing import List, Optional, Dict

@dataclass
class Question:
    prompt: str
    responseType: str
    detail: Optional[Dict]
    dependantQuestions: Optional["List[Question]"]
    groups: Optional[List[str]]