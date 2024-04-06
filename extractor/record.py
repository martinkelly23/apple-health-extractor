from dataclasses import dataclass

RECORD_ELEMENT = "Record"
TYPE = "@type"
VALUE = "@value"
START_DATE = "@startDate"
END_DATE = "@endDate"
CREATION_DATE = "@creationDate"
SOURCE_NAME = "@sourceName"
UNIT = "@unit"


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
        self.type = data.get(TYPE)
        self.start_date = data.get(START_DATE)
        self.end_date = data.get(END_DATE)
        self.creation_date = data.get(CREATION_DATE)
        self.source_name = data.get(SOURCE_NAME)
        self.unit = data.get(UNIT)
        self.value = data.get(VALUE)
