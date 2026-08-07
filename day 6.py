#Reeborg's world- maze escape exercise (reeborg.ca). Functions are provided by reeborg simulator, not standard python.

def turn_around():
    turn_left()
    turn_left()
def move_right():
    turn_left()
    turn_around()
while front_is_clear():
    move()
turn_left()
while not at_goal():
   if right_is_clear():
       move_right()
       move()
   elif front_is_clear():
       move()
   else:
       turn_left()