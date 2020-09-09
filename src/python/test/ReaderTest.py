import sys
sys.path.insert(0, '../io/')

import Reader

# Return 1 on success
def open_file_test(verbose):
    relative_file_path = "../../resources/sql/accountSchema.sql"
    file_contents = Reader.open_file(relative_file_path)
    if( len(file_contents) != 0 ):
        return 1
    return 0

def parse_table_test(verbose):
    relative_file_path = "../../resources/sql/accountSchema.sql"
    file_contents = Reader.open_file(relative_file_path)

    table_name = Reader.parse_table(file_contents)

    if(table_name == "account"):
    	return 1
    return 0

def parse_attributes_test(verbose):
    relative_file_path = "../../resources/sql/accountSchema.sql"
    file_contents = Reader.open_file(relative_file_path)

    table_name = Reader.parse_attributes(file_contents)

    return 0

def run_all_io_tests(verbose):
    num_correct = 0
    num_expected = 3

    num_correct += open_file_test(verbose)
    num_correct += parse_table_test(verbose)
    num_correct += parse_attributes_test(verbose)

    return (num_correct == num_expected)


def main():
    v = True

    success = run_all_io_tests(v)
    if(v):
        print(f"All Tests passed: {success}")


main()
