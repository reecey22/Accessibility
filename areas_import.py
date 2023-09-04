import os
import csv
import xml.etree.ElementTree as ET

def extract_svg_properties(svg_path):
    properties = []
    with open(svg_path, 'r') as svg_file:
        tree = ET.parse(svg_file)
        root = tree.getroot()
        for element in root.iter():
            if 'circle' in element.tag:
                properties.append(element.attrib)
    return properties

def format_value(value):
    if value.endswith("cm"):
        try:
            value = float(value[:-2])
            value = round(value, 1)
            return f"{value:.1f}cm"
        except ValueError:
            return value
    return value

def extract_properties_from_svgs(directory, output_file):
    with open(output_file, 'w', newline='') as csv_file:
        fieldnames = ['SVG File', 'Element', 'X', 'Y', 'Radius']
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        csv_writer.writeheader()

        svg_files = [file for file in os.listdir(directory) if file.endswith('.svg')]
        for svg_file in svg_files:
            svg_path = os.path.join(directory, svg_file)
            properties = extract_svg_properties(svg_path)
            print(f"SVG: {svg_file}")

            for index, details in enumerate(properties):
                row_data = {
                    'SVG File': svg_file,
                    'Element': index,
                    'X': format_value(details.get('cx', '')),
                    'Y': format_value(details.get('cy', '')),
                    'Radius': format_value(details.get('r', ''))
                }
                csv_writer.writerow(row_data)

directory_path = 'C:/Users/Shaniah Reece/Documents/Tactile_Study_Materials/Tactile_Study_Materials/Encoding Files/Areas'
output_file = 'C:/Users/Shaniah Reece/Documents/Tactile_Study_Materials/Tactile_Study_Materials/Encoding Files/Areas/Areas.csv'
extract_properties_from_svgs(directory_path, output_file)
