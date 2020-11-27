from flask import Flask,jsonify,render_template,request
import requests
app=Flask(__name__)
city=input("ENTER CITY : ")
api_key= #YOUR API KEY HERE
apiaddress='http://api.openweathermap.org/data/2.5/weather?q='+ city+'&appid='+api_key

jsondata=requests.get(apiaddress).json()
jsondata1=jsondata['weather'][0]['main']
jsondata2=jsondata['weather'][0]['description']
print(apiaddress)
print("weather : ",jsondata1," description : ",jsondata2)
