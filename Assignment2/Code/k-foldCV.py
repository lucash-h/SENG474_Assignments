#k fold cross validation
#general idea is to seperate the train + test set into small portions
#So that for example the split set into 4 sets with 6 pieces each
#then per set: 5 training sets and 1 test set
#so split both into 4
#split train into 5 rando

def k_fold_cross_validation(x_train, y_train, x_test, y_test, set_number, set_portion_size):
    k_fold_list = [set_number]

    #check to see if set_number is valid or set_number -1
    for i in range(0, set_number):
        portion_set_list = [set_portion_size]

        for j in range(0, set_portion_size):
            if(j == set_portion_size):
                set_portion_size[j] = x_test, y_test
                break

            portion_set_list[j] = x_train, y_train
            
    #might be better to just splice this shieet
    '''
    A list with each validation set
    A list with each set in the validation set (ie 5 train and 1 test)
    '''

    k_fold_list = [
        #splice into x values --> train-test tupples
    ]
    for set in k_fold_list:
        #splice each x values into 5 and add test but I think you actually want 6 training sets and validate that shit