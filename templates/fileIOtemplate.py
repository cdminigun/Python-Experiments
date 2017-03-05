import argparse

def process_large_file_with_lines(in_file):
    """ Function to process a large newline seperated file  """
    with open(in_file) as fd:
        for line in iter(fd.readline,''):
            manipulate_input(line)

def process_large_data_file(in_file, n):
    """ Function to process a large data file in increments of n bytes."""
    with open(in_file) as fd:
        for line in fd.read(n):
            manipulate_input(line)


def manipulate_input(input):
    """ User defined processing of lines """
    pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Parse file template")
    parser.add_argument("--l", "--line_file", type=str, help="Large line seperated file.")
    parser.add_argument("--d", "--data_file", type=str, help="Large data file name.")
    parser.add_argument("--n", "--num_of_bytes", type=int, help="Number of bytes for data_file.")
    args = parser.parse_args()
    if args.line_file:
        process_large_file_with_lines(args.line_file)
    elif args.data_file and args.num_of_bytes:
        process_large_data_file(args.data_file, args.num_of_bytes)
