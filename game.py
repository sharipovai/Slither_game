# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import tkinter as tk
import time
import tkinter.messagebox as mb
import random as rd
from datetime import timedelta, datetime

def score_field():
    global size,top_boarder
    canvas.create_rectangle(0,0,size,top_boarder, outline="black")
    canvas.create_text(10, 15, anchor="w", text="Score:     "+ str(len(snake1.coord_list)))
    canvas.create_text(400, 15, anchor="w", text="Time:     "+ str(datetime.now()-start_time)[:-7])

class Snake:
    
    def __init__(self, start_coord, length, width):
        self.coord_list = [] 
        self.step_x = 0
        self.step_y = 0
        self.flag_change=False
        for i in range(0, length, 2):
            snake_section = [start_coord + i, start_coord, start_coord + width + i, start_coord + width]
            self.coord_list.append(snake_section)
        

    def draw(self):
        color = "green"
        for i in range(len(self.coord_list)-1,-1,-1):
            if i==0:
                color = "black"
            canvas.create_rectangle(self.coord_list[i][0], self.coord_list[i][1], 
                                    self.coord_list[i][2], self.coord_list[i][3], 
                                    outline=color, fill="green")
                
    def change_coord(self, food):
        
        if self.step_x+self.step_y != 0:
            for i in range(len(self.coord_list)-1,0,-1):
                for j in range(4):
                    self.coord_list[i][j] = self.coord_list[i-1][j]  
            self.coord_list[0][0] += self.step_x
            self.coord_list[0][2] += self.step_x
            self.coord_list[0][1] += self.step_y
            self.coord_list[0][3] += self.step_y
        
     
        self.eating(food)

        
    def change_step(self, event, step_x, step_y):
        if self.flag_change==False:
            
            if self.step_y==0 and step_x == 0:
               self.step_y = step_y
               self.step_x = step_x
    
            if self.step_x==0 and step_y == 0 :
                self.step_x = step_x
                self.step_y = step_y
            self.flag_change=True
        
            
    def eating(self, food):
        if intersection(self.coord_list[0], food.food_coord):
            food.change_food()
            food.draw()
            step_x = self.coord_list[-1][0]-self.coord_list[-2][0]
            step_y = self.coord_list[-1][1]-self.coord_list[-2][1]
            for j in range(0, 10, 2):
                self.coord_list.append([self.coord_list[-1][i] + step_x if i % 2 == 0 else self.coord_list[-1][i] + step_y for i in range(len(self.coord_list[-1]))])
            #global timesleep
            #timesleep*=0.8
    
    def not_game_over(self):
        for i in range(len(self.coord_list[0])):
            if (i%2==0 and self.coord_list[0][i]<0) or (i%2==1 and self.coord_list[0][i]<top_boarder) or self.coord_list[0][i]>size:
                return False
        for part1 in self.coord_list[50:]:
            if intersection(self.coord_list[0], part1):
                return False
        return True
                
def intersection(list1, list2):
    flag_x =False
    flag_y = False
    if list2[0] <= list1[0] <= list2[2] or list2[0] <= list1[2] <= list2[2]:
        flag_x = True
    if list2[1] <= list1[1] <= list2[3] or list2[1] <= list1[3] <= list2[3]:
        flag_y = True   
    if flag_x and flag_y:
        return True
    else:
        return False
                
class Food:
    
    food_coord=[200, 300, 220, 320]
    
    def __init__(self):
        pass
    
    def draw(self):
        canvas.create_rectangle(self.food_coord[0], self.food_coord[1], 
                                    self.food_coord[2], self.food_coord[3], 
                                    outline="black", fill="red")
    
    def change_food(self):
        food_x = rd.randint(0, 580)
        food_y = rd.randint(top_boarder, 580)
        self.food_coord = [food_x, food_y, food_x+20, food_y+20]
        

            
window = tk.Tk()
window.geometry('600x600')
window.title("Snake")
#window.iconbitmap('logo.ico')
size = 600
top_boarder=40
timesleep=0.006
canvas = tk.Canvas(window, width=size, height=size)
canvas.pack()

start_time=datetime.now()
snake1 = Snake(300,40,20)
food = Food()


while snake1.not_game_over():
    canvas.delete("all")
    snake1.flag_change=False
    snake1.draw()
    food.draw()
    score_field()
    window.update_idletasks()
    window.update()
    window.bind('<KeyRelease-Left>',lambda e, step_x=-2, step_y=0: 
            snake1.change_step(e,step_x, step_y))
    window.bind('<KeyRelease-Right>',lambda e, step_x=2, step_y=0: 
            snake1.change_step(e,step_x, step_y))
    window.bind('<KeyRelease-Up>',lambda e, step_x=0, step_y=-2: 
            snake1.change_step(e,step_x, step_y))
    window.bind('<KeyRelease-Down>',lambda e, step_x=0, step_y=2: 
            snake1.change_step(e,step_x, step_y))
    snake1.change_coord(food)
    time.sleep(timesleep)  


message = "Ваш результат " + str(len(snake1.coord_list))
mb.showwarning("Game over", message)
window.destroy()

#window.mainloop()
#mb.showwarning("Предупреждение", step_x)

  
    



