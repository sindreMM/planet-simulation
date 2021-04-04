# Planet Simulation


## Summary
This is a program for simulating the movement of planets

## Prerequisites
To run this program, the required packages are:
Pillow, Numpy, PyWin32 and Sys

## Running the program
Start by importing the Planet-class and start_simulation-function from
the engine package. To add a planet to the scene, create a new instance of
the planet class using the prameters: mass(int), starting position (x, y),
starting speed (v_x, v_y), color(r, g, b), size(int).

To run the program, call the function start_simulation. An empty call starts
the simulation with a time step of 0.2 and fullscreen mode. Entering other
values for the time step will give change the speed and accuracy of the simulation.
Entering screen size with a tuple (x, y) will start the program in windowed mode
with the specified size.

## Not yet implemented features
ui for setting up simulation
behaviour for collision between planets

