#author zyzMarshall 
from datetime import datetime

def birth_before_parents_death(childname,childID,childbirthday,parentsdeathdate,death_bool):
    """The birth of a child should within 9 month after the death of their father(if the death
    date exist.),and can't born after their mother's death"""
    if (datetime.strptime(childbirthday,'%d%b%Y'))>(datetime.strptime(parentsdeathdate,'%d%b%Y')) and death_bool == False:
        birthdate = datetime.strptime(childbirthday,'%d%b%Y')
        parentsdeath = datetime.strptime(parentsdeathdate,'%d%b%Y')
        interval = ((birthdate - parentsdeath).days/365)*12   #timedelta between child birth and parents death
        if interval>9:
            error = "ERROR Us09: Birthday of child %s%s is longer than 9 months after father's death\n"%(childID,childname)
            print(error)
            return error
    elif ((datetime.strptime(childbirthday,'%d%b%Y'))>(datetime.strptime(parentsdeathdate,'%d%b%Y'))):
        error ="ERROR Us09: Birthday of child %s %s is after their mother's death.\n"%(childID,childname)
        print(error)
        return error
        


birth_before_parents_death("Ralph /Doe/", "I01", "20JUN1993", "20JUL1985",True)
