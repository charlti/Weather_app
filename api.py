import requests
import dearpygui.dearpygui as dpg

class dataValues():
    userInput = ""
    location = ""
    country = ""
    temp = 0
    updated = ""
    code = 0
    codeStatus = 0
    

key = "yourKey"
url = " http://api.weatherapi.com/v1/current.json?key="


def sendRequest(key, url, userInput):
    url = url + key + "&q=" + userInput
    dataValues.code = requests.get(url)
    dataValues.codeStatus = dataValues.code.status_code

    if dataValues.codeStatus == 200:

        response = requests.get(url).json()
        dataValues.location = response['location']['name']
        dataValues.country = response['location']['country']
        dataValues.temp = response['current']['temp_c']
        dataValues.updated = response['current']['last_updated']
        print(f"Temperature in {dataValues.location}, {dataValues.country} is {dataValues.temp} °C") 
        print(f"This was updated on {dataValues.updated}") 

    else:
        print("The name of your city is incorect, try again !")

    
def getCity(sender, value, user_data):
   
    dataValues.userInput= dpg.get_value("city")
    sendRequest(key, url, dataValues.userInput)

    if dataValues.codeStatus == 200:
        dpg.set_value(user_data, f"Temperature in {dataValues.userInput}, {dataValues.country} is : {dataValues.temp} °C")
    else:
        dpg.set_value(user_data, "The name of your city is incorrect, try again !")
    

with dpg.window(tag = "Primary Window"):

    dpg.add_text("Weather app", pos= [690, 200], color= (0, 187, 255))
    textControl = dpg.add_text(pos = [600, 450])
    dpg.add_input_text(tag = "city", hint="Enter your city here", width= 180, pos=[600,510])
    dpg.add_button(label="Send", callback=getCity, pos=[800, 510], height= 19, width=100, user_data= textControl) 
    

dpg.create_viewport(title = "Weather app")
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("Primary Window", True)
dpg.start_dearpygui()
dpg.destroy_context()










