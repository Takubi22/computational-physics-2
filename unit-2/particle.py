"""
PARTICLE CODE: CP2 - 2026
"""

# Import  libraries
import numpy as np
import scipy.constants as ct

# Create class

class Particle:
    """
    This class computes the kinetic energy of a non-relat. particle
    """
    # Class attribute: gravitational constant (SI units)
    _grav_ct = ct.G

    # Constructor
    def __init__(self, mass, velo):
        """
        Constructor: mass, velocity for the particle
        """
        self.mass = mass
        self.velo = velo

    # (1) Instance method: this uses self (mass, velo)
    def kinetic_energy(self):
        """
        Function to compute the kinetic energy.
        """
        # Kinetic energy equation
        k_e = self.mass*self.velo**2

        return k_e

    # (2) Class method: Factory method p -> v
    @classmethod
    def from_momentum(cls, mass, momentum):
        """
        Calculates the velocity from the momentum
        """
        # Non-relativistic particle
        velo = momentum/mass

        return cls(mass, velo)

    # (3) Static method:
    @staticmethod
    def escape_velocity(mass, radius):
        """
        Computes the esc. velocity of an object bound to a massive object.
        """
        # Gravitational constant: static method does not see the class attribute
        _grav_ct = ct.G

        # Compute escape velocity
        esc_v = np.sqrt(2 * _grav_ct * mass / radius)

        return esc_v


# Function Test
def test_particle():
    """
    Testing the kinetic energy method.
    """
    obj = Particle(4.,6.)
    a = obj.kinetic_energy()
    assert a == 72.
