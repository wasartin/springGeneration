import sys
sys.path.insert(0, '../model/')
sys.path.insert(1, '../io/')

import Table
import Reader
import Writer

def write_entity_test(verbose):
    relative_file_path = "../../resources/sql/accountSchema.sql"

    file_contents = Reader.open_file(relative_file_path)
    parser = Reader.SQL_Parser(file_contents)
    table_name = parser.parse_table()
    table_attributes = parser.parse_attributes()

    t = Table.Table(table_name, file_contents, table_attributes)

    w = Writer.Entity_Writer(t)

    w.write_entity("some_file")

    return 0

def write_controller_test(verbose):

    return 0

def write_repository_test(verbose):

    return 0

def run_all_writer_tests(verbose):
    num_correct = 0
    num_expected = 3

    num_correct += write_entity_test(verbose)
    num_correct += write_controller_test(verbose)
    num_correct += write_repository_test(verbose)

    return (num_correct == num_expected)


def main():
    v = True

    success = run_all_writer_tests(v)
    if(v):
        print(f"All Writer Tests passed: {success}")

main()
