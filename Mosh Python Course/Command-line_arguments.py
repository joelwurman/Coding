import sys

if len(sys.argv) == 1:
    print ("USAGE: python3 Command-line_arguments.py <password>")
else:
    password = sys.argv[1]
    print('Password', password)