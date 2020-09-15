"""
	Writing out the .java files
"""
class Entity_Writer(object):
	def __init__(self, table):
		self._table = table

	def get_java_equivanlency(self, sql_type):
		type_equiv_dict = {
			'CHAR': 'String', 'VARCHAR': 'String', 'YEAR' : 'String',
			'Binary': 'byte[]', 'VARBINARY' : 'byte[]',
			'BIT' : 'boolean', 'BOOL' : 'boolean', 'BOOLEAN' : 'boolean',
			'TINYINT' : 'Integer', 'SMALLINT' : 'Integer', 'INT' : 'Integer', 'INTEGER' : 'Integer',
			'BIGINT' : 'Long',
			'FLOAT' : 'Float',
			'DOUBLE' : 'Double', 'DOUBLE PRECISION' : 'Double',
			'DECIMAL' : 'BigDecimal', 'DEC' : 'BigDecimal', # java.math.BigDecimal
			'DATE' : 'Date', # java.sql.Date
			'DATETIME' : 'Timestamp', 'TIMESTAMP' : 'Timestamp' # java.sql.Timestamp
		}

		return type_equiv_dict[sql_type]

	# Helper method to turn the Table's attribute_dict into one with java types
	def get_java_variables_dict(self, attribute_dict):
		java_var_dict = {}
		for key, value in attribute_dict.items():
			java_equiv_type = self.get_java_equivanlency(value)
			java_var_dict[key] = java_equiv_type
		return java_var_dict

	def write_entity(self, target_file_path):
		# Write Intro Comments
		new_file = open('Account.java', 'w')
		comments = f"/**\n  * This file was created using springGen\n **/\n"
		new_file.write(comments)

		# Write Header
		header = ["@Entity\n", f"@Table(name=\"{self._table.get_name()}\")\n"]
		new_file.writelines(header)

		# write class
		class_line = [f"public class {self._table.get_name()}", " {\n"]
		new_file.writelines(class_line)
		# Write Variables

		variables = []
		java_vars = self.get_java_variables_dict(self._table.get_attributes())
		for key, value in java_vars.items():
			variables.append(f"\n\t@Column(name=\"{key}\")\n")
			variables.append(f"\tprivate {value} {key};\n")
		new_file.writelines(variables)

		# Write Constructurs
		super_constructor_list = [
			f"\n\tpublic {self._table.get_name()}()",
			"{\n",
			"\t\tsuper();\n",
			"\t}\n"
		]
		new_file.writelines(super_constructor_list)

		constructor_list = [
			f"\n\tpublic {self._table.get_name()}",
			"("
		]
		for key, value in java_vars.items():
			constructor_list.append(f"{value} {key}, ")

		constructor_list[-1] = constructor_list[-1][:-2] # Remove comma from last elt

		constructor_list.append("){\n")

		for k in list(java_vars.keys()):
			constructor_list.append(f"\t\tthis.{k} = {k}\n")

		constructor_list.append("\t}\n")

		new_file.writelines(constructor_list)

		# Write Getters/Setters

		getters_setters_list = []
		for key, value in java_vars.items():
			# Getter
			getters_setters_list.append(f"\n\tpublic {value} get_{key}()")
			getters_setters_list.append("{\n")
			getters_setters_list.append(f"\t\treturn {key};\n")
			getters_setters_list.append("\t}\n")

			# Setter
			getters_setters_list.append(f"\n\tpublic {value} set_{key}({value} {key})")
			getters_setters_list.append("{\n")
			getters_setters_list.append(f"\t\tthis.{key} = {key};\n")
			getters_setters_list.append("\t}\n")

		new_file.writelines(getters_setters_list)

		# Write Close Bracket
		new_file.write("\n}")
		new_file.close()

	def write_controller(self, table):
		pass

	def write_repository(self, table):
		pass
