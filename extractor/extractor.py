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

    def save_to_csv(self, output_file=None, filter_type=None, filter_source=None):
        if output_file is None:
            output_file = self.file_src.split(DIRECTORY_SEPARATOR)[FILE_NAME_INDEX].replace("xml", "csv")
        
        with open(output_file, "w", newline="") as csvfile:
            csv_writer = csv.writer(csvfile)

            headers = []
            filtered_records = []

            for record in self.health_data.get(RECORD_ELEMENT, []):
                record_obj = Record(**record)
                if (filter_type is None or record_obj.type == filter_type) and \
                   (filter_source is None or record_obj.source_name == filter_source):
                    filtered_records.append(record)
                    for key in record.keys():
                        if key not in headers:
                            headers.append(key)

            csv_writer.writerow(headers)

            for record in filtered_records:
                row = []
                for header in headers:
                    row.append(record.get(header, ""))
                csv_writer.writerow(row)

        print(f"Data saved to {output_file}")

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
    

    def get_distinct_types(self) -> List[str]:
        types = set()
        for record_data in self.health_data.get(RECORD_ELEMENT, []):
            record = Record(**record_data)
            types.add(record.type)
        return sorted(list(types))

    def get_distinct_source_names(self) -> List[str]:
        source_names = set()
        for record_data in self.health_data.get(RECORD_ELEMENT, []):
            record = Record(**record_data)
            source_names.add(record.source_name)
        return sorted(list(source_names))