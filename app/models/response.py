from dataclasses import dataclass
from typing import List, Optional

@dataclass
class Response:
    prompt: str
    responseType: str
    response: str