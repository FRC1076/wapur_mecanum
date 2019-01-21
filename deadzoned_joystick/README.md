The function of a joystick deadzone is to filter
out the controller noise when the joystick is
hands-off.

A dead zone is defined as a circle of a certain radius.
If the joystick values indicate a position inside this
circle, then the value (0,0), should be returned.

Otherwise a scaled value between 0 and 1 (or 0 and -1)
is to be returned.    The scaling is done so that the
joystick has continuous increase in the readings from
the border of the deadzone to the maximum value.

For the first part, we need a function that tells us if a
point is inside the deadzone or not. That will guide
what we return.

If you pass the first unit test, write a bunch more unit
tests that ensure that your function works for several
different sized deadzones, etc...

