from engine import Planet, start_simulation

Planet(1000000, [0, -0.15], [600, 500], (0, 250, 250), 50)
Planet(1000000, [0, 0.15], [1300, 500], (250, 250, 0), 50)


start_simulation(10)


