"""Module to aid in the creation of spacetime diagrams."""

import numpy as np
import matplotlib.pyplot as plt


class WorldLine:
    """Represents an object traveling through space at a given speed."""
    def __init__(self, label, point, speed=None, start=None, end=None):
        """Initialize a new WorldLine object."""
        self.label: str = label
        self.point: tuple = point # (x,y)
        self.speed: float = speed # measured as unit of speed of light
        self.start: float = start
        self.end: float = end


class Event:
    """Represents a static event at a given time and place."""
    def __init__(self, label, point, draw_lightline=False):
        """Initialize a new Event object."""
        self.label: str = label
        self.point: tuple = point
        self.draw_lightline: bool = draw_lightline


def _lorentz_transformation(point, vel) -> tuple:
    """Apply a lorentz tranformation to a given point.
    
    Params:
        - Point: An (x, ct) point to apply the transformation to
        - Vel: Relative velocity of the rest frame
    """
    assert abs(vel) <= 1, f"vel must be between -1 and 1. Value of vel: {vel}"
    gamma: float = 1 / np.sqrt(1 - (vel**2))
    x_prime: float = gamma * ( point[0] - vel * point[1] )
    t_prime: float = gamma * ( point[1] - point[0] * vel)
    return (x_prime, t_prime)


def plot_diagram(arr, limit, xlabel='x', ylabel='ct', title='Spacetime Graph', ref=None) -> None:
    """Plot given WorldLines and Events in a reference frame."""
    fig, ax = plt.subplots(figsize=(6,6))

    ax.set_xlim(limit[0],limit[1])
    ax.set_ylim(limit[0],limit[1])
    ax.set_xlabel('x')
    ax.set_ylabel('ct')
    ax.set_title(title)

    plt.gca().set_aspect('equal')
    plt.minorticks_on()
    plt.tick_params(direction='in', which='both')
    plt.grid(which='major', alpha=0.7)
    plt.grid(which='minor', alpha=0.2)

    ax.plot((limit[0],limit[1]), (0,0),color='Blue',linestyle='--', zorder=0)
    ax.plot((0,0),(limit[0],limit[1]),color='Blue',linestyle='--', zorder=0)

    for obj in arr:
        if obj.__class__.__name__ == 'WorldLine':
            if obj.label == ref:
                ref_speed: float = obj.speed

    for obj in arr:
        if obj.__class__.__name__ == 'WorldLine':
            x: float = obj.point[0]
            t: float = obj.point[1]

            if obj.speed == 0:
                x1: float = x
                x2: float = x
                t1: float = limit[0]
                t2: float = limit[1]

                if obj.start is not None:
                    if t1 < t2 and t1 < obj.start:
                        t1 = obj.start
                    elif t2 < t1 and t2 < obj.start:
                        t2 = obj.start

                if obj.end is not None:
                    if t1 > t2 and t1 > obj.end:
                        t1 = obj.end
                    elif t2 > t1 and t2 > obj.end:
                        t2 = obj.end

                x1,t1 = _lorentz_transformation((x1,t1), ref_speed)
                x2,t2 = _lorentz_transformation((x2,t2), ref_speed)

                x_points: list[float] = [x1, x2]
                t_points: list[float] = [t1, t2]

                ax.plot(x_points, t_points, label=obj.label, zorder=2)
                continue


            slope = 1 / obj.speed

            x1: float = limit[0]
            t1: float = slope * (x1 - x) + t
            x2: float = limit[1]
            t2: float = slope * (x2 - x) + t

            if obj.start is not None:
                if t1 < t2 and t1 < obj.start:
                    x1 = ((obj.start - t1) / slope) + x1
                    t1 = obj.start
                elif t2 < t1 and t2 < obj.start:
                    x2 = ((obj.start - t2) / slope) + x2
                    t2 = obj.start

            if obj.end is not None:
                if t1 > t2 and t1 > obj.end:
                    x1 = ((obj.end - t1) / slope) + x1
                    t1 = obj.end
                elif t2 > t1 and t2 > obj.end:
                    x2 = ((obj.end - t2) / slope) + x2
                    t2 = obj.end

            if np.abs(slope) != 1:
                x1,t1 = _lorentz_transformation((x1,t1), ref_speed)
                x2,t2 = _lorentz_transformation((x2,t2), ref_speed)

            x_points: list[float] = [x1, x2]
            t_points: list[float] = [t1, t2]

            ax.plot(x_points, t_points, label=obj.label, zorder=2)

        if obj.__class__.__name__ == 'Event':
            obj.point = _lorentz_transformation(obj.point, ref_speed)
            x_origin = obj.point[0]
            t_origin = obj.point[1]

            if obj.draw_lightline:
                x_1: float = limit[0]
                t_1: float = -1 * (x_1 - x_origin) + t_origin
                x_2: float = limit[1]
                t_2: float = 1 * (x_2 - x_origin) + t_origin

                x_points: list[float] = [x_1, x_origin, x_2]
                t_points: list[float] = [t_1, t_origin, t_2]

                ax.plot(x_points, t_points, color='#dddddd', zorder=1)

            ax.scatter(x_origin, t_origin,50, label=obj.label, ec='k', zorder=3)

    plt.legend()
    plt.show()
