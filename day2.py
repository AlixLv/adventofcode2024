sample = [[7, 6, 4, 2, 1], [1, 2, 7, 8, 9], [9, 7, 6, 2, 1], [1, 3, 2, 4, 5], [8, 6, 4, 4, 1], [1, 3, 6, 7, 9]]


def main():
    reports = readFile()
    counter = 0
    for list in reports:
        print(list)
        result_decrease = checkDecrease(list)
        if result_decrease == "safe":
                result_decrease_adjacent = checkDecreaseAdjacent(list) 
                print(f"🌺 {result_decrease_adjacent}")
                if result_decrease_adjacent == "safe":
                    counter += 1            
        else:
            result_increase = checkIncrease(list)
            if result_increase == "safe":
                result_increase_adjacent = checkIncreaseAdjacent(list)
                print(f"💐 {result_increase_adjacent}")
                if result_increase_adjacent == "safe":
                    counter +=1
    print(f"🌕 {counter}")                


def readFile():
    report = []
    with open("../adventofcode2024/input.txt", "r") as file:
        for line in file:
            line = line.split()
            if line:
                line = [int(i) for i in line]
                report.append(line)      
    return report
    

def checkDecrease(list):
    res = "safe"
    for i in range(1, len(list)):
        if list[i] >= list[i -1]:
            print(list[i] >= list[i -1])
            res = "unsafe"
            
        if res == "safe":   
            print(f"🌹 safe")    
    
    return res        


def checkIncrease(list):
    res = "safe"
    for i in range(1, len(list)):
        if list[i] <= list[i -1]:
            res = "unsafe"

    if res == "safe":
        print(f"🐚 safe : {list}")
      
    return res     
       
            
def checkDecreaseAdjacent(list):
    res = "safe"
    for i in range(1, len(list)):
        if list[i -1] - list[i] < 1 or list[i -1] - list[i] > 3:
            res = "unsafe"
         
    if res == "safe": 
        print("🍏safe: ", list)        

    return res                      


def checkIncreaseAdjacent(list):
    res = "safe"
    for i in range(1, len(list)):
        if list[i] - list[i -1] < 1 or list[i] - list[i -1] > 3:
            res = "unsafe"
            
    if res == "safe": 
        print(f"🐪 safe")

    return res  
             

main()