import numpy as np
import matplotlib.pyplot as plt


class worldline():
    def __init__(self, label, point, speed=None, start=None, end=None):
        self.label = label
        self.point = point # (x,y)
        self.speed = speed # measured as unit of speed of light
        self.start = start
        self.end = end

class lightline():
    def __init__(self, point):
        self.point = point

class event():
    def __init__(self, label, point, draw_lightline=False):
        self.label = label
        self.point = point
        self.draw_lightline = draw_lightline

def _lorentz_transformation(point, v) -> tuple:
    gamma: float = 1 / np.sqrt(1 - (v**2))
    x = gamma * ( point[1] - v * point[0] )
    t = gamma * ( point[0] - point[1] * v)
    return (t, x)


def plot_diagram(arr, limit, xlabel='x', ylabel='ct', title='Spacetime Graph', ref=None) -> None:
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
        if obj.__class__.__name__ == 'worldline':
            if obj.label == ref:
                ref_speed = obj.speed

    for obj in arr:
        if obj.__class__.__name__ == 'worldline':
            x = obj.point[0]
            t = obj.point[1]

            if obj.speed == 0:
                x1, x2 = x, x
                t1 = limit[0]
                t2 = limit[1]

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
                        
                x_points = [x1, x2]
                t_points = [t1, t2]

                ax.plot(x_points, t_points, label=obj.label, zorder=2)
                continue


            slope = 1 / obj.speed

            x1 = limit[0]
            t1 = slope * (x1 - x) + t
            x2 = limit[1]
            t2 = slope * (x2 - x) + t

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

            x_points = [x1, x2]
            t_points = [t1, t2]

            ax.plot(x_points, t_points, label=obj.label, zorder=2)

        if obj.__class__.__name__ == 'event':
            obj.point = _lorentz_transformation(obj.point, ref_speed)
            x_origin = obj.point[0]
            t_origin = obj.point[1]

            if obj.draw_lightline:
                x_1 = limit[0]
                t_1 = -1 * (x_1 - x_origin) + t_origin
                x_2 = limit[1]
                t_2 = 1 * (x_2 - x_origin) + t_origin

                x_points = [x_1, x_origin, x_2]
                t_points = [t_1, t_origin, t_2]

                ax.plot(x_points, t_points, color='#dddddd', zorder=1)

            ax.scatter(x_origin, t_origin,50, label=obj.label, ec='k', zorder=3)

    plt.legend()
    plt.show()
