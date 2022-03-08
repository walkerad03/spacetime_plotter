from plotter import worldline as wl, event, \
     plot_diagram

objects = [
    wl('Train Back', (-1, 0), 0.5),
    wl('Train Front', (1,0), 0.5),
    wl('Stationary Observer', (0,0), 0),
    wl('Train Observer', (0,0), 0.5),
    event('Lightning Strike A',(-1,0),draw_lightline=True),
    event('Lightning Strike B', (1,0),draw_lightline=True)
]
lim = (-5, 5)
plot_diagram(objects,lim, title="Reference Frame of Stationary Observer",ref='Stationary Observer')
plot_diagram(objects,lim, title="Reference Frame of Train Bound Observer",ref='Train Observer')
