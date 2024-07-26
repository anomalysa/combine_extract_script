import os

# Define paths
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
folder_path = os.path.join(desktop_path, "Baseplate_results")
backside_file = os.path.join(folder_path, "Backside_results.txt")
flatness_file = os.path.join(folder_path, "Flatness.txt")
combined_file = os.path.join(folder_path, "Baseplate_results.txt")
output_file_path = os.path.join(folder_path, "Filtered_results.txt")

# Combine files
with open(flatness_file, 'r') as flatness:
    flatness_content = flatness.read()

with open(backside_file, 'r') as backside:
    backside_content = backside.read()

combined_content = backside_content + "\n" + "="*40 + "\n" + flatness_content

with open(combined_file, 'w') as combined:
    combined.write(combined_content)

print("Files have been combined into 'Baseplate_results.txt'.")

# Define filtering and extraction functions
def is_desired_line(line):
    return any(keyword in line for keyword in ["Component ID:", "Component Material:", "Component Thickness(in mm):", "Flatness ="])

def extract_parameters(lines):
    component_id = None
    component_material = None
    component_thickness = None
    flatness = None

    for line in lines:
        if "Component ID:" in line and not component_id:
            component_id = line.split("Component ID:")[1].strip()
        elif "Component Material:" in line and not component_material:
            component_material = line.split("Component Material:")[1].strip()
        elif "Component Thickness(in mm):" in line and not component_thickness:
            component_thickness = line.split("Component Thickness(in mm):")[1].strip()
        elif "Flatness =" in line and not flatness:
            flatness = line.split("Flatness =")[1].strip()

    if component_id and component_material and component_thickness and flatness:
        return f"{component_id}, {component_material}, Full, {flatness}, {component_thickness}, Green"
    else:
        return None

def filter_and_convert_file(input_file_path, output_file_path):
    with open(input_file_path, 'r') as input_file:
        lines = input_file.readlines()

    desired_lines = []
    encountered_params = set()

    for line in lines:
        if is_desired_line(line):
            param_type = line.split(":")[0]
            if param_type not in encountered_params:
                encountered_params.add(param_type)
                desired_lines.append(line.strip() + "\n")
    
    combined_params = extract_parameters(desired_lines)
    
    if combined_params:
        # Prompt the user for the "component passed" value
        while True:
            component_passed = input("Component passed (true/false): ").strip().lower()
            if component_passed in ["true", "false"]:
                combined_params += f", {component_passed}\n"
                break
            else:
                print("Please enter 'true' or 'false'.")

        # Write the combined parameters to the output file
        with open(output_file_path, 'w') as output_file:
            output_file.write(combined_params)

# Combine the files and filter the results
filter_and_convert_file(combined_file, output_file_path)

print(f"Filtered results saved to {output_file_path}")
