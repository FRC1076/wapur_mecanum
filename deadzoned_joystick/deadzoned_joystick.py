import math
def is_in_deadzone(radius, location):
    (x,y) = location
    """
    #if in the function is in deadzone it will return true.
    #if the function is outside of the deadzone the function will return false.
    """
    return(x**2+y**2) <= (radius**2)
    
    
def deadzone(radius, location):
    """
    # if in the deazone this function will return 0,0.
    """
    (x,y) = location
    if is_in_deadzone(radius, location):
      
        return(0,0)
    elif location[0] == 0:
        """
        # if x is zero this function will just y without mutiplying or divideing by 0.
        """
        if y < 0:
            ny = (y + radius)/(1-radius)
        else:   
            ny = (y - radius)/(1 - radius)
        ny = round(ny, 2)
        return(0,ny)
        # convert on axis

        
    else:
        """
        # Rescales the x and the y values for the deadzone.
        will turn the x and y to polar cordinates and rescale then then turn them back into the rescaled cartesian coordinates.
        """
        i = (x**2+y**2)
        r = (math.sqrt(i))
        theta = (math.atan(x/y))
        k =(r-radius)/(1-radius)
        nx = (r*math.cos(theta))
        nx = round(nx, 2)
        ny = (r*math.sin(theta))
        ny = round(ny, 2)
        return(nx,ny)
    
    #y = 2.6666
    #x = round(y, 1)
    #print(x)
