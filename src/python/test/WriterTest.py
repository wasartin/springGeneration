import sys
sys.path.insert(0, '../io/')

import Writer

def write_entity_test(verbose):

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
