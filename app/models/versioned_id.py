from dataclasses import dataclass

@dataclass
class VersionedId:
    id: str
    version: int