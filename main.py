#!/usr/bin/python

def creationDictionnaire(nbIntersections,T,linesUtil):
    dic={}
    interCourante =  0
    while (interCourante <nbIntersections):
        dic[interCourante]={}
        interCourante = interCourante +1 
        
    for line in linesUtil:
        line = line.split(' ')
        dic[int(line[0])][int(line[1])]=[(int(line[4]),int(line[3])),0]
        if (line[3] == '2'):
            dic[int(line[1])][int(line[0])]=[(int(line[4]),int(line[3])),0]

    return dic 
    
file = open("paris_54000.txt","r")

lines = file.readlines()

enTete = lines[0:1]
chaine = str(enTete[0])
parsee = chaine.split(' ')

nbIntersections=int(parsee[0])
nbRues=int(parsee[1])
T=int(parsee[2])
nbVehicules=int(parsee[3])
intersectionDepart=int(parsee[4])

linesUtil=lines[1+nbIntersections+1:]

print nbIntersections
print nbRues
print T
print nbVehicules
print intersectionDepart

dic = creationDictionnaire(nbIntersections,T,linesUtil)

voitureCourante=0
while (voitureCourante < nbVehicules):
    voitureCourante = voitureCourante + 1
print "fin !"
