"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Huiruo Zou.
"""
########################################################################
# DONE: 1.
# On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# DONE: 2.
#
#  You should have RUN the PREVIOUS module and READ its code.
#  (Do so now if you have not already done so.)
#
#  Below this comment, add ANY CODE THAT YOUR WANT, as long as:
#    1. You construct at least 2 rg.SimpleTurtle objects.
#    2. Each rg.SimpleTurtle object draws something
#         (by moving, using its rg.Pen).  ANYTHING is fine!
#    3. Each rg.SimpleTurtle moves inside a LOOP.
#
#  Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#  If you make syntax (notational) errors, no worries -- get help
#  fixing them at either this session OR at the NEXT session.
#
#  Don't forget to COMMIT your work by using  VCS ~ Commit and Push.
########################################################################
import rosegraphics as rg

window = rg.TurtleWindow()

apple = rg.SimpleTurtle('turtle')
apple.pen = rg.Pen('red', 3)
apple.speed = 5

orange = rg.SimpleTurtle()
orange.pen = rg.Pen('orange',6)
orange.speed = 5
path=50

for k in range(5):
    apple.right(136)
    apple.forward(100)

    orange.draw_circle(path)
    orange.pen_up()
    orange.right(45)
    orange.forward(10)
    orange.left(45)

    orange.pen_down()
    path = path+15


window.close_on_mouse_click()
