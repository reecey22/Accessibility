import os
import csv
import xml.etree.ElementTree as ET

def format_d_attribute(value):
    # Split the path data into individual commands (e.g., M, C) and coordinates
    commands = value.split(' ')
    formatted_values = []
    for command in commands:
        # Check if the command contains numerical coordinates
        if any(char.isdigit() for char in command):
            coordinates = command.split(',')
            formatted_coordinates = [f"{float(coord):.1f}" for coord in coordinates]
            formatted_values.append(','.join(formatted_coordinates))
        else:
            formatted_values.append(command)
    return ' '.join(formatted_values)

def format_transform_attribute(value):
    # Extract rotation angle and coordinates
    parts = value.split('(')[1].split(')')[0].split(',')
    angle = float(parts[0])
    coordinates = [f"{float(coord):.1f}" for coord in parts[1:]]
    return f"rotate({angle},{','.join(coordinates)})"

def extract_svg_properties(svg_path):
    properties = []
    with open(svg_path, 'r') as svg_file:
        tree = ET.parse(svg_file)
        root = tree.getroot()
        for element in root.iter():
            if 'path' in element.tag:
                properties.append(element)
    return properties

def extract_properties_from_svgs(directory, output_file):
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['SVG File', 'Element', 'd', 'transform'])

        svg_files = [file for file in os.listdir(directory) if file.endswith('.svg')]
        for svg_file in svg_files:
            svg_path = os.path.join(directory, svg_file)
            properties = extract_svg_properties(svg_path)

            for index, details in enumerate(properties):
                svg_file_name = os.path.basename(svg_file)
                element = f"CIRCLE {index}"
                d_value = format_d_attribute(details.get('d', ''))
                transform_value = format_transform_attribute(details.get('transform', ''))

                writer.writerow([svg_file_name, element, d_value, transform_value])


directory_path = 'C:/Users/Shaniah Reece/Documents/Tactile_Study_Materials/Tactile_Study_Materials/Encoding Files/Curvatures'
output_file = 'C:/Users/Shaniah Reece/Documents/Tactile_Study_Materials/Tactile_Study_Materials/Encoding Files/Curvatures/Curvatures.csv'
extract_properties_from_svgs(directory_path, output_file)
