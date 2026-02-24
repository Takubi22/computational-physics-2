#!/usr/bin/env python3
"""functions for generating the Mandelbrot set."""

import matplotlib.pyplot as plt
import numpy as np

class MandelbrotConfig:
    """Configuration class for the Mandelbrot set."""
    def __init__(self, params):
        """Initializes the MandelbrotConfig with a dictionary of parameters."""
        self.nx = params.get('nx', 500)
        self.xmin = params.get('xmin', -2.0)
        self.xmax = params.get('xmax', 2.0)
        self.ymin = params.get('ymin', -2.0)
        self.ymax = params.get('ymax', 2.0)
        self.max_iter = params.get('max_iter', 10)
        self.take_log = params.get('take_log', False)

def mandelbrot(config):
    """create a mandelbrot set with a resolution
    nx x nx points. Returns a matplotlib Figure object"""

    x = np.linspace(config.xmin, config.xmax, config.nx)
    y = np.linspace(config.ymin, config.ymax, config.nx)

    xv, yv = np.meshgrid(x, y, indexing="ij")

    c = xv + 1j * yv

    z = np.zeros_like(c)

    m = np.zeros_like(c, dtype=np.int32)

    for i in range(config.max_iter):
        z = z**2 + c
        m[np.logical_and(np.abs(z) > 2, m == 0)] = i

    plot_fig, ax = plt.subplots()
    plot_fig.set_size_inches = (8, 8)

    if config.take_log:
        m = np.log10(m + 1)

    im = ax.imshow(m.T, origin="lower", extent=[config.xmin, config.xmax, config.ymin, config.ymax])

    plot_fig.colorbar(im, ax=ax)

    return plot_fig

# Example usage:
if __name__ == "__main__":
    params = {'nx': 500, 'max_iter': 50} # Parameters in a dictionary.
    mandel_config = MandelbrotConfig(params)
    fig = mandelbrot(mandel_config)
    plt.show()
