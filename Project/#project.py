#project

from guizero import App, Text, TextBox, PushButton, Picture, Box, Window

app = App("The introduction of my home town")

text=Text(app, "About WenZhou. Click the picture to read more!")

def info_DongTa():
    info_window = Window(app, title="About East pagoda", width=740, height=300)
    Text(info_window, text="""The Yueqing East Pagoda, located atop Donggao Mountain in Yueqing City, Wenzhou City," 
    Zhejiang Province, is a relic of ancient architecture from the Song Dynasty. 
    Built during the Northern Song Dynasty (1068-1077)," 
    the Yueqing East Pagoda stands approximately 18 meters tall. 
    Numerous inscriptions adorn the bricks of the pagoda, " 
    revealing its rich history, scientific significance, and artistic value.""", width=300)
    Picture(info_window, image="DongTa2.gif", align="left")
    Picture(info_window, image="China.gif", align="right")

def info_Liu():
    info_window = Window(app, title="About Liu Ji", width=800, height=300)
    Text(info_window, text="""Liu Ji (1 July 1311 - 16 May 1375), better known as Liu Bowen,
was a Chinese military strategist, philosopher, and politician who lived in the late Yuan and early Ming dynasties.
He was born in Wencheng County, WenZhou, Zhejiang.He served as a key advisor to Zhu Yuanzhang, the Emperor, 
the founder of the Ming dynasty, in the latter's struggle to overthrow the 
Yuan dynasty and unify China proper under his rule.""", width=300)
    Picture(info_window, image="LiuJi.gif", align="left")
    ming_box=Box(app, align="right")
    Picture(info_window, image="Ming.gif", align="left")
    Text(info_window, text="<--(The ming Empire)", align="left")

def info_Yandangshan():
    info_window = Window(app, title="About Yandang Mountain", width=650, height=300)
    Text(info_window, text="""Yandang Mountain is a mountain located in Yueqing, north of Wenzhou City,
    Zhejiang Province, China. It rises 500 to 600 meters southeast of the Yangtze River, 
    with its main peak, Baigangjian, at 1,108 meters southeast of the Yangtze River.
    It is designated a World Geopark, a Belt and Road National Key Scenic Area,
    and a National 5A Tourist Attraction.""", width=150)
    Picture(info_window, image="YandangshanA.gif", align="left")
    Picture(info_window, image="YandangshanB.gif", align="left")


def info_Ojiang():
    info_window = Window(app, title="About Ojiang River", width=800, height=300)
    Text(info_window, text="""The Ou River is the second-largest river in the Zhejiang province of eastern China.
    The river flows 388 kilometers  before finally reaching the city of Wenzhou and emptying into the East China Sea.
    The natural environment in the basin is well protected and has huge reserves of natural resources, 
    making it a good tourist destination.Also, Oujiang River has a species that is unique in the world -
    The Oujiang minnow.This is a small fish that usually lives in the middle and lower reaches of rivers. 
    It hides in deeper waters during the day and swims to shallower waters in the evening to find food.""")
    Picture(info_window, image="OjiangA.gif", align="left")
    Picture(info_window, image="OjiangB.gif", align="left")
    Picture(info_window, image="Fish.gif", align="left")

def info_Nuomifan():
    info_window = Window(app, title="About Wenzhou traditional cuisine", width=800, height=300)
    Text(info_window, text="""Wenzhou boasts a variety of local specialties, 
    the most typical of which are glutinous rice, fried vermicelli noodles, and sponge cakes. 
    Glutinous rice is a good breakfast,providing a strong sense of satiety. 
    Fried vermicelli noodles can be a main meal, 
    while sponge cakes are a snack with a smooth texture.""")
    Picture(info_window, image="Fan.gif", align="left")
    Picture(info_window, image="Gao.gif", align="left")
    Picture(info_window, image="Fengan.gif", align="left")

def info_jiangxinyu():
    info_window = Window(app, title="About Jiangxin Temple", width=800, height=300)
    Text(info_window, text="""There are two pagodas on Jiangxin Island, built about a thousand years ago, 
    which serve as lighthouses to guide ships. There is also a Buddhist temple on the island, 
    which attracts many tourists. It is ranked first among the four famous islands in China.""", width=150)
    Picture(info_window, image="JiangHe.gif", align="left")
    Picture(info_window, image="JiangSi.gif", align="left")
    Picture(info_window, image="JiangTa.gif", align="left")

main_box = Box(app, align="top")


left_box = Box(main_box, align="left")
img1 = PushButton(left_box, image="DongTa.gif", command=info_DongTa)
img2 = PushButton(left_box, image="Liu.gif", command=info_Liu)

right_box = Box(main_box, align="right")
img3 = PushButton(right_box, image="Yandangshan.gif", grid=[1,2], align="bottom", command=info_Yandangshan)
img4 = PushButton(right_box, image="Ojiang (1).gif", grid=[1,0], align="top", command=info_Ojiang)
img5 = PushButton(right_box, image="Nuomifan.gif", grid=[2,1], align="right", command=info_Nuomifan)
img6 = PushButton(right_box, image="jiangxinyu.gif", grid=[1,1], align="bottom", command=info_jiangxinyu)







app.display()
