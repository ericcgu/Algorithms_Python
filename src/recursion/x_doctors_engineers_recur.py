import pprint 

pp = pprint.PrettyPrinter(width=150) 


def findProfession(level, pos):
    if level == 1:
        return 'Engineer'
    if findProfession(level-1, (pos+1)//2) == 'Engineer':
        if pos % 2 == 0:
            return 'Engineer'
        else:
            return 'Doctor'
    else:
        if pos % 2 == 0:
            return 'Doctor'
        else:
            return 'Engineer'

pp.pprint(findProfession(4,2)) #Doctor