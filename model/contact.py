from sys import maxsize

class Contact:

    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, title=None, company=None, address1=None, home_phone=None,
                 mobile_phone=None, work_phone=None, fax=None, email=None, email2=None, email3=None, homepage=None,
                 address2=None, phone2=None, notes=None, id=None, all_emails=None, all_phones=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address1 = address1
        self.home_phone = home_phone
        self.mobile_phone = mobile_phone
        self.work_phone = work_phone
        self.fax = fax
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.address2 = address2
        self.phone2 = phone2
        self.notes = notes
        self.id = id
        self.all_emails = all_emails
        self.all_phones = all_phones

    def __repr__(self):
        return "%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s" \
               % (self.id, self.lastname, self.firstname, self.middlename, self.nickname,
                self.title, self.company, self.address1, self.home_phone,
                self.mobile_phone, self.work_phone, self.fax, self.email, self.email2, self.email3,
                self.homepage, self.address2, self.phone2, self.notes, self.all_phones, self.all_emails)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) \
               and (self.lastname == other.lastname or self.lastname is None or other.lastname is None) \
               and (self.firstname == other.firstname or self.firstname is None or other.firstname is None) \
               and (self.address1 == other.address1 or self.address1 is None or other.address1 is None) \
               and (self.middlename == other.middlename or self.middlename is None or other.middlename is None) \
               and (self.nickname == other.nickname or self.nickname is None or other.nickname is None) \
               and (self.title == other.title or self.title is None or other.title is None)\
               and (self.company == other.company or self.company is None or other.company is None)\
               and (self.home_phone == other.home_phone or self.home_phone is None or other.home_phone is None) \
               and (self.mobile_phone == other.mobile_phone or self.mobile_phone is None or other.mobile_phone is None)\
               and (self.work_phone == other.work_phone or self.work_phone is None or other.work_phone is None) \
               and (self.fax == other.fax or self.fax is None or other.fax is None) \
               and (self.email == other.email or self.email is None or other.email is None)\
               and (self.email2 == other.email2 or self.email2 is None or other.email2 is None)\
               and (self.email3 == other.email3 or self.email3 is None or other.email3 is None) \
               and (self.homepage == other.homepage or self.homepage is None or other.homepage is None)\
               and (self.address2 == other.address2 or self.address2 is None or other.address2 is None) \
               and (self.phone2 == other.phone2 or self.phone2 is None or other.phone2 is None) \
               and (self.notes == other.notes or self.notes is None or other.notes is None)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
