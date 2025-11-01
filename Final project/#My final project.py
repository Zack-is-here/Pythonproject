#My final project
#By Zack
#Last Edit:August 27

from guizero import App, Text, PushButton, Combo, Box, Window, Picture
import random
import time

app = App("Color Reaction Game", width=400, height=200)
colors = ["red", "green", "blue", "yellow", "purple"]    #These are colors game will use.
false_color = {"Easy": 0.0, "Medium": 0.5, "Hard": 0.8 } #Chance user will get a wrong color.
wait_range = (1000, 5000)                                #The Time user will wait.
 



game_window = None                                       #Game Window close. 
target_color = ""
now_difficulty = "Easy"                                  #Level now is Easy.
wait_for_color = False                                   #User can't click at this time
start_time = 0


Text(app, text="Select a level:", size=15)
difficulty = Combo(app, options=["Easy", "Medium", "Hard"], selected="Easy")

def launch_game():
    global now_difficulty
    now_difficulty = difficulty.value
    target_text.value = ""                               #When game start, the color, time and result will be none.
    time_text.value = ""
    result_text.value = ""
    game_window.show()
    app.hide()


intr_window = Window(app, title="About Reaction Speed", width=550, height=400)
intr_window.hide()
                                                         #The introduction of reaction

Text(intr_window, text="Introduction to reaction speed", size=16)
Text(intr_window, text=(
    "We all have a measurable reaction time.\n"
    "The average reaction time to visual stimulus is around 250 milliseconds,\n"
    "and most people seem to be hard capped at around 190-200 ms with training."
), size=12)
picture=Picture(intr_window, image="download.gif")


def close_intr():
    intr_window.hide()                                   #CLose introduction
    app.show()

PushButton(intr_window, text="Back to menu", command=close_intr)

def open_intr():
    app.hide()                                           #Open introduction
    intr_window.show()

PushButton(app, text="Introduction to reaction speed", command=open_intr)
PushButton(app, text="Start The Game", command=launch_game) 
                                                         #Click to start the game


game_window = Window(app, title="Reaction Game", width=400, height=300)
game_window.bg = "white"                                 #background = white
game_window.hide()                                       #Hide it till user start.

Text(game_window, text="Click the button at a correct time!", size=12, color="gray")
target_text = Text(game_window, text="", size=14)
bg_box = Box(game_window, width="fill", height=120)      #Set what will text and background color
bg_box.bg = "white"
time_text = Text(game_window, text="", size=12)          #This spot will text different things, depends on what user do.
result_text = Text(game_window, text="", size=12, color="black")


def easy_color():
    global wait_for_color, start_time
    bg_box.bg = "green"
    wait_for_color = True
    start_time = time.time()                             #For easy mode to use
    time_text.value = "Click now!"



def start_round():
    global the_color, wait_for_color, start_time
    result_text.value = ""
    time_text.value = "Get ready"
    bg_box.bg = "white"                                  #These are what system will do.
    wait_for_color = False
    start_time = 0
    if now_difficulty == "Easy":                         #In easy mode, wait a random time and show green
        wait = random.randint(*wait_range)
        game_window.after(wait, easy_color)
    else:
        the_color = random.choice(colors)                #For Medium and hard mode, show a random color after a random time.Tell user what they should click.
        target_text.value = f"Click when background is: {the_color.upper()}"
        next_color()


def next_color():
    time_W = random.randint(800, 2000)                   #Range of time user will wait.
    game_window.after(time_W, show_color_chance)

def show_color_chance():
    global wait_for_color, start_time

    is_fake = random.random() < false_color[now_difficulty] #If the number computer choose is smaller than 0.5(medium), 0.8(hard), it will show a fake color.
    if is_fake:
        fake_choice = []                                 #A list that will add fake color in.
        for color in colors:                             #For every color, if it is fake, put it into the list
            if color != the_color:
                fake_choice.append(color)
        chosen_color = random.choice(fake_choice)        #Choose a fake color randomly
        bg_box.bg = chosen_color                         #Make the background to that fake color
        time_text.value = "Wait..."
        wait_for_color = False                           #Click at this time will fail
        next_color()
    else:
        bg_box.bg = the_color                            #when the number is bigger, it show the real color
        time_text.value = "Click now!"
        wait_for_color = True                            #Click at this time won't fail
        start_time = time.time()

def on_click():
    global wait_for_color, start_time

    if not wait_for_color:                               #User clicked too early
        result_text.value = "Wrong! You clicked at the wrong time."
        return



    reaction_time = time.time() - start_time
    ms = int(reaction_time * 1000)                       #It caculate how fast user clicked(the result)
    result_text.value = f"Your Reaction Time: {ms} ms"
    wait_for_color = False                               #User can't click now
    start_time = 0




def back_menu():
    target_text.value = ""
    time_text.value = ""
    result_text.value = ""
    bg_box.bg = "white"                                 #Set everything to none and hide the game window, show the main menu
    game_window.hide()
    app.show()


b_box = Box(game_window, layout="grid", align="bottom")                #Buttons
PushButton(b_box, text="Start", command=start_round, grid=[0, 0])
PushButton(b_box, text="Click", command=on_click, grid=[1, 0])     
PushButton(b_box, text="Main Menu", command=back_menu, grid=[2, 0])



app.display()