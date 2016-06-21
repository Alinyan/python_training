from model.group import Group
import random
import string
import os.path
import json
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

number = 5
file = "data/groups.json"

for o, a in opts:
    if o == "-n":
        number = int(a)
    elif o == "-f":
        file = a

def random_string(prefix, maxlen):
    char = string.ascii_letters + string.hexdigits + ' '*15 #+ string.punctuation
    return prefix + "".join([random.choice(char) for i in range(random.randrange(maxlen))])

random_data = [
    Group(name=random_string("name", 20), header=random_string("header", 20), footer=random_string("footer", 20))
    for i in range(number)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", file)

with open(file, "w") as f:
    f.write(json.dumps(random_data, default=lambda x: x.__dict__, indent=2))