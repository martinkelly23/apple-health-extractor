import xmltodict

from extractor.constants.metadata import HEALTH_DATA_ELEMENT, RECORD_ELEMENT, RECORD_ELEMENT_TYPE, RECORD_ELEMENT_VALUE, \
    RECORD_ELEMENT_START_DATE, RECORD_ELEMENT_END_DATE, RECORD_ELEMENT_CREATION_DATE


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

    def get_records(self, record_type: str) -> list[dict]:
        values = []

        for record in self.health_data.get(RECORD_ELEMENT, []):
            if record.get(RECORD_ELEMENT_TYPE) == record_type:
                values.append({
                    "value": record.get(RECORD_ELEMENT_VALUE),
                    "start_date": record.get(RECORD_ELEMENT_START_DATE),
                    "end_date": record.get(RECORD_ELEMENT_END_DATE),
                    "creation_date": record.get(RECORD_ELEMENT_CREATION_DATE),
                })

        return values
