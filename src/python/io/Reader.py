from os import path # For opening the file w/ relative path
import re # For Regex on splitting strings

# Return a string representation of the file
def open_file(relative_file_path):
	file_contents = ''
	file_path = path.relpath(relative_file_path)
	with open(file_path) as file:
		file_contents += file.read()
	return file_contents

# Return the name of the table
def parse_table(file_contents):
	table_name = ''
	table_list = file_contents.split() # splits on whisespace, (' ', '\t', '\n')

	create_index = table_list.index("CREATE")
	if( (table_list[create_index + 1] == "TABLE") and (create_index + 2 < len(table_list)) ):
		table_name = table_list[create_index + 2]

	table_name = table_name.replace('(', '')
	return table_name


possible_data_types = 	[
							"CHAR", "VARCHAR", "BINARY", "VARBINARY",
							"BIT", "TININT", "BOOL", "BOOLEAN",
							"SMALLINT", "INT", "INTEGER", "BIGINT",
							"FLOAT", "DOUBLE", "DECIMAL", "DEC",
							"DATE", "DATETIME", "TIMESTAMP", "TIME",
							"YEAR"
						]

# Helper function to clean the attribute list
def remove_non_attributes(attribute_list):
	for i in range(len(attribute_list)):
		# Remove tabs and new lines
		attribute_list[i] = re.sub(r'[\n\t]+', '', attribute_list[i])
		# Remove anything containing a SQL keyword
		contains = False
		for dt in possible_data_types:
			if dt in attribute_list[i]:
				contains = True
		if(not contains):
			attribute_list[i] = ""
	clean_list = []
	for a in attribute_list:
		if a != "":
			clean_list.append(a)
	return clean_list

# return a dictionary with keys of the entity attributes
# and values as the data types
def parse_attributes(table_contents):
	x = table_contents.partition("(")
	attributes = x[2].split(",")
	attribute_list = remove_non_attributes(attributes)

	attribute_dict = {}
	for i in range(len(attribute_list)):
		# Split on whitespace
		attribute_index_split = attribute_list[i].split()
		for j in range(len(attribute_index_split)):
			# Remove '(*)'
			attribute_index_split[j] = re.sub(r'\(.*\)', '', attribute_index_split[j])
			if attribute_index_split[j] in possible_data_types:
				key = attribute_index_split[j - 1]
				value = attribute_index_split[j]
				attribute_dict[key] = value
	return attribute_dict
