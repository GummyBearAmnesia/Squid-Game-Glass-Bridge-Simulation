# Squid-Game-Glass-Bridge-Simulation
Using a probability function to calculate the probability of a contestant surviving the glass bridge from the popular TV show Squid Game

In this project, we formed equations to simulate the Squid Games bridge, in which there are 16 contestants trying to make it across 18 rows of glass panels set out so that each row has one safe panel and one panel that will fall through upon impact. We used python code to run a simulation of this scenario a large number of times and used the data to calculate the probabilities of success for each contestant, investigating their accuracy to the theoretical values.

In this task, a code was written to simulate the situation and compare with the theoretical probability of success for each contestant, which we have found in the introduction. First, the random module was called to allow random number generators to be used in the code.

First we built a function called “Trial()” to simulate one trial with of all 16 contestants. The function returns a dictionary called “Contestants_Placement” which contains a record of the final platform each contestant reaches. The variable “fate” indicates the success or failure of each step made by contestants, this variable is randomly generated to simulate the players random choice.

Finally, we wrote a function called “Simulation” to simulate large numbers of trials, it collects the data from each trial and adds a value to each contestant’s total successes every time they reach the 18th platform (and hence survive the challenge). The function uses two dictionaries, the first to store the total number of successes for each contestant; using this it calculates and stores the probabilities of success for each contestant in a second dictionary. The first loop iterates the trial for large number of trials, and the second loop iterates through the dictionaries to find and store the probability of success for each contestant. Note that we define success as having reached the 18th platform.

In order to make a comparison between the calculated and theoretical values added another library called “ProbError” to calculate and store the values for the error in the calculated value for each contestant. The code is run with 10^7 number of trials in order to calculate the probabilites and their errors at a high accuracy.
