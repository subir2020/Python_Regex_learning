file1 = open("ITMILAN4SA005.txt","r")
Lines = file1.readlines()
interface_statuses = []

x=0

for line in Lines:
    if x == 1:
        if file1.name[0:-4] in line:
            x=0
        else:
            interface_statuses.append(line)

    if "show interfaces status" in line:
        x=1

Duplex_Start = interface_statuses[1].find('Vlan') + 6
Duplex_End = interface_statuses[1].find('Duplex') + 6

Speed_Start = interface_statuses[1].find('Duplex') + 6
Speed_End = interface_statuses[1].find('Speed') + 5


dup = {}
speed = {}

interface_statuses.pop(0)

for line in interface_statuses:

    if 'Duplex' in line[Duplex_Start:Duplex_End].lstrip():
        continue

    if line[Duplex_Start:Duplex_End].lstrip() in dup.keys():
        dup[line[Duplex_Start:Duplex_End].lstrip()] = dup[line[Duplex_Start:Duplex_End].lstrip()] + 1
    else:
        dup[line[Duplex_Start:Duplex_End].lstrip()] = 1

    if line[Speed_Start:Speed_End].lstrip() in speed.keys():
        speed[line[Speed_Start:Speed_End].lstrip()] = speed[line[Speed_Start:Speed_End].lstrip()] + 1
    else:
        speed[line[Speed_Start:Speed_End].lstrip()] = 1

print(dup)
print(speed)





