import os
import csv
import xml.etree.ElementTree as ET

def format_float(value):
    # Check if the value is a string and ends with "cm"
    if isinstance(value, str) and value.endswith("cm"):
        # Extract the numerical part, convert to float, and format to one decimal place
        numerical_value = float(value[:-2])
        formatted_value = f"{numerical_value:.1f}cm"
        return formatted_value
    # Check if the value is a float and format it to one decimal place
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
            if 'line' in element.tag:
                properties.append(element)
    return properties

def extract_properties_from_svgs(directory, output_file):
    with open(output_file, 'w', newline='') as csvfile:
        fieldnames = ['SVG File', 'Line Index', 'stroke','stroke-width', 'x1','x2', 'y2', 'y1']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        svg_files = [file for file in os.listdir(directory) if file.endswith('.svg')]
        for svg_file in svg_files:
            svg_path = os.path.join(directory, svg_file)
            properties = extract_svg_properties(svg_path)
            for index, details in enumerate(properties):
                row_data = {'SVG File': svg_file, 'Line Index': index}
                for key, value in details.items():
                    formatted_value = format_float(value)
                    row_data[key] = formatted_value
                writer.writerow(row_data)

# Example usage
# Folder path with all the svg files.
directory_path = 'C:/Users/Shaniah Reece/Documents/Tactile_Study_Materials/Tactile_Study_Materials/Encoding Files/Lines'
output_path = 'C:/Users/Shaniah Reece/Documents/Tactile_Study_Materials/Tactile_Study_Materials/Encoding Files/Lines/Lines.csv'
extract_properties_from_svgs(directory_path, output_path)
