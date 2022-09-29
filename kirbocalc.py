
# title: Calcultor
# author: ME spencer kirby
# special thanks to owen receer for miner bug fixes and MAJOR help on turtle 
# description: simple graphing calculator 
import math , turtle , string, filename
screenWidth = 600 # screen width 
screenHeight = 400 
first_num= 0.0
second_num=0.0 
equations = [0]
A_value=0.0
F_value=0.0
B_value=0.0
C_value=0.0
D_value=0.0
E_value=0.0
low_value = 0.0
x = 0.0
answer=0.0
answer1=0.0 #lines 9- 19 just make variables 
operation = int(input("chose operation addition=1 subraction=2 multaplication=3 division=4 solving quadratic for x incept=5 solving quadratics for midpoint=6 solving quadratic for vertex 7 exponets=8 solving for x in absolute value problems  =9 solve for all vertexes=10 find the inverse of a equation "))#this is where they imput what function they want 
mode = int (input("do u want that graphed 0 No just ansers 1 just graph 2 both "))#ask them if they want that graphed 
if mode == 1 or 2:
    step = float (long (input("input step only aplicable if graphing ")))
if int(operation) < 5: 
    first_num = float(input("first num PLS use decimal instead of fraction.")) 
    second_num =  float(input("secod num num PLS use decimal instead of fraction.")) #takes the first num and second num for +-*/ operations 
elif operation < 8 : 
    A_value =  float(input("insert A value with format Ax^2+bx+c PLS use decimal instead of fraction"))
    B_value =  float(input("insert B value with format Ax^2+bx+c PLS use decimal instead of fraction"))
    C_value =  float(input("insert C value with format Ax^2+bx+c PLS use decimal instead of fraction"))#takes the values of parts of normal quadratics in a form we can work with 
elif operation == 9:
    A_value = float(input("insert A value with format A|Bx^2+Cx+D|+E+fx+gX^2  PLS use decimals instead of fractions "))
    B_value = float(input("insert B value with format A|Bx^2+Cx+D|+E+fx+gX^2  PLS use decimals instead of fractions "))
    C_value = float(input("insert C value with format A|Bx^2+Cx+D|+E+fX+gX^2  PLS use decimals instead of fractions "))
    D_value = float(input("insert D value with format A|Bx^2+Cx+D|+E+fX+gX^2  PLS use decimals instead of fractions "))
    E_value = float(input("insert E value with format A|Bx^2+Cx+D|+E+fX+gX^2  PLS use decimals instead of fractions "))
    F_value = float(input("insert F value with format A|Bx^2+Cx+D|+E+fX+gX^2  PLS use decimals instead of fractions "))
    G_value = float(input("insert G value with format A|Bx^2+Cx+D|+E+fX+gX^2  PLS use decimals instead of fractions "))#I do not know standard form for this and i dont think it exists so i just took it in variables 
    B_value = B_value * A_value 
    C_value = C_value * A_value 
    D_value = D_value * A_value #i distributed A_value because I can factor it out latter without messing with prime factorization 
elif operation == 10:
    A_value =  float(input("insert A value with format Ax^D+bx+c PLS use decimal instead of fraction"))
    B_value =  float(input("insert B value with format Ax^D+bx+c PLS use decimal instead of fraction"))
    C_value =  float(input("insert C value with format Ax^D+bx+c PLS use decimal instead of fraction"))#takes the values of parts of normal quadratics in a form we can work with 
    D_value =  float(input("insert C value with format Ax^D+bx+c PLS use decimal instead of fraction"))#takes the values of parts of normal quadratics in a form we can work with 
if operation == 9:
    first_num = float(input("number left of the ^ thing "))
    second_num = float(input("number right of the ^ thing "))#these just take what you want for the problem and solve and then print  thats from 40- 53 do that 
    answer = pow(first_num , second_num)
if operation == 1:
    answer = first_num + second_num
