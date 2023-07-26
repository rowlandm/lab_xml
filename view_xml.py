import xml.etree.ElementTree as ET

def parse_xml(xml_string):
    # Parse the XML string into an ElementTree object
    root = ET.fromstring(xml_string)

    # Define the XML namespace (if used)
    namespace = "{http://www.sitemaps.org/schemas/sitemap/0.9}"

    # Find all URL elements and extract the URLs
    urls = []
    for url_elem in root.findall(f"{namespace}url"):
        loc_elem = url_elem.find(f"{namespace}loc")
        if loc_elem is not None:
            url = loc_elem.text.strip()
            urls.append(url)

    return urls

# Read from "lab.xml" file
file_path = "lab.xml"

try:
    with open(file_path, "r") as xml_file:
        xml_string = xml_file.read()
        urls = parse_xml(xml_string)
        print("List of URLs:")
        for url in urls:
            print(url)
except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found.")
except Exception as e:
    print(f"Error: An unexpected error occurred while parsing the XML file: {e}")

