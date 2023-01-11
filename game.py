#this code is messy af and written in a hurry
import os
from copy import deepcopy

def mapParser(fileName):
    b1 = [-1,-1]
    b2 = [-1,-1]
    fin = (-1,-1)
    kaart = []
    with open(fileName,"r") as file:
        lines = file.readlines()
        for line in lines:
            if len(line) != 0: kaart.append([i for i in line.replace("b","x").replace("\n"," ")])
            rida = 0
            for i in line:
                if i == "b":
                    if b1[0] == -1:
                        b1 = [len(kaart)-1,rida]
                    else:
                        b2 = [len(kaart)-1,rida]
                elif i == "o":
                    fin = [len(kaart)-1,rida]
                rida+=1
    if b2 == [-1,-1]: #kui plokk seisab püsti
        b2=deepcopy(b1)
    return kaart,[b1,b2],fin

def printMap(kaart,plokk):
    k = list(deepcopy(kaart))
    k[plokk[0][0]][plokk[0][1]] = "■"
    k[plokk[1][0]][plokk[1][1]] = "■"
    for i in k: print("".join(i))

#0 - up, 1 - down, 2 - left, 3 - right
def move(iplokk, suund): #I stole my own code, who would've thought
    if iplokk[0] == iplokk[1]:
        if suund == "N":
            iplokk[0][0] -= 2
            iplokk[1][0] -= 1
        elif suund == "S":
            iplokk[0][0] += 1
            iplokk[1][0] += 2
        elif suund == "E":
            iplokk[0][1] += 1
            iplokk[1][1] += 2
        elif suund == "W":
            iplokk[0][1] -= 2
            iplokk[1][1] -= 1
    elif iplokk[0][1] != iplokk[1][1]: #orientation east-west
        if suund == "N":
            iplokk[0][0] -= 1
            iplokk[1][0] -= 1
        elif suund == "S":
            iplokk[0][0] += 1
            iplokk[1][0] += 1
        elif suund == "E":
            iplokk[0][1] += 2
            iplokk[1] = deepcopy(iplokk[0])
        elif suund == "W":
            iplokk[0][1] -= 1
            iplokk[1] = deepcopy(iplokk[0])
    elif iplokk[0][0] != iplokk[1][0]: #orientation north-south
        if suund == "N":
            iplokk[0][0] -= 1
            iplokk[1] = deepcopy(iplokk[0])
        elif suund == "S":
            iplokk[0][0] += 2
            iplokk[1] = deepcopy(iplokk[0])
        elif suund == "E":
            iplokk[0][1] += 1
            iplokk[1][1] += 1
        elif suund == "W":
            iplokk[0][1] -= 1
            iplokk[1][1] -= 1
    if kaart[iplokk[0][0]][iplokk[0][1]] == " ":
        return [[-1,-1],[-1,-1]]#dead
    if kaart[iplokk[1][0]][iplokk[1][1]] == " ":
        return [[-1,-1],[-1,-1]]#dead
    return iplokk

kaart, plokk, auk = mapParser("maps/Map1") #Laeme esimese mapi
mapCounter = 1

while True:
    printMap(kaart,plokk)
    vastus = input("Mida teed järgmiseks? ").lower()
    if vastus == "lahku":
        exit()
    elif vastus == "üles":
        plokk = move(plokk,"N")
    elif vastus == "alla":
        plokk = move(plokk,"S")
    elif vastus == "paremale":
        plokk = move(plokk,"E")
    elif vastus == "vasakule":
        plokk = move(plokk,"W")
    if plokk[0][0] == -1 or plokk[0][1] == -1 or plokk[1][0] == -1 or plokk[1][1] == -1: #death condition
        print("--------\nSa surid\n--------")
        kaart, plokk, auk = mapParser("maps/Map"+str(mapCounter))
    if plokk[0] == plokk[1] == auk: #win condition
        print("\n\n\n")
        if mapCounter!=len(os.listdir("maps")):
            mapCounter+=1
            kaart, plokk, auk = mapParser("maps/Map"+str(mapCounter))
        else:
            print("----------\nSa võitsid\n----------")
            input("(Vajuta ENTERIT, et lahkuda)")
            exit()
