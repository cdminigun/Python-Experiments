from optparse import OptionParser
from time import gmtime, strftime

def main():
    usage = "usage: %prog [options] arg"
    parser = OptionParser(usage)
    parser.set_defaults(gmt=True, temp_name="fileIO-Example")
    parser.add_option("-f", "--file", dest="temp_name",
                      help="Name of your output file")
    parser.add_option("-g", "--gmt",
                      action="store_true", dest="gmt",
                      help="Sets the time format for file creation to GMT")
    parser.add_option("-l", "--local",
                      action="store_false", dest="gmt",
                      help="Sets the time format for file creation to local time")
    (options, args) = parser.parse_args()
    if options.gmt:
        filename = strftime("%b-%d-%Y-%H:%M:%S-", gmtime())+ str(options.temp_name)
    else:
        filename = strftime("%b-%d-%Y-%H:%M:%S-") + str(options.temp_name)
    print filename

if __name__ == "__main__":
    main()
