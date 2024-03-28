import xmltodict


class Extractor:
    def __init__(self, file_src: str):
        self.file_src = file_src

        with open(self.file_src) as file:
            xml = xmltodict.parse(file.read())
            self.health_data = xml["HealthData"]

    def record_types(self) -> list[str]:
        record_types = set()

        for record in self.health_data.get('Record', []):
            record_type = record.get('@type')

            if record_type:
                record_types.add(record_type)

        return list(record_types)
