import sys
sys.path.insert(0, '../model/')
sys.path.insert(1, '../io/')

import Table
import Reader

"""
    Ensuring that the name of the table is correctly extracted.
"""
def name_test(verbose):
    relative_file_path = "../../resources/sql/accountSchema.sql"

    file_contents = Reader.open_file(relative_file_path)
    parser = Reader.SQL_Parser(file_contents)
    table_name = parser.parse_table()
    table_attributes = parser.parse_attributes()

    t = Table.Table(table_name, file_contents, table_attributes)

    if(t.get_name() == 'account'):
        return 1
    return 0

def attributes_test(verbose):
    relative_file_path = "../../resources/sql/accountSchema.sql"

    file_contents = Reader.open_file(relative_file_path)
    parser = Reader.SQL_Parser(file_contents)
    table_name = parser.parse_table()
    table_attributes = parser.parse_attributes()

    t = Table.Table(table_name, file_contents, table_attributes)

    expected_attribute_dict = {'account_email': 'VARCHAR', 'account_id': 'VARCHAR', 'account_type': 'CHAR'}

    count = 0

    if len(t.get_attributes()) != len(expected_attribute_dict):
        return 0
    for key in expected_attribute_dict:
        if t.get_attributes()[key] == expected_attribute_dict[key]:
            count+= 1
    if count == len(expected_attribute_dict):
        return 1

    return 0

def run_all_table_tests(verbose):
    num_correct = 0
    num_expected = 2

    num_correct += name_test(verbose)
    num_correct += attributes_test(verbose)

    if(verbose):
        print(f"Passed:  {num_correct} / {num_expected}")
    return (num_correct == num_expected)

def main():
    v = True

    success = run_all_table_tests(v)
    if(v):
        print(f"All Table Tests passed: {success}")

main()
