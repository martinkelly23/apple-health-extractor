from extractor.constants.metadata import RECORD_ATTRIBUTES
from dataclasses import dataclass


@dataclass
class Record:
    type: str
    start_date: str
    end_date: str
    creation_date: str
    source_name: str
    value: float
    unit: str = None

    def __init__(self, **data):
        self.type = data.get(RECORD_ATTRIBUTES["type"])
        self.start_date = data.get(RECORD_ATTRIBUTES["start_date"])
        self.end_date = data.get(RECORD_ATTRIBUTES["end_date"])
        self.creation_date = data.get(RECORD_ATTRIBUTES["creation_date"])
        self.source_name = data.get(RECORD_ATTRIBUTES["source_name"])
        self.unit = data.get(RECORD_ATTRIBUTES["unit"])
        self.value = data.get(RECORD_ATTRIBUTES["value"])
