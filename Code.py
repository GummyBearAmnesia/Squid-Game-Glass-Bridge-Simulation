import random

def Trial():
    #Dictionary containing each contestant and will be updated to store what platform they reach
    Contestants_Placement = {1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0,13:0,14:0,15:0,16:0}

    #Loops through each contestant
    for each in range(1,17):

    #i is the amount of platforms guessed
        i = 1
    #A fate of 1: Alive
    #A fate of 0: Dead
        fate = 1

        #While the contestant is still alive, they can continue to attempt the next platform
        while fate == 1:
            fate = random.randint(0,1)
            if fate == 0:
                #Checks if the contestant is the first or not
                #If not, the amount of platforms they guessed will be added on to the last reached platform
                if each > 1:
                    Contestants_Placement[each] = Contestants_Placement[each-1] + i
                    #The placement stops at 18
                    #If the previous contestant reached level 18, the next contestant will too.
                    if Contestants_Placement[each] >= 18:
                        Contestants_Placement[each] = 18
                #If the contestant is number 1, the amount of platforms starts from 1, no addition needed.
                else:
                    Contestants_Placement[each] = i
            else:
                i += 1
                
    return Contestants_Placement



def Simulation():
    #A dictionary to store how many times the contestant successfully crosses the bridge out of all the trials
    Contestants_Successes = {1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0,13:0,14:0,15:0,16:0}
    #A dictionary to store the calculated percentage of success for each player
    Contestants_Probabilities = {1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0,13:0,14:0,15:0,16:0}


    #A loop that runs the trial 10**4 times
    i=0
    while i <= 10**4:
        for each in Trial():
            #For each contestant in the trial, the Contestants_Successes dictionary is updated
            #1 success is added for a contestant if they have crossed the bridge during this Trial
            if Trial()[each]==18:
                Contestants_Successes[each] += 1
        i+= 1

    #Loop takes each contestant and divides their amount of successes by the total amount of trials to get a probability of success
    for each in Contestants_Successes:
        Prob = (Contestants_Successes[each])/10**4
        #Updates the Contestants_Probabilities dictionary to store the calculated probability for each player.
        Contestants_Probabilities[each] = Prob


    #Outputs the final successes for each player, and the calculated probability that each crosses the bridge
    print("SUCCESSES:")
    print(Contestants_Successes)
    print("PROBABILITIES:")
    print(Contestants_Probabilities)

Simulation()
