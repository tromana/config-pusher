import jinja2
import json
import os


template_file = raw_input("Enter the Jinja File:")
json_params_file = raw_input("Enter the Paramter skeleton:")
output_directory = "config_output"

# read the contents from the JSON files
print("Read JSON parameter file...")
config_parameters = json.load(open(json_params_file))

# next we need to create the central Jinja2 environment and we will load
# the Jinja2 template file (the two parameters ensure a clean output in the
# configuration file)
print("Create Jinja2 environment...")
env = jinja2.Environment(loader=jinja2.FileSystemLoader(searchpath="."),
                         trim_blocks=True,
                         lstrip_blocks=True)
template = env.get_template(template_file)

# we will make sure that the output directory exists
if not os.path.exists(output_directory):
    os.mkdir(output_directory)

# now create the templates
print("Create templates...")
for parameter in config_parameters:
    result = template.render(parameter)
    f = open(os.path.join(output_directory, parameter['hostname'] + ".cfg"), "w")
    f.write(result)
    f.close()
    print("Configuration '%s' created..." % (parameter['hostname'] + ".cfg"))
print("DONE")