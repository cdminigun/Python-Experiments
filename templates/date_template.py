from time import gmtime, strftime


def create_file_by_date():
    file_name = strftime("%b-%d-%Y-%H:%M:%S", gmtime()) + "-temp_name"
    print file_name

if __name__ == "__main__":
    create_file_by_date()
