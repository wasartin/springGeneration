import sys
sys.path.insert(0, '../model/')

import Table

def create_table(verbose):
    
    return 0

def name_test(verbose):

    return 0

def schema_test(verbose):

    return 0

def attributes_test(verbose):

    return 0

def string_test(verbose):

    return 0


def run_all_table_tests(verbose):
    num_correct = 0
    num_expected = 5

    num_correct += create_table(verbose)
    num_correct += name_test(verbose)
    num_correct += schema_test(verbose)
    num_correct += attributes_test(verbose)
    num_correct += string_test(verbose)

    return (num_correct == num_expected)

def main():
    v = True

    success = run_all_table_tests(v)
    if(v):
        print(f"All Table Tests passed: {success}")

main()