if operation == 2:
    answer = first_num - second_num
if operation == 3:
    answer = first_num * second_num 
if operation == 4: 
    answer = first_num / second_num
if operation == 1 or 2 or 3 or 4 or 9:
    equations = [ 
        lambda x:answer] # take stuff for graph 
if operation == 5 or 6 or 7 and mode == 1 or 2 :
    equations = lambda x: (A_value) * pow(x , 2) + (B_value)*x+ (C_value) #set the equation which is going to be graphed 
if operation == 5 or 6 or 7:
    if B_value ** 2 > 4 * A_value * C_value:
        first_num = (-1 * B_value - pow ((B_value ** 2 - 4*A_value*C_value)  ,.5))/(2 * A_value )
        second_num = (-1 * B_value + pow ((B_value ** 2 - 4*A_value*C_value), .5))/(2* A_value )
if operation == 5 or 6 or 7 and pow (B_value , 2) < 4*A_value*C_value:
    print("no X incept ")
elif operation > 4 and operation != 8 and first_num == second_num:#if the values are the same It prints there is 1 x- incept 
    print ("1 X intercept")
if operation == 6:
    answer = (first_num+second_num)/2
if operation == 7 :
    answer = (first_num+second_num)/2
    answer1 = pow((A_value * answer) ,2)+B_value * answer+ C_value #Lines64-54 are just math 
if operation == 5 and  B_value*B_value > 4*A_value*C_value and  mode == 0 or 2 :
    print(first_num )
    print(second_num)
if operation == 7 or operation == 9 and mode == 0 or 2 :
    print (answer1) #lines 65-70 just print ansers 
    def inout(self, x):  
        try:
            self.vairbale = self.equation(float(x)) 
            if math.isnan(float(self.vairbale)): return "NaN" 
            else: return self.vairbale 
        except: return "Bad Input L+Bad+Ratio" 
if mode == 1 or mode == 2:
  graphers = [] 
  turtleColors = ["#FF6347", "#FF8C00", "#FFD700", "#7CFC00", "#00FA9A", "#00CED1", "#6495ED", "#9370DB", "#DA70D6"] # 
  class Graph:
    def __init__(self, color, equation, mode, dotsize, graphLine, width, height, dot):
        self.equation = equation # Set the equation function
        self.ycor = 0.0 # Define the variable for later
        self.nan = False # Define the variable for later
        self.lineSize = dotsize # Define the variable for later
        self.lod = dot
        if mode == 1 or mode == 2 or mode == 3: # Define turtle if mode is 1 or 2
            self.turtle = turtle.Turtle() # Turtle object
            self.turtle.pu() # Pen up
            self.turtle.pensize(self.lineSize) # Pen size
            self.turtle.speed(0) # Maximum speed infinity
            if graphLine == True: # Graph the x andy axis lines
                self.turtle.color("#FFFFFF") # Color white
                self.turtle.goto(0 - width / 2, 0) # Goto one side
                self.turtle.pd() # Pendown
                self.turtle.goto(width / 2, 0) # Goto other side
                self.turtle.pu() # Penup
                self.turtle.goto(0, 0 - height / 2) # Goto the bottom
                self.turtle.pd() # Pendown
                self.turtle.goto(0, height / 2) # Goto the top
                self.turtle.pu() # Penup
            self.turtle.color(color) 
if mode == 1 or mode == 2: 

    screen = turtle.Screen() 
    screen.setup(screenWidth, screenHeight) 
    screen.bgcolor("#333333") # defines color
    screen.tracer(0)
if mode == 1 or mode == 2:
    x = 0 - (screenWidth / 2) 
if mode == 0 or mode == 2:#all of the lines 73- 101 just do graphing stuff 
    while True: #repeat forever 
        x = float (input("What x value do you want to solve for pls use decimals fractions are dumb ")) 
        if x != 0:
          print (A_value*x ** 2+B_value * x + C_value )

    
    
    
