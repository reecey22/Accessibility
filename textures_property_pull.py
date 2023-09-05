import os
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

def extract_properties_from_svgs(directory):
    svg_files = [file for file in os.listdir(directory) if file.endswith('.svg')]
    for svg_file in svg_files:
        svg_path = os.path.join(directory, svg_file)
        properties = extract_svg_properties(svg_path)
        for index, details in enumerate(properties):
            shape_type = details.tag.split('}')[-1]
            print(f"SVG File: {svg_file}")
            print(f"Shape Type: {shape_type}")
            print(f"Shape Index: {index}")
            for key, value in details.items():
                formatted_value = format_float_with_cm(value)
                print(f"{key}: {formatted_value}")
            print()

# Example usage
directory_path = 'C:/Users/Shaniah Reece/Documents/Tactile_Study_Materials/Tactile_Study_Materials/Encoding Files/Textures'
extract_properties_from_svgs(directory_path)


"""
# Code Review Comments:

# 1. Imports: The code imports the necessary modules (os and xml.etree.ElementTree), but it lacks comments explaining 
     why these specific modules are required for the task.

# 2. Error Handling: The code lacks error handling mechanisms. It doesn't handle potential exceptions that may occur when
     reading SVG files or parsing them. Consider adding try-except blocks to handle errors gracefully.

# 3. Magic Values: There are some hard-coded values in the code, such as '.svg' for file extension checking and 'cm' for unit 
    checking. Consider defining these as constants with meaningful names to improve code maintainability.

# 4. Function Documentation: While the function names are clear, there's a lack of docstrings (function documentation) 
     explaining the purpose, parameters, and return values of each function. Adding docstrings would make the code more understandable.

# 5. Limited Error Reporting: If there's an issue with an SVG file, the code doesn't provide detailed error reporting. 
     It would be helpful to log or report errors with specific file names or context to aid in debugging.

# 6. Potential Resource Leak: The code opens SVG files using a 'with' statement, which is good for resource cleanup. However, it 
    doesn't explicitly close the files after reading them. While Python often handles this automatically, explicitly closing 
    the files would be more robust.

# 7. Testing: The code doesn't include automated tests to verify the correctness of the functions. Consider adding unit tests
     to ensure that the code behaves as expected, especially as it evolves.

# 8. Separation of Concerns: The code combines file handling, SVG parsing, and property extraction in a single function. 
    Consider refactoring to separate these concerns into distinct functions, which can improve code modularity and testing.

# 9. Usability: The code assumes that all SVG files in the specified directory contain 'rect' or 'pattern' elements.
    It would be beneficial to handle cases where SVG files may not contain these elements gracefully.

# 10. Verbosity: The code is quite verbose in terms of printing information. Depending on the use case, you might want to consider 
    options for controlling the verbosity of the output.
    
# 11. Commenting: Adding comments throughout the code will promote understandability 

Overall, the code has a good foundation but lacks some important elements like error handling, documentation, and testing that would enhance its robustness and usability.

"""
