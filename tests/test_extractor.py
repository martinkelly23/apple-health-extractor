import os

from extractor.extractor import Extractor


class TestExtractor:
    def test_extract_record_types(self):
        test_dir = os.path.dirname(__file__)
        health_file_path = os.path.join(test_dir, 'resources', 'health_data.xml')

        extractor = Extractor(file_src=health_file_path)

        assert set(extractor.record_types()) == {'HKQuantityTypeIdentifierStepCount',
                                                 'HKQuantityTypeIdentifierHeartRate'}

