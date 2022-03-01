import numpy as np
import matplotlib.pyplot as plt


class spacetime_obj():
    def __init__(self, label, point, speed=None, start=None, end=None):
        self.label = label
        self.point = point # (x,y)
        self.speed = speed # measured as unit of speed of light
        self.start = start
        self.end = end
        if self.speed == None:
            self.type = 'point'
        else:
            self.type = 'line'
        

def plot_diagram(arr, limit, xlabel='x', ylabel='ct', title='Spacetime Graph', ref=None):
    """Plot spacetime objects as lines and points

    Args:
        arr: an array of spacetime objects

        limit: the negative and positive limits of the chart

        xlabel: the xlabel

        ylabel: the ylabel

        title: the title

    Returns: nothing
    """
    fig, ax = plt.subplots(figsize=(6,6))

    ax.set_xlim(limit[0],limit[1])
    ax.set_ylim(limit[0],limit[1])
    ax.set_title(title)

    ax.plot((limit[0],limit[1]), (0,0),color='Blue',linestyle='--')
    ax.plot((0,0),(limit[0],limit[1]),color='Blue',linestyle='--')

    plot_objects = {}

    for idx, obj in enumerate(arr):
        plot_objects[idx] = {}

        plot_objects[idx]['label'] = obj.label

        if obj.type == 'line':
            x = obj.point[1]
            y = obj.point[0]

            if obj.speed != 0:
                slope = 1 / obj.speed
            else:
                slope == np.inf

            x1 = limit[0]
            y1 = slope * (x1 - x) + y
            x2 = limit[1]
            y2 = slope * (x2 - x) + y

            if obj.start is not None:
                if obj.start > y1:
                    x1 = (obj.start - y) / slope + x
                    y1 = obj.start

            if obj.end is not None:
                if obj.end < y2:
                    x2 = (obj.end - y) / slope + x
                    y2 = obj.end


            x_points = [x1, x2]
            y_points = [y1, y2]

            ax.plot(x_points, y_points, label=obj.label)
    plt.legend()
    plt.show()


