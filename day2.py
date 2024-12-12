sample = [[7, 6, 4, 2, 1], [1, 2, 7, 8, 9], [9, 7, 6, 2, 1], [1, 3, 2, 4, 5], [8, 6, 4, 4, 1], [1, 3, 6, 7, 9]]
counter = 0

def main():
    reports = readFile()
    newCounter = checkDecrease(sample, counter)
    print("NEW COUNTER: ", newCounter)


def readFile():
    report = []
    with open("../adventofcode2024/input.txt", "r") as file:
        for line in file:
            line = line.split()
            if line:
                line = [int(i) for i in line]
                report.append(line)      
    return report


def checkDecrease(lists, count):
    res = "safe"
    for list in lists:
        for i in range(1, len(list)):
            if list[i] >= list[i -1]:
                res = "unsafe"
                increaseCounter = checkIncrease(list, counter)
                print(f"🌴 {increaseCounter}")
                
                
        if res == "safe":        
            newCounter = checkDecreaseAdjacent(list, counter) 
            print(f"🌿 {newCounter}")   
            count += newCounter
    
    count += increaseCounter
    return count         


def checkIncrease(list, count):
    res = "safe"
    for i in range(1, len(list)):
        if list[i] <= list[i -1]:
            res = "unsafe"

    if res == "safe":
        print(f"🐚 safe : {list}")
        newCounter = checkIncreaseAdjacent(list, counter) 
        print(f"🍄‍🟫 {newCounter}")  
        count += newCounter
    
    return count     
       
            
def checkDecreaseAdjacent(list, count):
    res = "safe"
    for i in range(1, len(list)):
        if list[i -1] - list[i] < 1 or list[i -1] - list[i] > 3:
            res = "unsafe"
         
    if res == "safe": 
        print("🍏safe: ", list)        
        count += 1
        
    print(f"🐓 {count}")
    return count                         


def checkIncreaseAdjacent(list, count):
    res = "safe"
    for i in range(1, len(list)):
        if list[i] - list[i -1] < 1 or list[i] - list[i -1] > 3:
            res = "unsafe"
            
    if res == "safe": 
        print("🍓safe: ", list)       
        count += 1
        
    print(f"🌻 {count}")
    return count    
             

main()