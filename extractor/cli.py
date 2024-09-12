import argparse
import os
from .extractor import Extractor

def main():
    parser = argparse.ArgumentParser(description="Extract and filter Apple Health data")
    parser.add_argument("xml_path", help="Path to the Apple Health export XML file")
    parser.add_argument("-o", "--output", help="Output CSV file name", default="health_data.csv")
    parser.add_argument("-t", "--type", help="Filter by record type")
    parser.add_argument("-s", "--source", help="Filter by source name")
    parser.add_argument("--list-types", action="store_true", help="List all distinct record types")
    parser.add_argument("--list-sources", action="store_true", help="List all distinct source names")
    
    args = parser.parse_args()

    if not os.path.exists(args.xml_path):
        print(f"Error: File not found at {args.xml_path}")
        return

    extractor = Extractor(args.xml_path)

    if args.list_types:
        print("\nDistinct Types:")
        for type_ in extractor.get_distinct_types():
            print(type_)
        return

    if args.list_sources:
        print("\nDistinct Source Names:")
        for source in extractor.get_distinct_source_names():
            print(source)
        return

    extractor.save_to_csv(args.output, filter_type=args.type, filter_source=args.source)
    print(f"Data extracted and saved to {args.output}")

if __name__ == "__main__":
    main()