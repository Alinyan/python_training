Scenario Outline: Add new contact
    Given a contact list
    Given a contact with <firstname>, <lastname>, <middlename>, <nickname>, <title>, <company>, <address>, <email2>, <email3>, <work_phone>, <home_phone>, <mobile_phone>, <fax>, <homepage>, <address2>, <phone2> and <notes>
    When I add the contact to the list
    Then the new contact list is equal to the old list with the added contact

    Examples:
    | firstname     | lastname    | middlename | nickname | title | company | address | email2  | email3  | work_phone | home_phone | mobile_phone | fax | homepage | address2 | phone2 | notes |
    | firstname123  | lastname111 | gfdgfdgfdf | fdfdsffd | hgghg | ooo     | Spb1237 | 435rtyt | 5423bhp | 2345443    | 56546546   | 935748484    | 555 | hgfghfg  | eritr45  | 575456 | ffgdf |



Scenario: Delete a contact
    Given a non-empty contact list
    Given a random contact from the list
    When I delete the contact from the list
    Then the new contact list is equal to the old contact list without the deleted contact


Scenario: Edit a contact
    Given a non-empty contact list
    Given a random contact from the list
    Given a index of the edited contact
    Given a contact with <firstname>, <lastname>, <middlename>, <nickname>, <title>, <company>, <address>, <email2>, <email3>, <work_phone>, <home_phone>, <mobile_phone>, <fax>, <homepage>, <address2>, <phone2> and <notes>
    When I edit the contact from the list
    Then the new contact list is equal to the old contact list with edited contact

    Examples:
    | firstname   | lastname   | middlename | nickname | title | company | address | email2  | email3  | work_phone | home_phone | mobile_phone | fax | homepage | address2 | phone2 | notes |
    | firyghghhh  | lastnfgfdg | middlename | nickname | title | oao     | Spb5555 | email   | emailg  | 2767677    | 56453545   | 767677686    | 575 | hjkjkjh  | eritr45  | 575456 | ffgdf |

