import pprint 

pp = pprint.PrettyPrinter(width=150) 


def findProfession(level, pos):
    if level == 1:
        return 'Engineer'

    print(findProfession(level-1, (pos+1)//2) + str(level-1) + str((pos+1)//2))
    if findProfession(level-1, (pos+1)//2) == 'Engineer':
        if (pos % 2) == 0:
            return 'Doctor'
        else:
            return 'Engineer'
    else:
        if (pos % 2) == 0:
            return 'Engineer'
        else:
            return 'Doctor'

pp.pprint(findProfession(4,8))