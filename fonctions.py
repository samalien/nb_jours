#----------------------------------------------------------------#
#                verifie si une année est bissextile             #
#----------------------------------------------------------------#
def isLeap(year):
    if year % 4 == 0 and year % 100 !=0:
        return True
    elif year % 400 == 0:
        return True
    return False

#----------------------------------------------------------------#
#                le nombre de jour d'un mois donné               #
#----------------------------------------------------------------#
def daysInMonth(month,year):
    days=[31,28,31,30,31,30,31,31,30,31,30,31]
    if isLeap(year):
        days[1]=29
    return days[month -1]

#----------------------------------------------------------------#
#                verifie si une date est valide                  #
#----------------------------------------------------------------#
def validDate(day,month,year):
    if day in range(1,daysInMonth(month,year)+1):
        return True
    return False

#----------------------------------------------------------------#
#    verifie si une date 1 est avant une date 2 données          #
#----------------------------------------------------------------#
def dateIsBefore(day1,month1,year1,day2,month2,year2):
    if year1 < year2:
        return True
    elif year1 == year2:
        if month1 < month2:
            return True
        elif month1 == month2:
            if day1 < day2:
                return True
    return False

#----------------------------------------------------------------#
#    retourne la date du lendemain a partir d'une date donnée    #
#----------------------------------------------------------------#
def nextDay(day,month,year):
    if day in range(1,daysInMonth(month,year)):
        return day+1,month,year
    elif month<12:
        return 1,month+1,year
    elif month == 12:
        return 1,1,year+1

#----------------------------------------------------------------#
#                compter le nombre de jour                       #
#----------------------------------------------------------------#
def count(day1,month1,year1,day2,month2,year2):
    nb=0
    while  day1 != day2 or month1 != month2 or year1 != year2:
        nb=nb+1
        day1,month1,year1=nextDay(day1,month1,year1)
    return nb

