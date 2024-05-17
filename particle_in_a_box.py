import constants as con
import math
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

class Particle_In_A_Box:
    def __init__(self, length: float = 1., mass: float = 1.):
        """_summary_

        Args:
            length (float): length of the box in Bohr radius. The default value is 1.
            mass (float, optional): mass of the particle in electron mass. The default value is 1.
        """
        self.mass = mass
        self.length = length
        
        self.ground_energy = con.H * con.H / (8. * self.mass * con.M_E * self.length * con.A_0 * self.length * con.A_0)
        self.ground_energy /= con.E_V
        
    
    def energy(self, n: int)-> float:
        """It returns the energy eigenstate for a given quantum number n

        Args:
            n (int): the quantum number

        Returns:
            float: the energy in eV
        """
        return n*n*self.ground_energy
    
    def wavefunction(self, n: int, x: float)->float:
        """It returns the wavefunction

        Args:
            n (int): the quantum number
            x (float): the value of the x coordinate

        Returns:
            float: the value of the wavefunction for a specific n at the x position
        """
        
        psi = math.sqrt(2./self.length) * math.sin(n * con.PI * x / self.length)
        
        return psi
    
    def plot_wavefunction(self, n: int)->None:
        """It plots the wavefunction for a given quantum number n

        Args:
            n (_type_): The quantum number
        """
        step = self.length/200.
        x_array = np.arange(stop=self.length + step, step=step)
        y_array = np.array([self.wavefunction(x, n) for x in x_array])
        
        graph = sns.lineplot(x=x_array, y=y_array)
        
        graph.set_title(rf'$\psi(x)=\sqrt{{\frac{{2}}{{L}}}} \sin({n}\pi x/L)$')
        graph.set_ylabel(r"$E/\text{eV}$")
        plt.show()
    
    def __str__(self)->str:
        """String representation of the object

        Returns:
            str: the string representation of the object
        """
        repr_str = "Particle in a monodimensional box\n"

        repr_str += "mass/electron mass = " + str(self.mass) + "\n"
        repr_str += "length of the box in Bohr radius = " + str(self.length) + "\n"
        repr_str += "Ground state energy in eV = " + str(self.ground_energy) + "\n"
        
        return repr_str
        