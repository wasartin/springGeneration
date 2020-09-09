import sys # For commandline args
import getopt # For parsing commandline args
import test/io/Test as Test

def flag_handling(argv):
    try:
        opts, args = getopt.getopt(argv)
    except getopt.GetoptError:
        print(output_help)
        sys.exit(2)


def main(argv):
    if( len(sys.argv) != 0 ):
        flag_handling(sys.argv)
