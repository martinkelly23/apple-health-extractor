import os

from extractor.extractor import Extractor


class TestExtractor:
    def test_get_json(self):
        test_dir = os.path.dirname(__file__)
        health_file_path = os.path.join(test_dir, "resources", "health_data.xml")

        extractor = Extractor(file_src=health_file_path)

        assert extractor.get_json() == {
            "Record": [
                {
                    "@creationDate": "2022-03-25 08:00:00 +0000",
                    "@endDate": "2022-03-25 00:00:00 +0000",
                    "@sourceName": "iPhone",
                    "@sourceVersion": "12.1",
                    "@startDate": "2022-03-25 00:00:00 +0000",
                    "@type": "HKQuantityTypeIdentifierStepCount",
                    "@unit": "count",
                    "@value": "1500",
                },
                {
                    "@creationDate": "2022-03-25 08:00:00 +0000",
                    "@endDate": "2022-03-25 12:00:00 +0000",
                    "@sourceName": "iPhone",
                    "@sourceVersion": "12.1",
                    "@startDate": "2022-03-25 12:00:00 +0000",
                    "@type": "HKQuantityTypeIdentifierStepCount",
                    "@unit": "count",
                    "@value": "2500",
                },
                {
                    "@creationDate": "2022-03-25 08:30:00 +0000",
                    "@endDate": "2022-03-25 08:30:00 +0000",
                    "@sourceName": "Apple Watch",
                    "@sourceVersion": "8.0",
                    "@startDate": "2022-03-25 08:30:00 +0000",
                    "@type": "HKQuantityTypeIdentifierHeartRate",
                    "@unit": "count/min",
                    "@value": "72",
                },
            ]
        }

    def test_save_to_csv(self):
        test_dir = os.path.dirname(__file__)
        health_file_path = os.path.join(test_dir, "resources", "health_data.xml")
        expected_csv = (
            "@type,@sourceName,@sourceVersion,@unit,@creationDate,@startDate,@endDate,@value\n"
            "HKQuantityTypeIdentifierStepCount,iPhone,12.1,count,2022-03-25 08:00:00 "
            "+0000,2022-03-25 00:00:00 +0000,2022-03-25 00:00:00 +0000,1500\n"
            "HKQuantityTypeIdentifierStepCount,iPhone,12.1,count,2022-03-25 08:00:00 "
            "+0000,2022-03-25 12:00:00 +0000,2022-03-25 12:00:00 +0000,2500\n"
            "HKQuantityTypeIdentifierHeartRate,Apple Watch,8.0,count/min,2022-03-25 "
            "08:30:00 +0000,2022-03-25 08:30:00 +0000,2022-03-25 08:30:00 +0000,72\n"
        )

        extractor = Extractor(file_src=health_file_path)

        extractor.save_to_csv()
        temp_file_path = "health_data.csv"
        assert os.path.exists(temp_file_path)
        with open(temp_file_path, "r") as file:
            csv_data = file.read()
            assert csv_data == expected_csv

        os.remove(temp_file_path)

    def test_extract_record_types(self):
        test_dir = os.path.dirname(__file__)
        health_file_path = os.path.join(test_dir, "resources", "health_data.xml")

        extractor = Extractor(file_src=health_file_path)

        assert set(extractor.get_record_types()) == {
            "HKQuantityTypeIdentifierStepCount",
            "HKQuantityTypeIdentifierHeartRate",
        }

    def test_get_records_when_given_record_type(self):
        test_dir = os.path.dirname(__file__)
        health_file_path = os.path.join(test_dir, "resources", "health_data.xml")

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
            },
            {
                "type": "HKQuantityTypeIdentifierStepCount",
                "value": "2500",
                "start_date": "2022-03-25 12:00:00 +0000",
                "end_date": "2022-03-25 12:00:00 +0000",
                "creation_date": "2022-03-25 08:00:00 +0000",
                "source_name": "iPhone",
                "unit": "count",
            },
        ]
