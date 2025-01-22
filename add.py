import sys

# Check if argument is passed
if len(sys.argv) != 2:
    print("Usage: python add.py <filename>")
    sys.exit(1)

# Read the argument (file path)
config_file = sys.argv[1]

# Open the config file and read its content
with open(config_file, 'r') as file:
    content = file.read()

# Print the content of the config file
print("Hello World! Here is the content from the config file:")
print(content)
