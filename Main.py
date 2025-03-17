import time

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

    data_copy = data.copy()
    for remove_column in range(1, data_copy.shape[1]):
        if remove_column not in current_set and remove_column != feature_to_add:
            data_copy[:, remove_column] = 0

    number_correctly_classified = 0
    # shape return row, colum
    for i in range(1, data_copy.shape[0]):         #This loops over all the rows

        object_to_classify = data_copy[i, 1:]      #Current row and get all column except the 0th
        label_object_to_classify = data_copy[i][0] #First item to the row -- Given object


        nearest_neighbor_distance = float('inf')
        nearest_neighbor_location = float('inf')
        nearest_neighbor_label = ""

        for j  in range(1, data_copy.shape[0]):
            if j != i:

                distance = 0
                for k in range(1, data_copy.shape[1]):
                    distance +=  (data_copy[j][k] - data_copy[i][k]) ** 2
                distance = distance ** 0.5


                if distance < nearest_neighbor_distance:
                    nearest_neighbor_distance = distance
                    nearest_neighbor_location = j
                    nearest_neighbor_label = data_copy[nearest_neighbor_location][0]



        if label_object_to_classify == nearest_neighbor_label:
            number_correctly_classified += 1


    accuracy = number_correctly_classified /data_copy.shape[0]

    return accuracy






#Search feature

'''
function feature_search_demo(data) 

for i 1: size(data,2) -1 
    disp(['On the ',num2str(i),'

'''

# def num2str(num):





def forward_feature_search(data):
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
                feature_used = current_set.copy()
                feature_used.add(j)


                print(f"Using feature(s) {sorted(feature_used)} accuracy is {round(accuracy*100,2)}%")     #Print what features are being used

                # Checking best feature at this level
                if accuracy > best_accuracy:
                    best_accuracy = accuracy
                    feature_to_add_at_this_level = j

                # Checking if this is the best set of features
                if best_accuracy_of_program < accuracy:
                    best_accuracy_of_program = accuracy
                    best_accuracy_feature_set = current_set.copy()
                    best_accuracy_feature_set.add(j)




        current_set.add(feature_to_add_at_this_level)                   #Add the best feature to current_set
        print(f"Feature set {sorted(current_set)} was the best, accuracy is {round(best_accuracy*100,2)}%")                  #Print the best found features at this level
        if not i == data.shape[1] - 1 :
            if best_accuracy < best_accuracy_of_program:
                print(f"Warning, Accuracy has decreased! Continuing search in case of local maxima")

    print(f"Finished search!! The best feature subset is {sorted(best_accuracy_feature_set)} , which has an accuracy of {round(best_accuracy_of_program*100,2)}%")

def backward_feature_search(data):
    
    best_accuracy_feature_set = set()               #Keep track of the best found feature set
    best_accuracy_of_program = 0                    #Keep track of the best accuracy of the program
    current_set = set()                             #Set of features as we keep on removing features

    not_first_run = False                           #Not remove any element in the first run

    #Mutate the current set with all the features
    for k in range(1, data.shape[1]):
        current_set.add(k)


    for i in range(1, data.shape[1]): #shape return row and column
        previous_run = set()                        #Not print multiple times for first run

        best_accuracy = 0                           #Keep track of the best accuracy at each level
        feature_set_to_keep = set()                 #Best feature set to keep

        for j in range(1, data.shape[1]):

            feature_to_use = current_set.copy()     #List of feature to test

            # Only remove and test the elements if they are present in current search
            if j in feature_to_use:

                # Testing different removals of features
                if j in feature_to_use and not_first_run:
                    feature_to_use.remove(j)

                accuracy = leave_one_out_cross_validation(data, feature_to_use, None)       #Accuracy of feature set being tested

                if not previous_run == feature_to_use:
                    print(f"Using feature(s) {sorted(feature_to_use)} accuracy is {round(accuracy*100,2)}%")     #Print what features are being used

                # Checking best feature at this level
                if accuracy > best_accuracy:
                    best_accuracy = accuracy
                    feature_set_to_keep = feature_to_use.copy()

                # Checking if this is the best set of features
                if best_accuracy_of_program < accuracy:
                    best_accuracy_of_program = accuracy
                    best_accuracy_feature_set = feature_to_use.copy()


                previous_run = feature_to_use.copy()

        current_set = feature_set_to_keep.copy()            #Replacing the best feature set after removal to current set
        not_first_run = True

        print(f"Feature set {sorted(feature_set_to_keep)} was the best, accuracy is {round(best_accuracy*100, 2)}%")                  #Print the best found features at this level

        # Checks if the accuracy decreased with new feature set
        if not i == data.shape[1] - 1:
            if best_accuracy < best_accuracy_of_program:
                print(f"Warning, Accuracy has decreased! Continuing search in case of local maxima")

    print(f"Finished search!! The best feature subset is {sorted(best_accuracy_feature_set)} , which has an accuracy of {round(best_accuracy_of_program*100, 2)}%")

    



    


def main():
    print("Welcome to Feature Search Algorithm.")   
    inputFile = "CS170_Small_Data__7.txt"
    print()

    print("     1)Forward Selection")
    print("     2)Backward Selection")
    
    algorithm_type = input("Type the number of the algorithm you want to run. ")
    print()

    data = np.loadtxt(inputFile)

    start_time = time.time()
    if algorithm_type == "1":
        forward_feature_search(data)

    if algorithm_type == "2":
        backward_feature_search(data)

    end_time = time.time()

    print(f"Time taken to run the algorithm is: {round(end_time - start_time,2)} seconds.")










if __name__ == '__main__':
    main()



            







