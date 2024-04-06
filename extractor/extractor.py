import csv
from dataclasses import asdict
from typing import Any, List, Dict

import xmltodict

from extractor.constants.metadata import HEALTH_DATA_ELEMENT
from extractor.record import Record, RECORD_ELEMENT

FILE_NAME_INDEX = -1
DIRECTORY_SEPARATOR = "/"


class Extractor:
    def __init__(self, file_src: str):
        self.file_src = file_src

        with open(self.file_src) as file:
            xml = xmltodict.parse(file.read())
            self.health_data = xml[HEALTH_DATA_ELEMENT]

    def get_json(self):
        return self.health_data

    def save_to_csv(self):
        csv_output_file = self.file_src.split(DIRECTORY_SEPARATOR)[
            FILE_NAME_INDEX
        ].replace("xml", "csv")
        with open(csv_output_file, "w", newline="") as csvfile:
            csv_writer = csv.writer(csvfile)

            headers = []
            for record in self.health_data.get(RECORD_ELEMENT, []):
                for key in record.keys():
                    if key not in headers:
                        headers.append(key)
            csv_writer.writerow(headers)

            for record in self.health_data.get(RECORD_ELEMENT, []):
                row = []
                for header in headers:
                    row.append(record.get(header, ""))
                csv_writer.writerow(row)

    def get_record_types(self) -> list[str]:
        record_types = set()

        for record_data in self.health_data.get(RECORD_ELEMENT, []):
            record = Record(**record_data)
            record_types.add(record.type)

        return list(record_types)

    def get_records(self, record_type: str) -> List[Dict[str, Any]]:
        records = []

        for record_data in self.health_data.get(RECORD_ELEMENT, []):
            record = Record(**record_data)
            if record.type == record_type:
                records.append(asdict(record))

        return records
