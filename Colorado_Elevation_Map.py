""" 
Colorado_Elevations.py
Brianna Brost
10/21/2022
The code reads elevation data from a file, finds the maximum elevation, and then draws a map using the elevation data. It also allows the user to click on the map to display the elevation at the clicked point. The program continues to run until a key is pressed.
"""
# set up canvas
import dudraw
dudraw.set_canvas_size(760,560)
dudraw.set_x_scale(0,760)
dudraw.set_y_scale(0,560)
elevations=[]
# read file
with open("CO_elevations_feet.txt", "r") as a_file:
    for line in a_file:
        elevations.insert(0, line.strip().split(" "))
#find max elevation
def max_elevation(a: list) -> int:
    """
    find max value of elevations
    Parameters: list of elevations
    Return: max value as int
    """
    max= 0
    for i in range(len(a)):
        for j in range (len(a[i])):
            a[i][j] = int(a[i][j])
        for element in a[i]:
            if element > max:
                max = element
    return max
max = max_elevation(elevations)
# print the things we were told to, good luck
print(elevations)
print(max)
clicked_elevation=0
def drawing()->None:
    """
    Draws pixels with color depending on elevation at point (couldnt get rectangles to actually print so had to use lines)
    Parameters: None
    Return: None
    """
    x=0
    y=0
    for i in range (len(elevations)):
        for j in range(len(elevations[i])):
            # color is fraction the elevation is of the max 
            color=int(255*(elevations[i][j])/max)
            dudraw.set_pen_color_rgb(color,color,color)
            # rectangles wouldnt print 
            dudraw.filled_square(x,y,1)
            # so i used lines and it worked
            # dudraw.line(j,i,j+1,i+1)
            x+=1
        y+=1
        x=0
    # puts box in bottom left and writes text
    dudraw.set_pen_color(dudraw.LIGHT_GRAY)
    dudraw.filled_rectangle(40,10,40,10)
    dudraw.set_pen_color(dudraw.DARK_BLUE)
    dudraw.text(25,10,"Elevation: ")
quit=False
# draws map
drawing()
while quit!=True:
    # when mouse pressed write elevation of where pressed in bottom left without reloading rest of drawing for sake of my computer
    if dudraw.mouse_is_pressed():
        x=int(dudraw.mouse_x())
        y=int(dudraw.mouse_y())
        clicked_elevation=elevations[y][x]
        dudraw.set_pen_color(dudraw.LIGHT_GRAY)
        dudraw.filled_rectangle(40,10,40,10)
        dudraw.set_pen_color(dudraw.DARK_BLUE)
        dudraw.text(25,10,("Elevation:"))
        dudraw.text(60,10, str(clicked_elevation))
#end when press key
    if dudraw.has_next_key_typed():
        quit=True
    dudraw.show(30)
