from plotter import spacetime_obj, plot_diagram
import numpy as np

objects = [
    spacetime_obj('Object A', (0,0), 0.5, start=0, end=2),
    spacetime_obj('Object B', (0,4), -0.5),
    spacetime_obj('Object C', (0,2), -0.9, end=5)
]
lim = (-1, 10)

plot_diagram(objects, lim)