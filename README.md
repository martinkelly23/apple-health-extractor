# Apple health data extractor
This library provides functionality to parse and extract data from the XML exports of Apple Health app, enabling users to analyze and utilize their health data conveniently.

### Features
Convert health data from XML format to JSON and CSV.
Retrieve types of records present in the health data.
Extract records of a specific type.

### Installation
You can install the library via pip:
```python
pip install apple-health-extractor
```

### Usage
```python
from extractor import Extractor

# Initialize the extractor with the path to the XML file
extractor = Extractor("path/to/health_data.xml")

# Get the health data as JSON
json_data = extractor.get_json()

# Save the health data to a CSV file
extractor.save_to_csv()

# Get the types of records available in the health data
record_types = extractor.get_record_types()

# Get records of a specific type
specific_records = extractor.get_records("HKQuantityTypeIdentifierHeartRate")
```

### Contributing
Contributions are welcome! Please fork the repository and open a pull request with your improvements.

### License
This project is licensed under the MIT License. See the LICENSE file for details.