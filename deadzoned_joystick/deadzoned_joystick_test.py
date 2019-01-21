import unittest
import math

from deadzoned_joystick import is_in_deadzone as is_in_deadzone
from deadzoned_joystick import deadzone as deadzone
 
class DeadZonedTest(unittest.TestCase):
    def test_is_in_deadzone_1(self):
        self.assertEqual(is_in_deadzone(.2, (0,0)), True)
    def test_is_in_deadzone_2(self):
        self.assertEqual(is_in_deadzone(.2, (.2,.2)), False)
    def test_is_in_deadzone_3(self):
        self.assertEqual(is_in_deadzone(1, (0.5,0.03)), True)
    def test_is_in_deadzone_4(self):
        self.assertEqual(is_in_deadzone(1, (0.5,0.03)), True)

    # is on-the-circle considered in the zone?
    def test_is_in_deadzone_5(self):
        self.assertEqual(is_in_deadzone(.3, (0.3,0.0)), True)
    def test_is_in_deadzonel(self):
        self.assertEqual(is_in_deadzone(.3, (0.0,0.1)), True)
    
    # test the actual deadzone values.
    # anywhere in the zone should return (0,0)
    def test_deadzone_1(self):
        self.assertEqual(deadzone(1, (0.5,0.03)), (0,0))
    def test_deadzone1(self):
        self.assertEqual(deadzone(1, (0,1)), (0,0))

    # On the edge of the deadzone is (0,0)
    def test_deadzone_2(self):
        rad = .5
        side = rad/math.sqrt(2)
        self.assertEqual(deadzone(rad, (side,side)), (0,0))

    # Somewhere outside the zone, does it get scaled properly?
    def test_deadzone_3(self):
        zone = .4
        
        
        # .7 is halfway between .4 and 1, so it should scale to 50%, right?
        # Note: this may fail if the smath gives us 0.49999, so we might need
        # to permit some slop in the comparison.  Check unitest to see if
        # it has a special "assert" variant to permit small errors.
        # Otherwise we can subtract and look for something close to 0
        rad = .7
        side = rad/math.sqrt(2)
        (x,y) = deadzone(zone, (side, -side)) 
        self.assertAlmostEqual(x, 0.5, places = 1)
        self.assertAlmostEqual(y, -0.5, places= 1)
        
    def test_deadzone_4(self):
        
        # try a point in the negative space (to make sure signs are working)
        # This one should be halfway between .2 and 1, so should scale to .5
        # 
        zone = .2
        rad = .7
        side = rad/math.sqrt(2)
        (x,y) = deadzone(zone, (-side, -side))
        self.assertAlmostEqual(-x, -0.5, places= 1)
        self.assertAlmostEqual(-y, -0.5, places= 1)

    def test_deadzone_5(self):
        #
        # Make sure we don't divide by zero when on the Y axis.  (that would be bad)
        # This is one is a quarter of the way between the deadzone and 1, so should resolve
        # to 0.25
        # 
        zone = .6
        rad = .7
        self.assertEqual(deadzone(zone, (0, -rad)), (0, -0.25))


if __name__ == '__main__':
    unittest.main()
