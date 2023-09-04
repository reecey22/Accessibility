import os
import xml.etree.ElementTree as ET

def extract_svg_properties(svg_path):
    properties = []
    with open(svg_path, 'r') as svg_file:
        tree = ET.parse(svg_file)
        root = tree.getroot()
        for element in root.iter():
            if 'circle' in element.tag:
                properties.append(element)
    return properties

def extract_properties_from_svgs(directory):
    svg_files = [file for file in os.listdir(directory) if file.endswith('.svg')]
    for svg_file in svg_files:
        svg_path = os.path.join(directory, svg_file)
        properties = extract_svg_properties(svg_path)
        print(f"SVG: {svg_file}")

        for index, details in enumerate(properties):
            print(f"CIRCLE {index}")
            for key, value in details.items():
                print(f"{key}: {value}")
        print()


directory_path = 'C:/Users/Shaniah Reece/Documents/Tactile_Study_Materials/Tactile_Study_Materials/Encoding Files/Areas'
extract_properties_from_svgs(directory_path)