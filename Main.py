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


    best_accuracy_feature_set = set()
    best_accuracy_of_program = 0
    current_set = set()

    for i in range(1, data.shape[1]): #shape return row and column

        # print(f"On the {i}th level of the search tree")
        feature_to_add_at_this_level = None
        best_accuracy = 0

        """
        Here let's keep the data aside 
        
        Let's assume the k fold validation return correct accuracy for the features we are passing and
        checks with the data.
        
        So the job of this function is to keep track of the features respect to the accuracy
        
        But here it's taking the element of our data rather than "what" the feature is?
        
        So is the k-fold validation knowing what feature we used based on the column or?
        
        
        
        """

        for j in range(1, data.shape[1]):

            if j not in current_set:

                accuracy = leave_one_out_cross_validation(data, current_set, j+1)

                #TO IMPLEMENT {...} figuring out a way to print all the features that are currently being used.
                #Elements from current set + J in ordered form
                # I'm thinking maybe first collect all the feature in another list and print them in sorted order.


                print(f"Using feature(s) {...} accuracy is {accuracy}%")
                ''''
                what does j+1 do here
                
                Let's assume accuracy still returns the correct value 
                
                '''

                if accuracy > best_accuracy: #Checking best feature at this level
                    best_accuracy = accuracy
                    feature_to_add_at_this_level = j

                if best_accuracy_of_program < accuracy: #Checking if this is the best set of features
                    best_accuracy_of_program = accuracy
                    best_accuracy_feature_set = current_set

                # THROW A WARNING IF ACCURACY DROPS FROM THE BEST OF THE PROGRAM ACCURACY  -------  DONE
                if accuracy < best_accuracy_of_program: #Checks if the accuracy decreased with added feature
                    print(f"Warning, Accuracy has decreased! Continuing search in case of local maxima")


                    ''''
                    Since we are adding only only feature at every level, does feature to add at this level need to be a 
                    set? Or am I missing something?
                    So I changed it to int rather than set
                    
                    '''



        #TO IMPLEMENT NEED TO KEEP TRACK OF THE BEST ACCURACY OF PROGRAM AND THE FEATURE --- DONE

        #AND PRINT WHICH FEATURE SET WAS THE BEST IN EACH LEVEL

        #Here I'm thinking to implement add elements from current_set and feature to add at this level to a list, sort them and print them with best_accuracy


        print(f"Feature set {...} was the best, accuracy is {best_accuracy}%")





        current_set.add(feature_to_add_at_this_level)
        print(f"On this level {i} i added feature, {feature_to_add_at_this_level}.")



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



            







