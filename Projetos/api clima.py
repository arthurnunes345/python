#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests
import json

cidade = input("Esceva sua cidade: ")
requisicao = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+cidade+'&appid=462b525854b8f01b2d04259cb907e697 ')

print(requisicao.text)


# In[13]:


import requests
import json

cidade = input("Esceva sua cidade: ")
requests.get('http://api.openweathermap.org/data/2.5/forecast/daily?q='+cidade+'&cnt=1&appid=462b525854b8f01b2d04259cb907e697')

print(requisicao.text)


# In[ ]:





# In[2]:


import requests
import json

iTOKEN = '9c6f39be1144b19f2f20dd4c3ed757b6' 

iTIPOCONSULTA1 = 1

#"http://apiadvisor.climatempo.com.br/api/v1/locale/city?name=São Paulo&state=SP&token=your-app-token"

if iTIPOCONSULTA1 == 1:
    iCITY = input("informe o nome da cidade:  ")
    iURL = "http://apiadvisor.climatempo.com.br/api/v1/locale/city?name="+str(iCITY)+"&token="+str(iTOKEN)
    iRESPONSE = requests.request("GET",iURL)
    iRETORNO_REQ = json.loads(iRESPONSE.text)
    print(iRETORNO_REQ)



# In[6]:


import requests, json 
api_key = "462b525854b8f01b2d04259cb907e697"
base_url = "http://api.openweathermap.org/data/2.5/weather?"
city_name = input("Enter city name : ") 
complete_url = base_url + "appid=" + api_key + "&q=" + city_name 
response = requests.get(complete_url) 

x = response.json() 
  
if x["cod"] != "404": 
  
    
    
    y = x["main"] 
  
    
    
    current_temperature = y["temp"] 
    
    
    
    current_pressure = y["pressure"] 
  
    
    
    current_humidiy = y["humidity"] 
  
    
    
    z = x["weather"] 
  
    
    
    
    weather_description = z[0]["description"] 
  
    
    print(" Temperatura (in kelvin unit) = " +
                    str(current_temperature) + 
          "\n atmospheric pressure (in hPa unit) = " +
                    str(current_pressure) +
          "\n humidity (in percentage) = " +
                    str(current_humidiy) +
          "\n description = " +
                    str(weather_description)) 
  
else: 
    print(" City Not Found ") 


# # clima atual da minha cidade

# In[3]:


import pyowm
owm = pyowm.OWM('462b525854b8f01b2d04259cb907e697')
observation = owm.weather_at_place('Vespasiano,BR')
w = observation.get_weather()


# In[5]:


# humidade do ar
w.get_humidity()


# In[4]:


# Informação sobre o vento
w.get_wind()


# In[12]:


#temperartura de hoje
w.get_temperature('celsius')

