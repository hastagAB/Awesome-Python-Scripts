import webbrowser as wb 
import requests
import re
import json


username=input("Enter the username : ")

try:
	content = requests.get("https://www.instagram.com/"+username).content
	find=re.findall(r"logging_page_id.*show_suggested_profiles",str(content))
	user_id=((find[0][16:]).split(","))[0][14:-1] # We get the user id of the username
	jsonreq=requests.get("https://i.instagram.com/api/v1/users/"+user_id+"/info/").content # using a link we get the whole info of the person
	jsonloaded=json.loads(jsonreq)
	imgurl=jsonloaded["user"]["hd_profile_pic_url_info"]["url"]
	wb.open_new_tab(imgurl)
except:
	print("No such username exists")
