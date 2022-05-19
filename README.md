# Monte_Carlo_Simulation
**Project Description**</br>
Monte Carlo simulation is a model used to predict the probability of different outcomes when the intervention of random variables is present.
It help to explain the impact of risk and uncertainty in prediction and forecasting models.
</br>
For this project, we have a mosquito with different problem statements.</br>
</br>
**Problem Statement 1**
1. The mosquito is born in a puddle at [0,0]</br>
2. She will live for ten days.</br>
3. At the beginning of each day, she will try to smell a host.</br>
4. If see can smell a host, she will find them, game over.</br>
5. If see cannot, she will “turn off” her sense of smell for the rest of the day and fly 250 m in a random direction. Next morning, GOTO ‘1’. </br>
6. Obviously, after ten days, if she does not find a host, she dies without taking a blood meal.
7. A mosquito can smell a human at 50 meters. </br>

<img width="128" alt="Mosquito" src="https://user-images.githubusercontent.com/72067723/169188568-60e4bf07-f927-4ff5-abf5-1b9ece838394.PNG">

**Problem Statement 2**</br>
Let us assume that the mosquito turn off its sense of smell as it makes a random flight. However, suppose that was not the case. That would mean that even if it flies over the yellow circle, it will find the host. Lets compute the probability of finding the host.

**Problem Statement 3**
Suppose that the center of the yellow circle can move along the Y axis, form as little as zero to at most 2,525 m (at which point, the mosquito cannot reach it), Let us create a plot showing the probably that the mposquito finds the host, as a function of K.
<img width="125" alt="Mosquioto_K_function" src="https://user-images.githubusercontent.com/72067723/169190664-bdeed106-24e4-403f-8775-1ab819f79e3f.PNG">

**Project Structure**</br>
All problem statemenst logics has been written in seperate python files which can be found in code folder.</br>
**1. Main.py:** This file contains the solution of problem statement 1.</br>
**2. Mosquito_Flying_WithSmell.py:** This file contains the solution of problem statement 2.</br>
**3. Mosquito_WithoutSmell_WhileFlying_WithHostMovement.py and Mosquito_Withsmell_Whileflying_WithoutHostMovement.py:** This file contains the the solution for problem statement 3.</br>

**How to install and run the project**</br>
The code has been written in Python 3.9.7 and can be cloned from this repository.
The program can be executed by running the python seperate python files command in the project folder's command prompt.

Please find the report and code for more details.









