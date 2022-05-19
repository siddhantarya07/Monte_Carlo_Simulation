import sys
import matplotlib
# matplotlib.use('Agg')
# import matplotlib.pyplot as plt
from matplotlib import pyplot as plt
import numpy as np
import math
import random 


# Analyze mosquito movements
def calculate_step_analytics(step_size, days):
    # x and y are arrays which store the coordinates of the position
    x = 0  
    y = 0
    day = 0
    while(day<days):
        theta=2*math.pi*random.random()
        x_step=step_size*math.cos(theta)
        y_step=step_size*math.sin(theta)
        int_x_steps = int(x_step)
        int_y_steps = int(y_step)       
        i=0
        j=0
        while(i < abs(int_x_steps) or j < abs(int_y_steps)):
            if(i < abs(int_x_steps)):
                i = i+1
                if int_x_steps < 0:
                    x = x -1
                else:
                    x = x+1
            if(j< abs(int_y_steps)):
                j = j+1
                if int_y_steps < 0:
                    y = y -1
                else:
                    y = y+1
            # As mosquito can fly accross y axis
            random_y_axis = random.randint(0, 2525)        
            # if(-50 <=x <=50  and 200 <= y <= 300): 
            if(-50 <=x <=50  and random_y_axis-100 <= y <= random_y_axis+100): 
                return True, -1,-1,random_y_axis
        day =day +1
    return False,x,y,0
    

# Sampling for N times
def step_movement_simulation(number_of_sampling, days):
    success_on_particular_days = []
    success_on_particular_y_axis= []
    total_success = 0                     #Variable to count the number of Success events
    total_failure = 0                     #Variable to count number of Failure events
    mosquito_outside_the_circle = 0       #variable to count mosquito outside the red region
    step_size =250                        #Distance that mosquito can fly in a day
    for i in range(number_of_sampling):
        result = calculate_step_analytics(step_size, days)
        #Mosquito finds the host
        if result[0] == True:
            total_success =total_success +1 
            #success_on_particular_days.append(result[3]) 
            success_on_particular_y_axis.append(result[3])
        #Mosquito fails to find the host inside the red region                           
        elif result[0] == False and result[1] <= 1000 and result[2] <= 1000:
            total_failure = total_failure +1  
        #Mosquito dies outside the circle                           
        else:
            mosquito_outside_the_circle = mosquito_outside_the_circle +1  #Mosquito is outside the red region
    

         
    # Finding probabilities
    probability_of_finding_host = total_success/number_of_sampling
    probability_of_dying_in_red_region = mosquito_outside_the_circle/number_of_sampling
    print(f"The probability of finding a host before mosquito dies is: {probability_of_finding_host}")
    print(f"The probability of mosquito dying outside the red region is: {probability_of_dying_in_red_region}")
    # return success_on_particular_days
    return success_on_particular_y_axis


def get_probabilities(success_on_particular_y_axis, number_of_sampling):
    success_on_each_day  = [0 for i in range(2525)] 
    k_axis = []
    day_incrementor =0
    while(day_incrementor <2525):
        success_on_each_day[day_incrementor] = success_on_particular_y_axis.count(day_incrementor)
        day_incrementor = day_incrementor +1
        k_axis.append(day_incrementor)
    prob_success_each_day = []
    for i in range(0,2525):
        temp_prob = success_on_each_day[i] /number_of_sampling
        prob_success_each_day.append(temp_prob)
        
    
    return k_axis,prob_success_each_day

def plot_graph(k_axis, prob_success_each_day):
    xpoints = k_axis
    ypoints = prob_success_each_day

    plt.plot(xpoints, ypoints)
    plt.show()

    #Two  lines to make our compiler able to draw:
    plt.savefig(sys.stdout.buffer)
    sys.stdout.flush()


#Driver Functions
def main():
    days= 10
    number_of_sampling = 1000000
    success_on_particular_y_axis = step_movement_simulation(number_of_sampling, days)
    result = get_probabilities(success_on_particular_y_axis, number_of_sampling)
    plot_graph(result[0], result[1])


if __name__ == "__main__":
    main()
