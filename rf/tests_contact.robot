*** Settings ***
Library    rf.Addressbook
Library    Collections
Suite Setup   Init Fixtures
Suite Teardown    Destroy Fixtures

*** Test Cases ***
Add new contact
    ${old_list}=   Get Contact List
    ${contact}=  New Contact    firstname=name123   lastname=lastname2345  address=SPBdfgtr  email2=rtretr  email3=rtrjhe \
    ...     home_phone=343423  mobile_phone=454543   work_phone=5645645   phone2=7675675
    Create Contact   ${contact}
    ${new_list}=   Get Contact List
    Append To List    ${old_list}    ${contact}
    Contact Lists Should Be Equal    ${new_list}    ${old_list}

Delete contact
    ${old_list}=   Get Contact List
    ${len}=    Get Length    ${old_list}
    ${index}=    Evaluate   random.randrange(${len})    random
    ${contact}=   Get From List   ${old_list}   ${index}
    Delete Contact   ${contact}
    ${new_list}=   Get Contact List
    Remove Values From List    ${old_list}    ${contact}
    Contact Lists Should Be Equal    ${new_list}    ${old_list}

Edit contact
    ${old_list}=   Get Contact List
    ${len}=    Get Length    ${old_list}
    ${index}=    Evaluate   random.randrange(${len})    random
    ${random_contact}=   Get From List   ${old_list}   ${index}
    ${edit_contact}=  New Contact    firstname=name7657   lastname=lastnamehjgb address=Sghgf  email2=rkkjlkj  email3=rsadsad\
    ...   home_phone=7878768  mobile_phone=213123  work_phone=65465465   phone2=78768768
    Edit Contact    ${random_contact}    ${edit_contact}
    ${new_list}=   Get Contact List
    Replace Values List    ${old_list}   ${index}   ${edit_contact}
    Contact Lists Should Be Equal    ${new_list}    ${old_list}



