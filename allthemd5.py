import os
import argparse
import md5

verbose = False

def find_folders(folder):
    try:
        pass_through_flag = 0
        a = dict()
        while True:
            for dirname, dirnames, filenames in os.walk(folder):
                for filename in filenames:
                    hash_files( filename, os.path.join(dirname, filename), pass_through_flag, a)
            pass_through_flag += 1
    except OSError as e:
        print "An OSError occured. \nTraceback: \n {0}".format(e)
    except:
        print "An unknown error occured in find_folders"

def hash_files(filename, full_path, pass_through_flag, a):
    try:
        m = md5.new()
        f = open(full_path, "r")
        r = open("hex", 'w')
        for line in f:
            m.update(line)
            #r.write("{0} : {1}\n".format(full_path, m.hexdigest()))
        new_md5 = m.hexdigest()
        if pass_through_flag == 0 and verbose:
            print "Added {0} with md5 of {1}".format(full_path, new_md5)
        if full_path in a and pass_through_flag > 1:
            if a[full_path] == new_md5:
                pass
            else:
                print "[*] : {0} has changed from an md5 of {1} to {2}".format(filename, a[full_path], new_md5)
                a[full_path] = new_md5
        elif pass_through_flag > 1:
            print "[*] : New File {0} added with an md5sum of {1}".format(filename, a[full_path])
            a[full_path] = new_md5
        elif not filename in a and pass_through_flag == 0:
            a[full_path] = new_md5
    except OSError as e:
        print "An unexpected OSError has occured in hash_files. \nTraceback: \n{0}".format(e)
    except IOError as e:
        print "An unexpected IOError has occured in hash_files. \nTraceback: \n{0}"
    except:
        print "An unknown error occured."

def pwn_tripwire(folder, data, full_file_path):
    try: 
        a = dict()
        for dirname, dirnames, filenames in os.walk(folder):
            for filename in filenames:
                f = open(os.path.join(dirname, filename), "a")
                f.write("\n ")
    except OSError as e:
        print "An unexpected OSError occured in pwn_tripwire. \nTraceback: \n{0}".format(e)
    except IOError as e:
        print "An unexpected IOError occured in pwn_tripwire. \nTraceback: \n{0}".format(e)
    except:
        print "An unknown error occured in pwn_tripwire."


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Tripwire in python.")
    parser.add_argument("-f", "--folder", type=str, help="Absolute path to the folder.")
    parser.add_argument("-a", "--all_files", action="store_true", help="Md5sum of all directories")
    parser.add_argument("-v", "--verbose", action="store_true", help="Print debugging information." )
    parser.add_argument("-p", "--pwn", action="store_true", help="Pwn tripwire and write data to a file. Note -d, -n and -f are needed with -p")
    parser.add_argument("-d", "--data", type=str, help="Data to be written in pwn_tripwire")
    parser.add_argument("-n","--full_file_path", type=str, help="Path of file to be written.")
    args = parser.parse_args()
    if args.verbose:
        verbose = True
    if args.all_files:
        find_folders("/")
    elif args.folder:
        find_folders(args.folder)
    elif args.pwn:
        if args.folder and args.data and args.full_file_path:
            pwn_tripwire(args.folder, args.data, args.full_file_path)
        else:
            parser.print_help()
    else:
       parser.print_help()
