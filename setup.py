"""Setup file for spacetime_plotter package."""
import setuptools

with open('requirements.txt', 'r') as f:
    install_requires = f.read().splitlines()

setuptools.setup(name='spacetime_plotter',
                 packages=['spacetime_plotter'],
                 install_requires=install_requires)
