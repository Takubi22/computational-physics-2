import numpy as np
import matplotlib.pyplot as plt

class MandelbrotSet:
    """
    A class to generate and plot the Mandelbrot set.

    Attributes:
        N (int): The number of points on each axis (grid resolution).
        xmin (float): The minimum x-coordinate for the plot.
        xmax (float): The maximum x-coordinate for the plot.
        ymin (float): The minimum y-coordinate for the plot.
        ymax (float): The maximum y-coordinate for the plot.
        max_iter (int): The maximum number of iterations for the escape-time algorithm.
    """
    
    def __init__(self, N, xmin=-2.0, xmax=2.0, ymin=-2.0, ymax=2.0, max_iter=10):
        """
        Initializes the MandelbrotSet object with given parameters.
        """
        self.N = N
        self.xmin = xmin
        self.xmax = xmax
        self.ymin = ymin
        self.ymax = ymax
        self.max_iter = max_iter
        
    def generate_set(self):
        """
        Generates the Mandelbrot set data using the escape-time algorithm.

        Returns:
            np.ndarray: A 2D array representing the number of iterations 
                        each point took to escape.
        """
        # Create a grid of complex numbers
        x = np.linspace(self.xmin, self.xmax, self.N)
        y = np.linspace(self.ymin, self.ymax, self.N)
        xv, yv = np.meshgrid(x, y, indexing="ij")
        c = xv + 1j * yv
        
        z = np.zeros((self.N, self.N), dtype=np.complex128)
        m = np.zeros((self.N, self.N), dtype=np.int64)
        
        # Iteratively apply the function z = z^2 + c
        for i in range(1, self.max_iter):
            z = z**2 + c
            
            # Find points that have escaped and have not been marked yet
            has_escaped = np.abs(z) > 2
            not_marked_yet = m == 0
            
            # Mark these points with the current iteration number
            m[np.logical_and(has_escaped, not_marked_yet)] = i
            
        return m

    def plot_set(self):
        """
        Generates and displays a plot of the Mandelbrot set.
        """
        # Generate the set data
        mandelbrot_data = self.generate_set()
        
        # Create the plot
        fig, ax = plt.subplots()
        fig.set_size_inches(8, 8)
        
        im = ax.imshow(np.transpose(mandelbrot_data), origin="lower",
                       extent=[self.xmin, self.xmax, self.ymin, self.ymax],
                       cmap="magma")
        
        ax.set_title(f"Mandelbrot Set (N={self.N}, Iterations={self.max_iter})")
        ax.set_xlabel("Real Axis")
        ax.set_ylabel("Imaginary Axis")
        fig.colorbar(im, ax=ax, label="Iterations to Escape")
        
        plt.show()
        
# --- Example Usage ---
if __name__ == "__main__":
    # Create an instance of the class
    mandelbrot_object = MandelbrotSet(N=500, max_iter=100)
    
    # You can also change the parameters for a zoomed-in view
    # mandelbrot_object = MandelbrotSet(N=500, xmin=-0.75, xmax=-0.74, ymin=0.08, ymax=0.09, max_iter=200)

    # Generate and plot the set
    mandelbrot_object.plot_set()
