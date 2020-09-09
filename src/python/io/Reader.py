from os import path # For opening the file w/ relative path
import re # For Regex on splitting strings


# Return a string representation of the file
def open_file(relative_file_path):
	file_contents = ''
	file_path = path.relpath(relative_file_path)
	with open(file_path) as file:
		file_contents += file.read()
	return file_contents

def parse_table(file_contents):
	table_name = ''
	table_list = file_contents.split() # splits on whisespace, (' ', '\t', '\n')

	create_index = table_list.index("CREATE")
	if( (table_list[create_index + 1] == "TABLE") and (create_index + 2 < len(table_list)) ):
		table_name = table_list[create_index + 2]

	table_name = table_name.replace('(', '')
	return table_name


def parse_attributes(table_contents):
	# start_inex = table_contents.index("(")
	# end_index = table_contents.index(")")
	x = table_contents.partition("(")
	attributes = x[2].split(",")

	for i in range(len(attributes)):
		attributes[i] = re.sub(r'[\n\t]+', '', attributes[i])


	print(attributes)
