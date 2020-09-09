import sys
sys.path.insert(0, 'test/')

import ReaderTest as ReaderTest

class Tests():
    def __init__(self, verbose):
        self.verbose = verbose

    def reader_tests(verbose):
        return ReaderTest.run_all_io_tests(verbose)

    def run_all_tests(verbose):

        reader_test_results = reader_tests(verbose)
        return reader_test_results


def main():
    print("\nRunning Test Files Verbose")
    test_runner = Tests(True)
    test_runner.run_all_tests(True)


main()
