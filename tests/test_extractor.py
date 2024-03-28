import os

from extractor.extractor import Extractor


class TestExtractor:
    def test_extract_record_types(self):
        test_dir = os.path.dirname(__file__)
        health_file_path = os.path.join(test_dir, 'resources', 'health_data.xml')

        extractor = Extractor(file_src=health_file_path)

        assert set(extractor.get_record_types()) == {'HKQuantityTypeIdentifierStepCount',
                                                     'HKQuantityTypeIdentifierHeartRate'}

    def test_get_records_when_given_record_type(self):
        test_dir = os.path.dirname(__file__)
        health_file_path = os.path.join(test_dir, 'resources', 'health_data.xml')

        extractor = Extractor(file_src=health_file_path)

        assert extractor.get_records("HKQuantityTypeIdentifierStepCount") == [
            {
                "type": "HKQuantityTypeIdentifierStepCount",
                "value": "1500",
                "start_date": "2022-03-25 00:00:00 +0000",
                "end_date": "2022-03-25 00:00:00 +0000",
                "creation_date": "2022-03-25 08:00:00 +0000",
                "source_name": "iPhone",
                "unit": "count",
            }, {
                "type": "HKQuantityTypeIdentifierStepCount",
                "value": "2500",
                "start_date": "2022-03-25 12:00:00 +0000",
                "end_date": "2022-03-25 12:00:00 +0000",
                "creation_date": "2022-03-25 08:00:00 +0000",
                "source_name": "iPhone",
                "unit": "count",
            }
        ]
