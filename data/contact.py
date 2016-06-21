from model.contact import Contact
import random
import string


def random_string(prefix, maxlen):
    char = string.ascii_letters + string.hexdigits + ' '*10 #+ string.punctuation
    return prefix + "".join([random.choice(char) for i in range(random.randrange(maxlen))])

constant_data = [
    Contact(firstname="Olga", middlename="Petrovna", lastname="Petrova", nickname="Star", title="economist",
            company="OAO Dream-House", address1="Russia, Lenina 5", home_phone="7894563", mobile_phone="9221547586",
            work_phone="6123457", fax="6123458", email2="olga-star@oao-dream-house.com", email3="olga@dh.com",
            homepage="www.dream-house.com", address2="Russia, Spb, Lenina 17", phone2="145", notes="Likes to read books"),
    Contact(firstname="firstname", middlename="middlename", lastname="lastname", nickname="Star", title="blablabla",
            company="OAO Dream-House", address1="spb", home_phone="7894563", mobile_phone="9221547586",
            work_phone="6123457", fax="54544545", email2="olga-star@oao-dream-house.com", email3="olga@dh.com",
            homepage="www.dream-house.com", address2="Russia, Spb, Lenina 17", phone2="23545655",
            notes="blablabla"),
    Contact(firstname="Ekaterina", middlename="Petrovna", lastname="Ivanova", nickname="CosmoStar", title="lololololol",
            company="OAO Dream-House", address1="Russia", home_phone="7894563", mobile_phone="9221547586",
            work_phone="6123457", fax="645664565", email2="olga-star@oao-dream-house.com", email3="olga@dh.com",
            homepage="www.dream-house.com", address2="Russia, Spb, Lenina 17", phone2="5252527",
            notes="lololololololo")
]

random_data = [Contact(firstname=fn, address1=a1, work_phone=wp, email2=e2)
            for fn in ["", random_string("Firstname", 20)]
            for a1 in ["", random_string("address1", 50)]
            for wp in ["", random_string("workphone", 15)]
            for e2 in ["", random_string("email2", 30)]
]