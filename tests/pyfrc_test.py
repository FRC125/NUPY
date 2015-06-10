'''
    This test module imports tests that come with pyfrc, and can be used
    to test basic functionaity of just about any robot.
'''

from pyfrc.tests import *
from subsystems import DriveTrain
import math

def norm(vec_1):
	return math.sqrt(sum(e**2 for e in vec_1))

def almost_equal(vec_1, vec_2):
	return abs(norm(vec_1)-norm(vec_2)) < 0.000001
def test_get_field_centric():
	dt = DriveTrain()

	assert dt.get_field_centric(0, 0, 0) == (0,0)
	assert dt.get_field_centric(0, 1, 0) == (1,0)
	assert dt.get_field_centric(0, 0, 1) == (0,1)
	assert almost_equal(dt.get_field_centric(360, 1, 0), (1,0))
	assert almost_equal(dt.get_field_centric(360, 0, 1), (0,1))
	assert almost_equal(dt.get_field_centric(180, 1, 0), (-1,0))
	assert almost_equal(dt.get_field_centric(180, 0, 1), (0,-1))
	assert almost_equal(dt.get_field_centric(90, 1, 0), (0,1))
	assert almost_equal(dt.get_field_centric(45, 1, 0), (0.7071067812, 0.7071067812))
	assert almost_equal(dt.get_field_centric(135, 1, 0), (-0.7071067812, 0.7071067812))


