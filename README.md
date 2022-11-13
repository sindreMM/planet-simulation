# Planet Simulation


## Summary
This library allows the user to set up and run n-body simulations 

## Required libraries:
* Opencv-python
* Numpy 
* PyWin32
* Sys

## Running the program
Start by importing the Planet-class and start_simulation-function from
the engine package. To add a planet to the scene, create a new instance of
the planet class using the prameters: mass (int), starting position (x, y),
starting speed (v_x, v_y), color(r, g, b), size(int).

To run the program, call the function start_simulation. An empty call starts
the simulation with a time step of 0.2 and fullscreen mode. Entering other
values for the time step will give change the speed and accuracy of the simulation.
Entering screen size with a tuple (x, y) will start the program in windowed mode
with the specified size.


Here are some example simulations:
![planetSimulation3](https://user-images.githubusercontent.com/39603487/201530254-7a4659df-ade8-4eed-9758-21ce78d55e22.gif)
![planetSimulation2](https://user-images.githubusercontent.com/39603487/201520811-8f3754d8-1e21-4751-b6ae-2b20f01cf275.gif)
![planetSimulation1](https://user-images.githubusercontent.com/39603487/201520802-e720bf81-0973-4391-9b60-ae3fc8ec13f5.gif)
