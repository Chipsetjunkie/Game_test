import simplegui
import random

numbers = range(8) + range(8)
random.shuffle(numbers)
Turns = 0
state = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
memory = [0,0]
count = 0
pre = 16

def new_game():
    global numbers,state,memory,count,pre
    random.shuffle(numbers)
    state = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    memory[0] = memory[1] = count = 0
    pre = 16

def mouse_handler(position):
    global state,count,memory,numbers,pre,Turns
    pos = abs(min(position[0]/50, (50-position[0])/50))
    while(pre != pos):
        pre = pos
        state[pos] = 1
        count += 1
        if count < 3:
           memory[count - 1] = pos
        else:
           Turns += 1 
           if numbers[memory[0]] != numbers[memory[1]]:
              state[memory[0]] = state[memory[1]] = 0  
              count = 1
              memory[count - 1] = pos 
           else:
              count = 1
              memory[count - 1] = pos      
                    
def cards(canvas):
    for i in range(17):
        if state[i] == 0:
            canvas.draw_polygon([(50*i, 0), (50+50*i,0),(50+50*i,100), (50*i,100)], 1,'Green','Red')
        else:
            canvas.draw_text(str(numbers[i]), ((25+50*i)-10,60), 35, 'White')
           

frame = simplegui.create_frame("My Game" ,800,100)
frame.set_mouseclick_handler(mouse_handler)
frame.set_draw_handler(cards)
frame.add_button("Reset", new_game)
label = frame.add_label(str(Turns))
frame.start()
