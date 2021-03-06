#user story 38 list upcoming birthday
import unittest
from prettytable import PrettyTable
from datetime import datetime, timedelta

def get_is_alive(indi):
    #Don't need to count individual's birthday if this individual is already dead.
    if "DEAT" in indi:
        death = datetime.strptime(indi["DEAT"], '%d%b%Y')
        return False
    else:
        return True


def get_birth_date(indi):
    #check BIRT tag in individual's data
    if "BIRT" in indi:
        birth = datetime.strptime(indi["BIRT"], '%d%b%Y')
        return birth
    else:
        return 0
    
def us38(indi):
        """"US38
        Prints birthdays within the next 30 days
        """
        people = indi
        table = PrettyTable(["ID", "Name", "Birthday"])

        result = False

        for person_id in people:
            individual = indi[person_id]
            individual = people[person_id] 
            today = datetime.today()
            individual_birthday = get_birth_date(individual)
            if individual_birthday is not 0 and get_is_alive(indi):
                individual_current_birthday = datetime(today.year, individual_birthday.month, individual_birthday.day)
                if 0 <= (abs(individual_current_birthday - today)).days <= 30:
                    table.add_row([individual["id"], individual["name"], individual_birthday])
                    result = True
        print('US38 Individuals whose birthday within next 30 days:\n',table)
        return result

ind = {'I01': {'id': 'I01', 'name': 'Joe /Smith/', 'BIRT': '15MAY1960', 'sex': 'M', 'family': 'F23', 'DEAT': '31DEC2013'},
 'I07': {'id': 'I07', 'name': 'Jennifer /Smith/', 'BIRT': '23MAY1960', 'sex': 'F', 'family': 'F23'},
 'I19': {'id': 'I19', 'name': 'Dick /Smith/', 'BIRT': '13MAY1981', 'sex': 'M', 'family': 'F23'},
  'I26': {'id': 'I26', 'name': 'Jane /Smith/', 'BIRT': '13MAY1982', 'sex': 'F', 'family': 'F23'},
  'I30': {'id': 'I30', 'name': 'Mary /Test/', 'BIRT': '13FEB1987', 'sex': 'F', 'family': 'F23'},
}

class MyTest(unittest.TestCase):
    def test(self): 
        self.assertTrue(us38(ind))
         
if __name__ == '__main__':
    unittest.main()