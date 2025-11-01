
#TheProject

from guizero import App, Text, PushButton, Picture, Box, Window, ButtonGroup

from guizero import *
import pygame
app = App("The Introduction of My Hometown")


pygame.mixer.init()
music_file = "Minecraft.mp3" 

def play_music():
    pygame.mixer.music.load(music_file)
    pygame.mixer.music.play()

text=Text(app, "About WenZhou. Click the picture to read more!")

click = [False] * 6         
already_show = False                         #make a list that include six "false" 
open_window = []             

def check_all_and_closed():
    global already_show
    if all(click) and not open_window and not already_show:      #if all the windows have benn opened and closed, and the q_win have not opened yet, show the question window.
        already_show = True
        show_question_window()

def close_and_check(window):
    open_window.remove(window)               #once user closed the window, it will close and hide the window.
    window.hide()
    check_all_and_closed()


def show_question_window():
    q_win = Window(app, title="Quiz Time!", width=600, height=600)
    Text(q_win, text="You've clicked all the pictures!\nNow answer these questions:")

    Text(q_win, text="1. What kind of animal was discovered in the Oujiang River?")
    q1 = ButtonGroup(q_win,
        options=[
            ["Crab", "Crab"],
            ["Bird", "Bird"],
            ["Fish", "Fish"],                    #the question part.
            ["JellyFish", "Jellyfish"],
            ["Submarine", "Submarine"]
        ],
        selected="Crab", horizontal=False)

    Text(q_win, text="2. What is the main peak of Yandang Mountain?")
    q2 = ButtonGroup(q_win,
        options=[
            ["Baigangjian", "Baigangjian"],
            ["Huashan", "Huashan"],
            ["Everest", "Everest"]
        ],
        selected="Baigangjian", horizontal=False)

    Text(q_win, text="3. Which dynasty was Liu Ji active in?")
    q3 = ButtonGroup(q_win,
        options=[
            ["Tang", "Tang"],
            ["Song", "Song"],
            ["Yuan and Ming", "Yuan and Ming"],
            ["Now", "Now"]
        ],
        selected="Tang", horizontal=False)

    def check_answers():
        correct = 0

        if q1.value == "Fish":
            correct += 1
        if q2.value == "Baigangjian":
            correct += 1
        if q3.value == "Yuan and Ming":
            correct += 1

        if correct == 3:
            Text(q_win, text="All correct! Well done!")
            Picture(q_win, image="QFish.gif", align="bottom")
        else:
            Text(q_win, text="You got " + str(correct) + "/3 correct. Try again!")     #caculate the final score

    PushButton(q_win, text="Check my answer", command=check_answers)


def info_DongTa():
    window = Window(app, title="About East Pagoda", width=740, height=300)
    Text(window, text="""The Yueqing East Pagoda, located atop Donggao Mountain in Yueqing City, Wenzhou City,
Zhejiang Province, is a relic of ancient architecture from the Song Dynasty. Built during the Song Dynasty
 (1068-1077), the Yueqing East Pagoda stands approximately 18 meters tall. 
Numerous inscriptions adorn the bricks of the pagoda, revealing its rich history, 
scientific significance, and artistic value.""", width=80)
    Picture(window, image="DongTa2.gif", align="left")
    Picture(window, image="China.gif", align="right")

    open_window.append(window)
                                                #The button part. All these will show on the window that user opened.
    def on_close():
        close_and_check(window)                 #Turn the "False" to "True" and remove this window when user close the window.
    window.when_closed = on_close

def info_Liu():
    window = Window(app, title="About Liu Ji", width=800, height=300)
    Text(window, text="""Liu Ji (1 July 1311 - 16 May 1375), better known as Liu Bowen,
was a Chinese military strategist, philosopher, and politician who lived in the late Yuan and early Ming dynasties. 
He was born in Wencheng County, Wenzhou, Zhejiang. He served as a key advisor to Zhu Yuanzhang, 
the Emperor, also the founder of the Ming dynasty, in the latter's struggle to overthrow the Yuan dynasty 
and unify China under his rule.""")
    Picture(window, image="LiuJi.gif", align="left")
    Picture(window, image="Ming.gif", align="left")
    Text(window, text="<---(The Ming Empire)", align="left")

    open_window.append(window)

    def on_close():
        close_and_check(window)                 #Same as the first one
    window.when_closed = on_close

