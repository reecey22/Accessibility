import os
import csv
import xml.etree.ElementTree as ET

def format_float_with_cm(value):
    if isinstance(value, str) and value.endswith('cm'):
        return f"{float(value[:-2]):.1f}cm"
    else:
        return value

def extract_svg_properties(svg_path):
    properties = []
    with open(svg_path, 'r') as svg_file:
        tree = ET.parse(svg_file)
        root = tree.getroot()
        for element in root.iter():
            if 'rect' in element.tag or 'pattern' in element.tag:
                properties.append(element)
    return properties

def extract_properties_from_svgs(directory, output_file):
    with open(output_file, 'w', newline='') as csvfile:
        fieldnames = ['SVG File', 'Shape Type', 'Shape Index', 'x', 'y', 'width', 'height', 'fill', 'stroke', 'stroke-width']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        svg_files = [file for file in os.listdir(directory) if file.endswith('.svg')]
        for svg_file in svg_files:
            svg_path = os.path.join(directory, svg_file)
            properties = extract_svg_properties(svg_path)
            for index, details in enumerate(properties):
                shape_type = details.tag.split('}')[-1]
                row_data = {'SVG File': svg_file, 'Shape Type': shape_type, 'Shape Index': index}
                for key, value in details.items():
                    formatted_value = format_float_with_cm(value)
                    row_data[key] = formatted_value
                writer.writerow(row_data)

directory_path = 'C:/Users/Shaniah Reece/Documents/Tactile_Study_Materials/Tactile_Study_Materials/Encoding Files/Textures'
output_file = 'C:/Users/Shaniah Reece/Documents/Tactile_Study_Materials/Tactile_Study_Materials/Encoding Files/Textures/Textures.csv'
extract_properties_from_svgs(directory_path, output_file)
