import turtle
import time
import random

turtle.tracer(0,0)
turtle.hideturtle()
snake_position= [(0,0),(20,0),(40,0),(60,0)]
width= turtle.window_width()
length= turtle.window_height()
food_coords_for_egg=[(random.randint(-width//2+10,width//2-10)) , (random.randint (-length//2+10,length//2-10))]
food_coords_for_ant=[length+200, width+100]
gameover= False
score= 0

def draw_frame():
   global snake_position
   global width
   global length
   global food_coords_for_egg
   global food_coords_for_ant
   turtle.clear()
   if len(food_coords_for_egg) != 0:
      turtle.penup()
      turtle.goto(food_coords_for_egg[0], food_coords_for_egg[1])
      turtle.pendown()
      turtle.color("green")
      turtle.dot(10)
   if len(food_coords_for_ant)!=0:
      turtle.penup()
      turtle.goto(food_coords_for_ant[0], food_coords_for_ant[1])
      turtle.pendown()
      turtle.color("green")
      turtle.stamp()
   #Drawing head
   turtle.up()
   turtle.goto(snake_position[0][0],snake_position[0][1])
   turtle.down()
   turtle.color("red")
   rectangle_head()
   #Drawing body
   for i in range(1,len(snake_position)):
      turtle.up()
      turtle.goto(snake_position[i][0],snake_position[i][1])
      turtle.down()
      turtle.color("black")
      rectangle_head()

def write_score():
   global score
   turtle.up()
   turtle.goto(-width+ 10,length/2 +10)
   turtle.down()
   turtle.write("SCORE:"+str(score), font=("Arial", 24, "normal"))


def whether_snake_eats():
   ##This function has two parts
   snake_head_x_coords= snake_position[0][0]
   snake_head_y_coords= snake_position[0][1]
   global score
   global file_obj
   ##This part checks if the snake has eaten the food, which is egg
   if len(food_coords_for_egg)!=0:
      if snake_head_x_coords-10 <= food_coords_for_egg[0] <= snake_head_x_coords+30 and snake_head_y_coords-10 <= food_coords_for_egg[1]<= snake_head_y_coords+30:
         score+=5
         if  snake_head_x_coords > food_coords_for_egg[0]:
            snake_position.append([snake_position[-1][0]+20,snake_position[-1][1]])
            food_position()
         elif snake_head_x_coords < food_coords_for_egg[0] and snake_head_y_coords+10 == food_coords_for_egg[1]:
            snake_position.append([snake_position[-1][0],snake_position[-1][1]])
            food_position()
         elif snake_head_x_coords < food_coords_for_egg[0] and snake_head_y_coords < food_coords_for_egg[1]:
            snake_position.append([snake_position[-1][0],snake_position[-1][1]])
            food_position()
         elif snake_head_x_coords < food_coords_for_egg[0] and  snake_head_y_coords>food_coords_for_egg[1]:
            snake_position.append([snake_position[-1][0],snake_position[-1][1]+20])
            food_position()
   ##This part checks if the snake has eaten the food, which is ant
   elif len(food_coords_for_ant)!=0:
      if snake_head_x_coords-30<=food_coords_for_ant[0]<=snake_head_x_coords+30 and snake_head_y_coords-30<=food_coords_for_ant[1]<=snake_head_y_coords+30:
         score+=10
         food_position()
         
def whether_snake_dies():
   snake_head_x_coords= snake_position[0][0]
   snake_head_y_coords= snake_position[0][1]
   global width
   global length
   global gameover
   global file_obj
   global score
   SumCheckx=0 #The SumCheckx variable sees if the snake touches itself horizontally
   SumChecky=0 #The SumCheckx variable sees if the snake touches itself vertically
   ##This function has two parts, the first for loop checks if the snake touches itself.
   for i in range(1,len(snake_position)):
         if (snake_head_x_coords+20==snake_position[i][0] and snake_head_y_coords==snake_position[i][1]):
             SumCheckx+=1
   for j in range(1,len(snake_position)):
         if (snake_head_x_coords-20==snake_position[j][0] and snake_head_y_coords==snake_position[j][1]):
             SumCheckx+=1
   if SumCheckx==2:
      gameover=True
      print("You lose! Your score is", score)
   for k in range(1,len(snake_position)):
         if (snake_head_y_coords+20==snake_position[k][1] and snake_head_x_coords==snake_position[k][0]):
             SumChecky+=1
   for l in range(1,len(snake_position)):
         if (snake_head_y_coords-20==snake_position[l][1] and snake_head_x_coords==snake_position[l][0]):
             SumChecky+=1
   if SumChecky==2:
      gameover=True
      print("You lose! Your score is", score)
      
   ##The second part of the function checks if the snake touches the border, thereby ending the game
   if snake_head_x_coords+20==(width) or snake_head_x_coords==(-width): #or snake_head_y_coords-20==(length-325) or snake_head_y_coords==(-length+325):
         gameover=True
         print("You lose! Your score is", score)

def food_position():
   global food_coords_for_egg
   global food_coords_for_ant
   global width
   global length
   whether_egg_or_ant= random.randint(0,1)
   if whether_egg_or_ant == 0:
      """
      The position of food is set so that it always remains inside of the border, otherwise snake will have
      to touch the border in order to eat the food and it will die
      """
      ##when food is egg
      x_food= random.randint(-width//2+50, width//2-50)
      y_food= random.randint (-length//2+50, length//2-50)
      food_coords_for_egg=[]
      food_coords_for_egg.append(x_food)
      food_coords_for_egg.append(y_food)
      food_coords_for_ant=[]
      
   if whether_egg_or_ant == 1:       ## When food is ant
      x_food= random.randint(-width//2+50, width//2-50)
      y_food= random.randint (-length//2+50, length//2-50)
      food_coords_for_ant=[]
      food_coords_for_ant.append(x_food)
      food_coords_for_ant.append(y_food)
      food_coords_for_egg=[]
      
   
def rectangle_head():
   ##This function just draws all the snake bodies
   turtle.width(3)
   turtle.forward(20)
   turtle.left(90)
   turtle.forward(20)
   turtle.left(90)
   turtle.forward(20)
   turtle.left(90)
   turtle.forward(20)
   turtle.left(90)
   
   
def snake_head_move_right():
   ##This function decides what happens when the user presses the right arrow key
   global snake_position
   head_xcoord=snake_position[0][0]
   body_x_coord= snake_position[1][0]
   if not head_xcoord < body_x_coord:
      for i in range(-1,-len(snake_position),-1):
         snake_position[i]= snake_position[i-1]
      head_pos=snake_position.pop(0)
      head_pos_new= [head_pos[0]+20,head_pos[1]]
      snake_position.insert(0,head_pos_new)

   
def snake_head_move_left():
   ##This function decides what happens when the user presses the left arrow key
   global snake_position
   head_xcoord=snake_position[0][0]
   body_x_coord=snake_position[1][0]
   if not head_xcoord > body_x_coord:
      for i in range(-1,-len(snake_position),-1):
         snake_position[i]= snake_position[i-1]
      head_pos=snake_position.pop(0)
      head_pos_new= [head_pos[0]-20,head_pos[1]]
      snake_position.insert(0,head_pos_new)

   
def snake_head_move_down():
   ##This function decides what happens when the user presses the down arrow key
   global snake_position
   head_ycoord=snake_position[0][1]
   body_ycoord=snake_position[1][1]
   if not head_ycoord > body_ycoord:
      for i in range(-1,-len(snake_position),-1):
         snake_position[i]=snake_position[i-1]
      head_pos=snake_position.pop(0)
      head_pos_new= [head_pos[0],head_pos[1]-20]
      snake_position.insert(0,head_pos_new)
 

def snake_head_move_up():
   ####This function decides what happens when the user presses the up arrow key
   global snake_position
   head_ycoord=snake_position[0][1]
   body_ycoord=snake_position[1][1]
   if not head_ycoord < body_ycoord:
      for i in range(-1,-len(snake_position),-1):
         snake_position[i]= snake_position[i-1]
      head_pos=snake_position.pop(0)
      head_pos_new= [head_pos[0],head_pos[1]+20]
      snake_position.insert(0,head_pos_new)
   
      
   
def main():
   global gameover
   turtle.tracer(0,0)
   turtle.hideturtle()
   turtle.onkey(snake_head_move_left, "Left")
   turtle.onkey(snake_head_move_right, "Right")
   turtle.onkey(snake_head_move_up, "Up")
   turtle.onkey(snake_head_move_down, "Down")
   turtle.listen()
   #reset()
   while not gameover:
        turtle.clear()
        whether_snake_dies()
        whether_snake_eats()
        draw_frame()
        write_score()
        turtle.update()
        time.sleep(0.05)


main()
food_position()






