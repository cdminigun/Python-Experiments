"""
usage: allthemd5.py [-h] [-f FOLDER] [-a] [-v] [-p] [-d DATA]
                    [-n FULL_FILE_PATH]

Tripwire in python.

optional arguments:
  -h, --help            show this help message and exit
  -f FOLDER, --folder FOLDER
                        Absolute path to the folder.
  -a, --all_files       Md5sum of all directories
  -v, --verbose         Print debugging information.
  -p, --pwn             Pwn tripwire and write data to a file. Note -d, -n and
                        -f are needed with -p
  -d DATA, --data DATA  Data to be written in pwn_tripwire
  -n FULL_FILE_PATH, --full_file_path FULL_FILE_PATH
                        Path of file to be written.
"""
import os
import argparse
import md5

verbose = False

def find_folders(folder):
    """
    Finds all subfolders and files and hashes them itteratively like tripwire.
    Args:
        folder (str) : The name or path of a folder to hash
    """
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
    """
    Continiously hashes files within any subdirectory of a specified folder.
    Args:
        filename (str) : The name of path of a file.
        full_path (str) : The full folder path
        pas_through_flag (bool) : Flag for whether or not to pass through
    """
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

def pwn_tripwire(folder):
    """
    Attempts to write data to all files within a folder path.
    Args:
        folder (str) : A name or path of a folder
    """
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
    args = parser.parse_args()
    if args.verbose:
        verbose = True
    if args.all_files:
        find_folders("/")
    elif args.folder:
        find_folders(args.folder)
    elif args.pwn:
        if args.folder:
            pwn_tripwire(args.folder)
        else:
            parser.print_help()
    else:
        parser.print_help()
