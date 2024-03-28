import xmltodict

from extractor.constants.metadata import HEALTH_DATA_ELEMENT, RECORD_ELEMENT, RECORD_ELEMENT_TYPE, RECORD_ELEMENT_VALUE


class Extractor:
    def __init__(self, file_src: str):
        self.file_src = file_src

        with open(self.file_src) as file:
            xml = xmltodict.parse(file.read())
            self.health_data = xml[HEALTH_DATA_ELEMENT]

    def get_record_types(self) -> list[str]:
        record_types = set()

        for record in self.health_data.get(RECORD_ELEMENT, []):
            record_type = record.get(RECORD_ELEMENT_TYPE)

            if record_type:
                record_types.add(record_type)

        return list(record_types)

    def get_record_values(self, record_type: str) -> list[str]:
        values = []

        for record in self.health_data.get(RECORD_ELEMENT, []):
            if record.get(RECORD_ELEMENT_TYPE) == record_type:
                value = record.get(RECORD_ELEMENT_VALUE)
                if value:
                    values.append(value)

        return values
