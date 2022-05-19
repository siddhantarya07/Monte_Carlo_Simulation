import sys
import matplotlib
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
                    
            if(-50 <=x <=50  and 200 <= y <= 300): 
                return True, -1,-1,day
        day =day +1
    return False,x,y,0
    

# Sampling for N times
def step_movement_simulation(number_of_sampling, days):
    success_on_particular_days = []
    total_success = 0                     #Variable to count the number of Success events
    total_failure = 0                     #Variable to count number of Failure events
    mosquito_outside_the_circle = 0       #variable to count mosquito outside the red region
    step_size =250                        #Distance that mosquito can fly in a day
    for i in range(number_of_sampling):
        result = calculate_step_analytics(step_size, days)
        #Mosquito finds the host
        if result[0] == True:
            total_success =total_success +1 
            success_on_particular_days.append(result[3]) 
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
    return success_on_particular_days


def get_probabilities(success_on_particular_days, days, number_of_sampling):
    success_on_each_day  = [0 for i in range(days)] 
    day_list = []
    day_incrementor =0
    while(day_incrementor <days):
        success_on_each_day[day_incrementor] = success_on_particular_days.count(day_incrementor)
        day_incrementor = day_incrementor +1
        day_list.append(day_incrementor)
    prob_success_each_day = []
    for i in range(0,days):
        temp_prob = success_on_each_day[i] /number_of_sampling
        prob_success_each_day.append(temp_prob)
        
    
    return day_list,prob_success_each_day

def plot_graph(day_list, prob_success_each_day):
    xpoints = day_list
    ypoints = prob_success_each_day

    plt.plot(xpoints, ypoints)
    plt.show()

    #Two  lines to make our compiler able to draw:
    plt.savefig(sys.stdout.buffer)
    sys.stdout.flush()


#Driver Functions
def main():
    days= 10
    number_of_sampling = 10000
    success_on_particular_days = step_movement_simulation(number_of_sampling, days)
    result = get_probabilities(success_on_particular_days, days, number_of_sampling)
    plot_graph(result[0], result[1])


if __name__ == "__main__":
    main()
