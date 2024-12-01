list1 = [3,4,2,1,3,3]
list2 = [4,3,5,3,9,3]

#TO DO : revoir ordre exécution fonction, quand il n'y a plus que 2 éléments dans chaque list
#distance pas calculée pour quand 2 éléments par liste !!

def main():
    list_of_distance = compare_list(list1, list2)
    total_distance = sum_of_distance(list_of_distance)
    print("total of distance: ", total_distance)



def smallest_number(list):
    smaller_element = list[0]

    for element in list:
        if element < smaller_element:
            smaller_element = element 
    
    if len(list) == 2:
        print("DANS LE IF")
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
    #appliquer sur chaque élément de list1 smallest_number
    #renvoie un résultat
    new_list1 = list1
    new_list2 = list2
    listing_distance = []

    while len(new_list1) > 1:
        while len(new_list2) >= 1:
            result1 = smallest_number(new_list1)
            print("smaller element n-1: ", result1)
            result2 = smallest_number(list2)
            print("smaller element n-2: ", result2)
            new_list1 = remove_smallest_number(result1, new_list1)
            print("new list 1: ", new_list1) 
            new_list2 = remove_smallest_number(result2, new_list2)
            print("new list 2: ", new_list2) 

            if len(new_list1) == 1:
                result1 = new_list1[0]
                print("smaller element n-1: ", result1)

            if len(new_list2) == 1:
                result2 = new_list2[0]
                print("smaller element n-2: ", result2)
            
    #appliquer calcul_distance pour chaque couple de résultat
            distance = calcul_distance(result1, result2)
            print("distance: ", distance)

    #stocker ces résultats dans une nouvelle liste
            listing_distance.append(distance)
            print("list of distance: ", listing_distance)

    return listing_distance


def sum_of_distance(list):
    sum = 0
    for element in list:
        sum += element
    return sum

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
