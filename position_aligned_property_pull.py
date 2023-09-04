import os
import xml.etree.ElementTree as ET

def format_float_with_cm(value):
    if isinstance(value, str) and value.endswith('cm'):
        numeric_value = float(value[:-2])
        return f"{numeric_value:.1f}cm"
    elif isinstance(value, float):
        return f"{value:.1f}"
    else:
        return value

def extract_svg_properties(svg_path):
    properties = []
    with open(svg_path, 'r') as svg_file:
        tree = ET.parse(svg_file)
        root = tree.getroot()
        for element in root.iter():
            if 'circle' in element.tag or 'rect' in element.tag:
                properties.append(element)
    return properties

def extract_properties_from_svgs(directory):
    svg_files = [file for file in os.listdir(directory) if file.endswith('.svg')]
    for svg_file in svg_files:
        svg_path = os.path.join(directory, svg_file)
        properties = extract_svg_properties(svg_path)
        for shape_index, details in enumerate(properties):
            shape_type = details.tag.split('}')[-1]
            print(f"SVG File: {svg_file}")
            print(f"Shape Type: {shape_type}")
            print(f"Shape Index: {shape_index}")
            for key, value in details.items():
                formatted_value = format_float_with_cm(value)
                print(f"{key}: {formatted_value}")
            print()

directory_path = 'C:/Users/Shaniah Reece/Documents/Tactile_Study_Materials/Tactile_Study_Materials/Encoding Files/Position_Aligned'
extract_properties_from_svgs(directory_path)
