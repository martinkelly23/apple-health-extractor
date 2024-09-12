from extractor import Extractor
import os

def main():
    # Path to your Apple Health export XML file
    # Replace this with the actual path to your XML file
    xml_path = "/Users/david/Desktop/tmp/apple_health_export/export.xml"
    
    # Check if the file exists
    if not os.path.exists(xml_path):
        print(f"Error: File not found at {xml_path}")
        return

    # Create an Extractor instance
    extractor = Extractor(xml_path)

    # Save data to CSV
    output_dir = "health_data_output"
    extractor.save_to_csv(filter_source="Cronometer")

    print(f"Data extracted and saved.")

    # After creating the extractor instance
    print("\nDistinct Types:")
    print(extractor.get_distinct_types())

    print("\nDistinct Source Names:")
    print(extractor.get_distinct_source_names())

    # Example: Print some basic stats
    #print("\nBasic Stats:")
    #print(f"Total records: {len(extractor.data)}")
    
    # Print the first few records
    #print("\nFirst few records:")
    #for record in extractor.data[:5]:
    #    print(record)

if __name__ == "__main__":
    main()