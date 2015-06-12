'''
    This test module imports tests that come with pyfrc, and can be used

    to test basic functionaity of just about any robot.
'''

from pyfrc.tests import *
from subsystems import DriveTrain
import math
import itertools

def norm(vec_1):
	return math.sqrt(sum(e**2 for e in vec_1))

def magnitude_almost_equal(vec_1, vec_2):
	return abs(norm(vec_1)-norm(vec_2)) < 0.000001
def test_get_field_centric():
	dt = DriveTrain()

	x_range = [float(i)/10 for i in range(10)]
	y_range = [float(i)/10 for i in range(10)]
	t_range = range(360)

	for x, y, t in itertools.product(x_range, y_range, t_range):
		assert magnitude_almost_equal((x,y), (dt.get_field_centric(t, x, y)))







	