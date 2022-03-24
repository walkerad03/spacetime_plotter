"""A module containing tests for the plotter module."""

import pytest
import spacetime_plotter.plotter as plt

def test_pytest():
    """A test to confirm that pytest is loaded properly."""
    assert True == True


def test_lorentz_transformation_normal_case_1():
    """Testing the '_lorentz_transformation' function."""
    calculated = plt._lorentz_transformation((5,3), 0.8)
    real = (4.333,-1.6667)
    percent_error_x = (abs(real[0] - calculated[0]) / calculated[0]) * 100
    percent_error_ct = (abs(real[1] - calculated[1]) / calculated[1]) * 100
    assert percent_error_x < 0.01 and percent_error_ct < 0.01


def test_lorentz_transformation_normal_case_2():
    """Testing the '_lorentz_transformation' function."""
    calculated = plt._lorentz_transformation((0,3), 0.3)
    real = (-0.943,3.145)
    percent_error_x = (abs(real[0] - calculated[0]) / calculated[0]) * 100
    percent_error_ct = (abs(real[1] - calculated[1]) / calculated[1]) * 100
    assert percent_error_x < 0.01 and percent_error_ct < 0.01


def test_lorentz_transformation_normal_case_3():
    """Testing the '_lorentz_transformation' function."""
    calculated = plt._lorentz_transformation((10,18), 0.0)
    real = (10,18)
    percent_error_x = (abs(real[0] - calculated[0]) / calculated[0]) * 100
    percent_error_ct = (abs(real[1] - calculated[1]) / calculated[1]) * 100
    assert percent_error_x < 0.01 and percent_error_ct < 0.01


def test_lorentz_transformation_bad_case_1():
    """Testing the '_lorentz_transformation' function with bad input."""
    with pytest.raises(Exception) as e_info:
        plt._lorentz_transformation((1,3), 1.5)