def fares(prise, student=False, senior=False):
    if student or senior:
        print 'hel'
        return 'halv'
    else:
        if prise <20 or prise >65:
            return 'halv'
        else:
            return 'hel'




# test cases
print 'barn 10',fares(20)
print 'pensioner 65',fares(20)
print 'studen 25',fares(29,student=True)
print 'vuxen 20',fares(40)






