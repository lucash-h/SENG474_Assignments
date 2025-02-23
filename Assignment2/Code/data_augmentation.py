

def data_augment(images, labels, r_dir, degree):

#rotate in a direction x degrees
#look into randrotate.py --> given
for i in range(0,num to augment):
    img = images[i]
    new img = randrotate(img)
    new_label = label[i]
    #add it to set or replace??

return images & labels


''' 
main

import data
process/normalize
splice out smaller set out of larger set

--- Testing hyperparameters ---
choose num to augment out of smaller set
set r dir and degree

run it then train

--- hyperparams---


'''
