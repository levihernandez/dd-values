import streamlit as st
import yaml

# Load values.yaml
def load_yaml(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

# Function to generate YAML content based on selected options
def generate_yaml_content(selected_values):
    return yaml.dump(selected_values)

# Function to display configuration options
def display_config_options(config, selected_values, parent_key=''):
    for key, value in config.items():
        full_key = f"{parent_key}.{key}" if parent_key else key
        if isinstance(value, dict):
            # Display nested dictionary without nesting expanders
            st.subheader(full_key)
            display_config_options(value, selected_values, full_key)  # Call recursively
        elif isinstance(value, bool):
            selected_values[full_key] = st.checkbox(full_key, value=value, key=f"checkbox_{full_key}")
        elif isinstance(value, list):
            selected_values[full_key] = st.multiselect(full_key, options=value, default=value, key=f"multiselect_{full_key}")
        else:
            selected_values[full_key] = st.text_input(full_key, value=value, key=f"textinput_{full_key}")

# Load your specific values.yaml file
values = load_yaml('conf/values.yaml')  # Adjusted path

# Streamlit UI
st.title("Datadog Helm Chart Customizer")

# Dictionary to hold user-selected values
selected_values = {}

# Display the configuration options
display_config_options(values, selected_values)

# Bundles to enable
bundles = st.multiselect("Select Bundles to Enable", ["bundle1", "bundle2", "bundle3"], key="bundles_select")
selected_values['enabled_bundles'] = bundles

# Button to generate preview
if st.button("Generate Preview"):
    st.subheader("Preview of values.yaml")
    yaml_preview = generate_yaml_content(selected_values)
    st.code(yaml_preview, language='yaml')

    # Button to download the generated YAML
    st.download_button("Download YAML", yaml_preview, file_name='values.yaml', mime='text/yaml')
