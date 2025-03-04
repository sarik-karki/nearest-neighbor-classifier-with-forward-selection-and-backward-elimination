import numpy as np

# On the ith level of the search tree
#--considering adding the -- feature
#....
#....

#On the level i, I added feature 4 to current set ( the best feature)

#On the i + 1 level of the search tree, with current set
#--Considering adding the 1 feature
#(Consider all other feature expect the one that's not on the current set)


#On the level i+1, I added {best feature} to the current set ...

#MATLAB CODE

"""
function accuracy = leave_one_out_cross_validation(data, current_set, feature_to_add)
    accuracy = rand;
end

"""

def leave_one_out_cross_validation(data, current_set, feature_to_add):
    data = np.loadtxt(data)


    number_correctly_classified = 0
    # shape return row, colum
    for i in range(1, data.shape[0]): #This loops over all the rows
        object_to_classify = data[i, 1:]      #Current row and get all column except the 0th
        label_object_to_classify = data[i][0] #First item to the row -- Given object


        nearest_neighbor_distance = float('inf')
        nearest_neighbor_location = float('inf')

        for j  in range(1, data.shape[0]):
            if j != i:
                distance  = sqrt((sum((object_to_classify - data[k, 1:])))
                if distance < nearest_neighbor_distance:
                    nearest_neighbor_distance = distance
                    nearest_neighbor_location = j
                    nearest_neighbor_label = data[nearest_neighbor_location][0]



        if label_object_to_classify == nearest_neightbor_label:
            number_correctly_classified = number_correctly_classified + 1


    accuracy = number_correctly_classfied = number_correctly_classified /size(data,1)

    return accuracy






#Search feature

'''
function feature_search_demo(data) 

for i 1: size(data,2) -1 
    disp(['On the ',num2str(i),'

'''

# def num2str(num):





def feature_search(data):

    print("Beginning search. ")


    best_accuracy_feature_set = set()               #Keep track of the best found feature set
    best_accuracy_of_program = 0                    #Keep track of the best accuracy of the program
    current_set = set()                             #Set of features as we keep on adding features

    for i in range(1, data.shape[1]): #shape return row and column

        feature_to_add_at_this_level = None         #Find best feature at each level
        best_accuracy = 0                           #Keep track of the best accuracy at each level

        for j in range(1, data.shape[1]):
            feature_used = set() #List of feature that were just tested

            if j not in current_set:

                accuracy = leave_one_out_cross_validation(data, current_set, j)

                #To print which feature is being used
                feature_used = current_set
                feature_used.add(j)


                print(f"Using feature(s) {sorted(feature_used)} accuracy is {accuracy}%")     #Print what features are being used

                # Checking best feature at this level
                if accuracy > best_accuracy:
                    best_accuracy = accuracy
                    feature_to_add_at_this_level = j

                # Checking if this is the best set of features
                if best_accuracy_of_program < accuracy:
                    best_accuracy_of_program = accuracy
                    best_accuracy_feature_set = current_set

                # Checks if the accuracy decreased with added feature
                if accuracy < best_accuracy_of_program:
                    print(f"Warning, Accuracy has decreased! Continuing search in case of local maxima")


        current_set.add(feature_to_add_at_this_level)                   #Add the best feature to current_set
        print(f"Feature set {sorted(current_set)} was the best, accuracy is {best_accuracy}%")                  #Print the best found features at this level

    print(f"Finished search!! The best feature subset is {sorted(best_accuracy_feature_set)} , which has an accuracy of {best_accuracy_of_program}%")



def main():
    print("Welcome to Feature Search Algorithm.")
    inputFile = input(print("Type in the name of the file to test: "))

    print()
    print("Type the number of the algorithm you want to run.")
    print()
    print("     1)Forward Selection")
    print("     2)Backward Selection")









if __name__ == '__main__':
    main()



            







