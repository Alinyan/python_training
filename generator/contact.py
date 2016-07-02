from model.contact import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

number = 5
file = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        number = int(a)
    elif o == "-f":
        file = a

def random_string(prefix, maxlen):
    char = string.ascii_letters + string.hexdigits + ' '*5 #+ string.punctuation
    return prefix + "".join([random.choice(char) for i in range(random.randrange(maxlen))])

random_data = [
    Contact(firstname=random_string("firstname", 20), middlename=random_string("middlename", 20), lastname=random_string("lastname", 20),
            nickname=random_string("Star", 20), title=random_string("blablabla", 20), company=random_string("OAO Dream-House", 30),
            address1=random_string("spb", 20), home_phone=random_string("7894563", 20), mobile_phone=random_string("9221547586", 20),
            work_phone=random_string("6123457", 20), fax=random_string("54544545", 20), email2=random_string("olga-star@oao-dream-house.com", 20),
            email3=random_string("olga@dh.com", 20), homepage=random_string("www.dream-house.com", 20), address2=random_string("Russia, Spb, Lenina 17", 20),
            phone2=random_string("23545655", 20), notes=random_string("blablabla", 20))
    for i in range(number)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", file)

with open(file, "w") as f:
    jsonpickle.set_encoder_options("json", indent=2)
    f.write(jsonpickle.encode(random_data))
