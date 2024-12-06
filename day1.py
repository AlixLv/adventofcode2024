def main():
    list1, list2 = readFile()
    list_of_distance = compare_list(list1, list2)
    total_distance = sum_of_distance(list_of_distance)
    print("total of distance: ", total_distance)


def readFile():
    left_list = []
    right_list = []
    with open("adventofcode2024/input.txt", "r") as file:
        for line in file:
            values = line.split("   ")
            left_list.append(int(values[0]))
            right_list.append(int(values[1]))
    left_list.sort()
    right_list.sort()        
    return left_list, right_list


def smallest_number(list):
    smaller_element = list[0]

    for element in list:
        if element < smaller_element:
            smaller_element = element 
    
    if len(list) == 2:
        for element in list:
            if list[0] > list[1]:
                return list[1]
            else:
                return list[0]

    return smaller_element


def calcul_distance(num1, num2):
    if num1 > num2:
        distance = num1 - num2
    else: 
        distance = num2 - num1    
    return distance


def remove_smallest_number(number, list):
    list.remove(number)
    return list  
     

def compare_list(list1, list2):
    new_list1 = list1
    new_list2 = list2
    listing_distance = []

    while len(new_list1) >= 1:
        while len(new_list2) >= 1:
            result1 = smallest_number(new_list1)
            result2 = smallest_number(list2)

            if len(new_list1) == 1:
                result1 = new_list1[0]

            if len(new_list2) == 1:
                result2 = new_list2[0]

            new_list1 = remove_smallest_number(result1, new_list1)
            new_list2 = remove_smallest_number(result2, new_list2)
            
            distance = calcul_distance(result1, result2)

            listing_distance.append(distance)


    return listing_distance


def sum_of_distance(list):
    sum = 0
    for element in list:
        sum += element
    return sum

main()


