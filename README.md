# quantum_learning

In *constant.py* there are some useful constants.

In *particle_in_a_box.py* there is the implementation of a class about the quantum problem of a particle in a monodimensional box.
Both the wavefunction and the energy are implemented and there is the possibility to inspect the graph of the wavefunction for 
a given quantum number. 


# Example of usage
Instantiating the class with the default values
`my_obj = Particle_In_A_Box()`

Printing the information about the created object
`print(my_obj = Particle_In_A_Box())`

It displays the graph of the wavefunction for the level with $n=5$
`my_obj.plot_wavefunction(5)`
