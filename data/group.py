from model.group import Group
import random
import string


def random_string(prefix, maxlen):
    char = string.ascii_letters + string.hexdigits + ' '*15 #+ string.punctuation
    return prefix + "".join([random.choice(char) for i in range(random.randrange(maxlen))])

constant_data = [
    Group(name="Name1", header="Header1", footer="Footer1"),
    Group(name="Name2", header="Header2", footer="Footer2"),
    Group(name="Name3", header="Header3", footer="Footer3")
]

random_data = [
    Group(name=name, header=header, footer=footer)
    for name in ["", random_string("Name_", 10)]
    for header in ["", random_string("Header_", 20)]
    for footer in ["", random_string("Footer_", 10)]
]