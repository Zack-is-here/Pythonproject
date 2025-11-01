#The unit 3 project

from guizero import App, Window, Text, TextBox, PushButton, Combo, info

app = App(title="Unit Converter", width=300, height=200)

def open_unit_window():
    unit_win.show()
    app.hide()                                    

def open_temp_window():
    temp_win.show()                       #These function will show the calculate window and hide the main menu.
    app.hide()

def open_money_window():
    money_win.show()
    app.hide()

Text(app, text="Choose one to convert", size=16)

PushButton(app, text="Unit Conversion(cm, m, inch)", command=open_unit_window, width=30)
PushButton(app, text="Temperature Conversion(℃, ℉)", command=open_temp_window, width=30)
PushButton(app, text="Currency Conversion(CAD, RMB)", command=open_money_window, width=30)
#These are the buttons that can use the "show the window can close the main menu" function.



unit_win = Window(app, title="Unit Converter", width=350, height=300)
unit_win.hide()
#This is the unit window, to hide it first, show it when the button it pushed.


def ca_unit():
    try:                                          #The caculate part
        val = float(unit_input.value)
        in_unit = input_unit.value
        out_unit = unit_combo.value

        if in_unit == out_unit:
            result.value = f"{val} {in_unit} = {val} {out_unit}"
        elif in_unit == "centimeter":
            if out_unit == "meter":
                resu = val / 100
            elif out_unit == "inch":
                resu = val / 2.54
        elif in_unit == "meter":
            if out_unit == "centimeter":
                resu = val * 100
            elif out_unit == "inch":
                resu = val * 39.3701
        elif in_unit == "inch":
            if out_unit == "centimeter":
                resu = val * 2.54
            elif out_unit == "meter":
                resu = val / 39.3701
        result.value = f"{val} {in_unit} = {resu:.2f} {out_unit}"
    except:
        info("error", "Please enter a valid number!")

def reset_unit():               #To reset, make the input and result to nothing.
    unit_input.value = ""
    result.value = ""

def close_unit():
    unit_win.hide()             #To close it, hide it and show the main menu.
    app.show()

Text(unit_win, text="Enter the number:")
unit_input = TextBox(unit_win, width=20)

Text(unit_win, text="Input unit:")
input_unit = Combo(unit_win, options=["centimeter", "meter", "inch"])   #Options user can choose.
input_unit.value = "centimeter"

Text(unit_win, text="Convert to:")
unit_combo = Combo(unit_win, options=["centimeter", "meter", "inch"])   #Output user can choose.
unit_combo.value = "meter"

PushButton(unit_win, text="calculate", command=ca_unit)
PushButton(unit_win, text="reset", command=reset_unit, height=1, width=5)   #Buttons
PushButton(unit_win, text="Main menu", command=close_unit)

result = Text(unit_win, text=" ", size=12, color="blue")



temp_win = Window(app, title="Temperature Converter", width=350, height=300)
temp_win.hide()
                                         #Temperature Converter.
def ca_temp():
    try:
        val = float(temp_input.value)
        mode = temp_combo.value
        if mode == "Celsius --> Fahrenheit":
            res = val * 9 / 5 + 32
            result_temp.value = f"{val} ℃ = {res:.1f} ℉"     #How to calculate the temperature.
        else:
            res = (val - 32) * 5 / 9
            result_temp.value = f"{val} ℉ = {res:.1f} ℃"
    except:
        info("error", "Please enter a valid number")

def reset_temp():
    temp_input.value = ""
    result_temp.value = ""                 #Make the input and result to nothing to reset.

def close_temp():
    temp_win.hide()                        #hide the window and shoe the main menu to close it.
    app.show()

Text(temp_win, text="Enter the Temperature:")
temp_input = TextBox(temp_win, width=20)
Text(temp_win, text="Choose a way to Converter:")         #options user can choose.
temp_combo = Combo(temp_win, options=["Celsius ---> Fahrenheit", "Fahrenheit ---> Celsius"])
temp_combo.value = "Celsius ---> Fahrenheit"

PushButton(temp_win, text="calculate", command=ca_temp)
PushButton(temp_win, text="reset", command=reset_temp)
PushButton(temp_win, text="Main menu", command=close_temp)    #buttons

result_temp = Text(temp_win, text="", size=12, color="red")



money_win = Window(app, title="Currency Converter", width=350, height=300)
money_win.hide()                   #The currency part.

def calc_currency():
    try:
        val = float(currency_input.value)
        mode = currency_mode.value
        if mode == "RMB ➜ CAD":
            res = val / 5
            result_currency.value = f"￥{val:.2f} RMB = ${res:.2f} CAD"
        else:                                                                  #calculate part
            res = val * 5
            result_currency.value = f"${val:.2f} CAD = ￥{res:.2f} RMB"
    except:
        info("Error", "Please enter a valid number!")

def reset_currency():
    currency_input.value = ""                       
    result_currency.value = ""                 #To reset, make the input and result to nothing.

def close_currency():
    money_win.hide()
    app.show()                                 #To close it, hide it and show the main menu.

Text(money_win, text="Choose conversion direction:")
currency_mode = Combo(money_win, options=["RMB ➜ CAD", "CAD ➜ RMB"])   #options user can choose.
currency_mode.value = "RMB ➜ CAD"

Text(money_win, text="Enter the RMB or CAD:")
currency_input = TextBox(money_win, width=20)        #User input

PushButton(money_win, text="Calculate", command=calc_currency)
PushButton(money_win, text="reset", command=reset_currency)      #buttons
PushButton(money_win, text="Main menu", command=close_currency)

result_currency = Text(money_win, text="", size=12, color="purple")



app.display()
