from dataclasses import dataclass
from typing import List, Optional

@dataclass
class Question:
    prompt: str
    responseType: str
    dependantQuestions: Optional["List[Question]"]
    groups: Optional[List[str]]