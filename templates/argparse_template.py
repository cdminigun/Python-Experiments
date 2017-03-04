import argparse



def funca():
    pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Template")
    parser.add_argument("-t", "--temp", type=str, help="test")
    #more arguments
    args = parser.parse_args()
    if args.temp:
        funca()
