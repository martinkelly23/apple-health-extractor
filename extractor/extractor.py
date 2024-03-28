from dataclasses import asdict
from typing import Any

import xmltodict

from extractor.constants.metadata import HEALTH_DATA_ELEMENT, RECORD_ELEMENT, RECORD_ATTRIBUTES
from extractor.record import Record


class Extractor:
    def __init__(self, file_src: str):
        self.file_src = file_src

        with open(self.file_src) as file:
            xml = xmltodict.parse(file.read())
            self.health_data = xml[HEALTH_DATA_ELEMENT]

    def get_record_types(self) -> list[str]:
        record_types = set()

        for record in self.health_data.get(RECORD_ELEMENT, []):
            record_type = record.get(RECORD_ATTRIBUTES["type"])

            if record_type:
                record_types.add(record_type)

        return list(record_types)

    def get_records(self, record_type: str) -> list[dict[str, Any]]:
        values = []

        for record in self.health_data.get(RECORD_ELEMENT, []):
            if record.get(RECORD_ATTRIBUTES["type"]) == record_type:
                values.append(asdict(Record(**record)))

        return values
