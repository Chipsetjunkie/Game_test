import simplegui
import random

pos = [250,250]
vel = [0,0]
r = 20
size = [500,500]
pad_vel = [0,0]
pad_velR = [0,0]
padpos  = [200,300]
padposR  = [200,300]
score = [0,0]
    
def restart():
    global pos,score
    score = [0,0]
    pos = [250,250]    
    vel[0] = -1
    vel[1] = random.choice([0.75,-0.75])


def Circle(canvas):
 
    # draw mid line and gutters
    canvas.draw_line([size[0] / 2, 0],[size[0] / 2, size[0]], 1, "White")
    canvas.draw_line([5, 0],[5, size[0]], 1, "White")
    canvas.draw_line([size[0] - 5, 0],[size[0] - 5, size[0]], 1, "White")

    update()
    canvas.draw_circle(pos,r,2,'White','White')
    canvas.draw_line((0, padpos[0]), (0, padpos[1]),10 , 'Red')
    canvas.draw_line((500, padposR[0]), (500, padposR[1]),10 , 'Red')
    canvas.draw_text(str(score[0]),(200,50),45 ,'White')
    canvas.draw_text(str(score[1]),(300,50),45 ,'White')
    

def bordercheck():
    #Ball border
    if pos[1] < r or pos[1] > size[1]-r:
        vel[1] = vel[1]*-1
    #Paddle border
    if padpos[0] == 0 or padpos[0] == 400:
             pad_vel[0] = 0
    if padposR[0] == 0 or padposR[0] == 400:        
             pad_velR[0] = 0
    #Paddle Reflection
    if pos[0] < 25 and padpos[0]< pos[1] < padpos[1]:
        vel[0] = (vel[0]-1)*-1 
    if pos[0]+vel[0] > 475  and padposR[0]< pos[1] < padposR[1]: 
        vel[0] = (vel[0]+1)*-1   
            
def collisioncheck():
    global pos
    if pos[0] < r:  
       pos = [250,250]
       vel[0] = 1
       vel[1] = random.choice([0.75,-0.75])
       Score('Left') 
     
    elif pos[0] > size[0]-r:
          pos = [250,250]
          vel[0] = -1
          vel[1] = random.choice([0.75,-0.75])  
          Score('Right')   
            
def Keydown(key):
    if key == simplegui.KEY_MAP['w']:
        pad_vel[0] += 10
    if key == simplegui.KEY_MAP['s']:
        pad_vel[0] -= 10
    if key == simplegui.KEY_MAP['up']:
        pad_velR[0] += 10
    if key == simplegui.KEY_MAP['down']:
        pad_velR[0] -= 10    
     
        

def Keyup(key):
    global pad_vel,pad_velR
    pad_vel = [0,0]
    pad_velR = [0,0]
    
def Score(side):
    if side == 'Left':
        score[1] += 1
    
    elif side == 'Right':
        score[0] += 1        
               
def update():
    pos[0] += vel[0]
    pos[1] += vel[1]
    padpos[0] -= pad_vel[0]
    padpos[1] -= pad_vel[0]
    padposR[0] -= pad_velR[0]
    padposR[1] -= pad_velR[0]
    bordercheck()
    collisioncheck()
        

# create frame
frame = simplegui.create_frame("Pong", size[0], size[0])
frame.set_draw_handler(Circle)
frame.set_keydown_handler(Keydown)
frame.set_keyup_handler(Keyup)
buton1 = frame.add_button('Restart',restart)


# start frame
frame.start()
restart()