def info_Yandangshan():
    window = Window(app, title="About Yandang Mountain", width=650, height=300)
    Text(window, text="""Yandang Mountain is located in Yueqing, north of Wenzhou City,
     It rises 500 to 600 meters southeast of the Yangtze River, with its main peak, Baigangjian, 
    at 1,108 meters. It is designated a World Geopark and 
    a National 5A Tourist Attraction.""")
    Picture(window, image="YandangshanA.gif", align="left")
    Picture(window, image="YandangshanB.gif", align="left")

    open_window.append(window)

    def on_close():
        close_and_check(window)
    window.when_closed = on_close               #Same

def info_Ojiang():
    window = Window(app, title="About Oujiang River", width=800, height=300)
    Text(window, text="""The Ou River is the second-largest river in the Zhejiang province of eastern China.
    The river flows 388 kilometers  before finally reaching the city of Wenzhou and emptying into the East China Sea.
    The natural environment in the basin is well protected and has huge reserves of natural resources, 
    making it a good tourist destination.Also, Oujiang River has a species that is unique in the world -
    The Oujiang minnow.This is a small fish that usually lives in the middle and lower reaches of rivers. 
    It hides in deeper waters during the day and swims to shallower waters in the evening to find food.""", width=80)
    Picture(window, image="OjiangA.gif", align="left")
    Picture(window, image="OjiangB.gif", align="left")
    Picture(window, image="Fish.gif", align="left")

    open_window.append(window)

    def on_close():
        close_and_check(window)                  #same
    window.when_closed = on_close

def info_Nuomifan():
    window = Window(app, title="About Local Cuisine", width=800, height=300)
    Text(window, text="""Wenzhou boasts a variety of local specialties, 
    the most typical of which are glutinous rice, fried vermicelli noodles, and WanZhou pastry. 
    Glutinous rice is a good choice of breakfast, providing a strong sense of satiety. 
    Fried vermicelli noodles can be a main meal, like lunch or dinner 
    while WenZhou pastry are a snack with a smooth texture.""", width=80)
    Picture(window, image="Fan.gif", align="left")
    Picture(window, image="Gao.gif", align="left")
    Picture(window, image="Fengan.gif", align="left")

    open_window.append(window)

    def on_close():
        close_and_check(window)                   #same
    window.when_closed = on_close

def info_jiangxinyu():
    window = Window(app, title="About Jiangxin Island", width=800, height=300)
    Text(window, text="""There are two pagodas located on Jiangxin Island, built about a thousand years ago, 
    which serve as lighthouses to guide ships. There is also a Buddhist temple on the island, 
    which attracts many tourists. It is ranked first among the four famous islands in China.""", width=80)
    Picture(window, image="JiangHe.gif", align="left")
    Picture(window, image="JiangSi.gif", align="left")
    Picture(window, image="JiangTa.gif", align="left")

    open_window.append(window)

    def on_close():
        close_and_check(window)                   #same
    window.when_closed = on_close


def rem_info(index, function):
    def wrapped():
        click[index] = True                       #A function that remember this picture have been clicked when user click it. Open the window and check "is it the time to open the question window?"
        function()
        play_music()
        check_all_and_closed()
    return wrapped


main_box = Box(app, align="top")

left_box = Box(main_box, align="left")
PushButton(left_box, image="DongTa.gif", command=rem_info(0, info_DongTa))
PushButton(left_box, image="Liu.gif", command=rem_info(1, info_Liu))

right_box = Box(main_box, align="right")
PushButton(right_box, image="Yandangshan.gif", grid=[1,2], align="bottom", command=rem_info(2, info_Yandangshan))
PushButton(right_box, image="Ojiang (1).gif", grid=[1,0], align="top", command=rem_info(3, info_Ojiang))
PushButton(right_box, image="Nuomifan.gif", grid=[2,1], align="right", command=rem_info(4, info_Nuomifan))
PushButton(right_box, image="jiangxinyu.gif", grid=[1,1], align="bottom", command=rem_info(5, info_jiangxinyu))

#These are the button that user will click. Once user click the button, open the correct window.




app.display()