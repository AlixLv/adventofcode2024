sample = [[7, 6, 4, 2, 1], [1, 2, 7, 8, 9], [9, 7, 6, 2, 1], [1, 3, 2, 4, 5], [8, 6, 4, 4, 1], [1, 3, 6, 7, 9]]

def main():
    #reports = readFile()
    # nested lists
    #print(reports)
    checkDecrease(sample)

#The levels are either all increasing or all decreasing.
#Any two adjacent levels differ by at least one and at most three.

def readFile():
    report = []
    with open("adventofcode2024/input.txt", "r") as file:
        for line in file:
            line = line.split()
            if line:
                line = [int(i) for i in line]
                report.append(line)      
    return report


def checkDecrease(lists):
    res = True
    for list in lists:
        for i in range(1, len(list)):
            if list[i] >= list[i -1]:
                res = False
                print(f"🐹{list}, {res}")
                #liste pas décroissante, on la passe dans fonction vérifiant si liste est croissante
            else:
                res = True 
                print(f"🐸{list}, {res}")  
                #liste bien décroissante, alors on la passe dans la fonction vérifiant l'espace entre chaque nombre
        return res           
            

main()