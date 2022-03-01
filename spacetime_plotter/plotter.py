import numpy as np
import matplotlib as plt


class spacetime_obj():
    def __init__(self, label, point=None, speed=None, start=None, end=None):
        self.label = label
        self.point = point
        self.slope = speed
        self.start = start
        self.end = end


def plot_diagram(arr, limit, xlabel=None, ylabel=None, title=None, ref=None):
    """Plot spacetime objects as lines and points

    Args:
        arr: an array of spacetime objects

        limit: the negative and positive limits of the chart

        xlabel: the xlabel

        ylabel: the ylabel

        title: the title

    Returns: nothing
    """
    plot_objects = {}

    for idx, obj in enumerate(arr):
        plot_objects[idx] = {}

        plot_objects[idx]['label'] = obj[0]

        if(obj['speed'] is None):
            plot_objects[idx]['x'] = obj['point'][0]
            plot_objects[idx]['y'] = obj['point'][1]

        elif(obj['speed'] is not None):
            pass

        else:
            raise ValueError(obj, 'defines an spacetime invalid object')
