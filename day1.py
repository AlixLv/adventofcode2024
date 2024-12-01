list1 = [3,4,2,1,3,3]
list2 = [4,3,5,3,9,3]
list_of_distance = []

def main():
    result1 = smallest_number(list1)
    print("smaller element n-1: ", result1)
    result2 = smallest_number(list2)
    print("smaller element n-2: ", result2)
    distance = calcul_distance(result1, result2)
    print("distance: ", distance)


def smallest_number(list):
    smaller_element = list[0]
    print("smaller element: " , smaller_element)
    for element in list:
        if element < smaller_element:
            smaller_element = element
            print("new smaller element: ", smaller_element)      
    return smaller_element


def calcul_distance(num1, num2):
    if num1 > num2:
        distance = num1 - num2
    else: 
        distance = num2 - num1    
    return distance

def remove_smallest_number(number, list):
    for element in list:
        if element == number:
            list.remove(number)
    print("list: ", list) 
    return list  
     


main()


# TO DO :

# In the example list above, the pairs and distances would be as follows:

# The smallest number in the left list is 1, and the smallest number in the right list is 3. The distance between them is 2.
# The second-smallest number in the left list is 2, and the second-smallest number in the right list is another 3. The distance between them is 1.
# The third-smallest number in both lists is 3, so the distance between them is 0.
# The next numbers to pair up are 3 and 4, a distance of 1.
# The fifth-smallest numbers in each list are 3 and 5, a distance of 2.
# Finally, the largest number in the left list is 4, while the largest number in the right list is 9; these are a distance 5 apart.
# To find the total distance between the left list and the right list, add up the distances between all of the pairs you found. 
# In the example above, this is 2 + 1 + 0 + 1 + 2 + 5, a total distance of 11!

# appliquer sur chaque élément de la liste la fonction smallest
# comparer le résultat à l'aide de calculdistance
# comparer ces deux plus petits éléments pour trouver la distance entre eux deux