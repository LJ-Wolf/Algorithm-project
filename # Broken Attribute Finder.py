# Broken Attribute Finder

import xml.etree.ElementTree as ET

def is_broken(attributeValue):
    return attributeValue is None or attributeValue.strip() == ""

def find_BrokenAttribute(element, path=""):

    for attr_name, attr_value in element.attrib.items():
        if is_broken(attr_value):
            print(f"Broken attribute found: {attr_name}")

    for child in element:
        find_BrokenAttribute(child)

def main():
    file_path = "XMLexampleFile.xml"

    try:
        tree = ET.parse(file_path)
        root = tree.getroot()

        print(f"Checking for broken attributes in the XML document ({file_path}):")
        find_BrokenAttribute(root)

    except FileNotFoundError:
        print("File not found")
    except ET.ParseError as e:
        print(f"Failed to parse the XML document. Details: {e}")

if __name__ == "__main__":
    main()