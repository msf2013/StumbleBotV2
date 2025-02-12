import random
import funmanager
#import openai
pip install requests beautifulsoup4 websocket-client colorama pickledb cloudscraper g4f openai
#import pickledb

import cloudscraper
from g4f.client import Client

client = Client()

import threading
import requests
import websocket
import json
import re
import signal
import os
import sys
from colorama import Fore, Style, init
from bs4 import BeautifulSoup
import time
import unicodedata
from requests.cookies import RequestsCookieJar
from datetime import datetime, timedelta
#from playsound import playsound

# Play an MP3 file
#playsound("ding.mp3")
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
startTime = time.time()

'''

∧,,,∧\n
( ̳• · •̳)\n
/ づ\̅_̅/̷̚ʾ ℂ𝕠𝕗𝕗𝕖𝕖 ℂ𝕙𝕖𝕖𝕣𝕤\n

'''

init(autoreset=True)

username = "spamfairy2024"
password = "gifisnotgif"
botsname = "Spamfairy"
bot_prefix = "@"
room_name = "outpost"
logpath = room_name + '_logs.txt'
badwords = ['ni--er','abortions']
debugging = True
kob = True
secretkey = "tigerpaw"
guestnamesallowed = True 
guestsallowed = True
guestnamesallowed = True
currentYT = ""
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
SUITS = '♣ ♢ ♡ ♠'.split()

imgur_ID = '---'
youtube_api_key = ""
youtube_playlist = []
#loadlists
knownuserslist = f'{room_name}_KnownUsers.txt'
knownusers = []
userlist = []
cambans = []
checkvip = False
VIPCAM = False
announcement = False

greet = True
onlineusers = 1 # <---- yea im #1
#===========================================
#=============  User Rights ================
#===========================================

Level0 = [] #Guest
Level1 = [] #Everyone
Level2 = [] #Operator/Mods
Level3 = [] #CoOwner
Level4 = [] #Admin
operators = []
userdata = {}
admins = []

session = cloudscraper.create_scraper()
cookie_jar = RequestsCookieJar()

left_eyes = ["≽", "≼", "⩾", "⩽", ">", "<", "◕", "✧"]
right_eyes = ["≽", "≼", "⩾", "⩽", ">", "<", "◕", "✧"]
noses = ["•", "⩊", "⩌", "⪡", "⪢", "o", "∘"]
mouths = ["^", "-", "_", "~", "ω", "w"]

emoticons = [
    "( ͡° ͜ʖ ͡°)", "(☞ ͡° ͜ʖ ͡°)☞", "(╯°□°)╯︵ ┻━┻", "┬─┬ ノ( ゜-゜ノ)",
    "(ಥ_ಥ)", "¯\\_(ツ)_/¯", "(づ｡◕‿‿◕｡)づ", "(ノಠ益ಠ)ノ彡┻━┻", "(ಠ_ಠ)", "(ง •̀_•́)ง",
    "(ᵔᴥᵔ)", "(ʘ‿ʘ)", "(≧▽≦)", "(・_・)", "(¬‿¬)", "ʕ•ᴥ•ʔ", "ʕノ•ᴥ•ʔノ ︵ ┻━┻",
    "ʕ´•ᴥ•`ʔ", "(ಥ﹏ಥ)", "(>_<)", "(^_^)", "(o_O)", "(¬_¬)", "(✿◕‿◕)", "(✧ω✧)",
    "(◕‿◕✿)", "(╥﹏╥)", "ヽ(´▽`)/", "(´∀`)", "(ᵕ.ᵕ)", "(*^‿^*)", "(•‿•)",
    "( ͡ᵔ ͜ʖ ͡ᵔ )", "(ง'̀-'́)ง", "(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧", "(≧◡≦)", "(Ｔ▽Ｔ)", "ヽ(✿ﾟ▽ﾟ)ノ",
    "(~˘▾˘)~", "(☞ﾟ∀ﾟ)☞", "(´･_･`)", "(´・ω・｀)", "o(≧▽≦)o", "(✿╹◡╹)", "(>人<)",
    "(*´ω｀*)", "(>w<)", "(⌒‿⌒)", "(─‿‿─)", "(･ิω･ิ)", "(°ロ°)", "(ʘᴗʘ✿)",
    "(⊙_☉)", "(✪ω✪)", "(｀∀´)Ψ", "(╯︵╰,)", "(*≧ω≦)", "(☆▽☆)", "(✿´‿`)",
    "(＾▽＾)", "(ᗒᗨᗕ)", "(╬ ಠ益ಠ)", "＼(º □ º l|l)/", "( ﾟヮﾟ)", "(๑˃ᴗ˂)ﻭ",
    "(≧∇≦)/", "(๑•̀ㅂ•́)و✧", "ヽ(✧ᗜ✧)ノ", "(⌐■_■)", "(ಠ‿ಠ)", "(╬ Ò﹏Ó)",
    "(╯_╰)", "(´･ᴗ･ ` )", "(o´▽`o)", "(ʘ╭╮ʘ)", "(´ヘ｀;)", "(⩾﹏⩽)", "(￣︿￣)",
    "(*￣▽￣)b", "(๑•́ ω •̀๑)", "( ͡ಠ ʖ̯ ͡ಠ)", "(*≧︶≦))(￣▽￣* )ゞ", "(´･ω･`)ﾉ",
    "(｡♥‿♥｡)", "ヽ(°◇° )ノ", "(ノ´∀`)ノ", "٩(｡•́‿•̀｡)۶", "(•̀ᴗ•́)و ̑̑", "(๑˘︶˘๑)",
    "(⌒▽⌒)☆", "(∩^o^)⊃━☆ﾟ.*･｡ﾟ", "(∪｡∪)｡｡｡zzz", "(ノT＿T)ノ", "(´・ω・)っ由",
    "ヽ(｡◕o◕｡)ﾉ.", "(。・ω・。)", "(´ε｀ )♡", "(╯▽╰ )", "(o˘◡˘o)"
]

def generate_random_smiley():
    # Randomly pick parts for the smiley
    left_eye = random.choice(left_eyes)
    right_eye = random.choice(right_eyes)
    nose = random.choice(noses)
    mouth = random.choice(mouths)
    
    # Construct the smiley
    smiley = f"{left_eye}^{nose}{mouth}{nose}^{right_eye}"
    return smiley



def log_message(message, log_type="INFO"):
    
    with open(logpath, 'a') as log_file:
        log_file.write(f"{log_type}: {message}\n")

def load_banned_handles(filename="cambans.txt"):
    # Open the file in read and append mode
    with open(filename, "a+") as file:
        # Move the file pointer to the beginning
        file.seek(0)
        # Read lines and store them as a set of stripped strings
        return {line.strip() for line in file}

# Load banned handles once at the start
banned_handles = load_banned_handles()


correctanswer = ""
class User:
    def __init__(self, handle, avatar, backgroundcolor, namebackgroundcolor, messagetextcolor, username, nick, mod, guest):
        self.handle = handle
        self.avatar = avatar
        self.backgroundcolor = backgroundcolor
        self.namebackgroundcolor = namebackgroundcolor
        self.messagetextcolor = messagetextcolor
        self.username = username
        self.nick = nick
        self.mod = mod
        self.guest = guest
    def get_handle_by_username(self, username):
        if self.username == username:
            return self.handle
        return None
    def get_username_by_handle(self, handle):
        if self.handle == handle:
            return self.username
        return None

    def __repr__(self):
        return f"'username':'{self.username}', 'handle': '{self.handle}'"



def get_csrf_token():
    try:
        login_page_response = session.get('https://stumblechat.com/login')
        login_page_response.raise_for_status()
        soup = BeautifulSoup(login_page_response.text, 'html.parser')
        csrf_token = soup.find('meta', {'name': '_csrf'}).get('content')
        csrf_cookie = login_page_response.cookies.get('_csrf')
        #print(f"{Fore.LIGHTGREEN_EX}CSRF token retrieved: {csrf_token}{Style.RESET_ALL}")
        #print(f"{Fore.LIGHTGREEN_EX}CSRF cookie retrieved: {csrf_cookie}{Style.RESET_ALL}")
        return csrf_token, csrf_cookie
    except requests.exceptions.RequestException as e:
        print(f"{Fore.LIGHTRED_EX}Error retrieving CSRF token: {e}{Style.RESET_ALL}")
        exit(1)

def login():
    try:
        csrf_token, csrf_cookie = get_csrf_token()
        headers = {
            'content-type': 'application/json;charset=UTF-8',
            'cookie': f'_csrf={csrf_cookie}',
            'csrf-token': csrf_token
        }
        data = {
            'username': username,
            'password': password,
            'rememberme': True
        }
        response = session.post('https://stumblechat.com/account/login', headers=headers, json=data)
        response.raise_for_status()
        session_cookie = response.cookies.get('StumbleChatV2')
        print(f"{Fore.LIGHTGREEN_EX}Login successful.{Style.RESET_ALL}")
        return csrf_token, csrf_cookie, session_cookie
    except requests.exceptions.RequestException as e:
        print(f"{Fore.LIGHTRED_EX}Login failed: {e}{Style.RESET_ALL}")
        exit(1)

if cookie_jar:
    session.cookies.update(cookie_jar)

csrf_token, csrf_cookie, session_cookie = login()
cookie_jar.set('_csrf', csrf_cookie)
cookie_jar.set('StumbleChatV2', session_cookie)
session.cookies.update(cookie_jar)

headers = {
    'content-type': 'application/json;charset=UTF-8',
    'cookie': f'_csrf={csrf_cookie}; StumbleChatV2={session_cookie}',
    'csrf-token': csrf_token
}
def get_websocket_endpoint(room_name):
    try:
        data = {'name': room_name}
        response = session.post('https://stumblechat.com/api/room/token', headers=headers, json=data)
        response.raise_for_status()
        result = response.json()
        return result['endpoint'], result['result']
    except requests.exceptions.RequestException as e:
        print(f"{Fore.LIGHTRED_EX}Error getting WebSocket endpoint: {e}{Style.RESET_ALL}")
        exit(1)
def HandleUptime(startTime):
    
    uptime = time.time() - startTime
    days = int(uptime // (24 * 3600))
    hours = int((uptime % (24 * 3600)) // 3600)
    minutes = int((uptime % 3600) // 60)
    seconds = int(uptime % 60)
    uptime_message = (f"Uptime: {days} days, {hours} hours, "
                      f"{minutes} minutes, {seconds} seconds")

    SendPublicMessage(uptime_message)

def HandleUserCamClose(name):


    handle = get_handle_by_nick_or_username(name, userlist)
    
    SendPublicMessage(f"{name}: {handle} was closed. Not really.")

def SendPublicMessage(message):
    global emoticons
    #message = message.replace("\n", " ")
    truncated_message = message[:400]

    time.sleep(0.6)
    emoji = random.choice(emoticons)
    smiles = generate_random_smiley()
    pb = {"stumble": "msg", "text": "🎉🎆🎇🥳🥳🥳🎆🎇🎉⎛⎝" + smiles + "⎠⎞\n" + truncated_message} # + " " + emoji}
    ws.send(json.dumps(pb))
    print(f"{Fore.LIGHTYELLOW_EX}Sent public message:\n{pb} {Style.RESET_ALL}")

def SendGPTPublicMessage(message):
    global emoticons
    # Remove newlines from message
    message = message.replace("\n", " ")

    # Split the message into chunks of 400 characters
    message_chunks = [message[i:i+400] for i in range(0, len(message), 400)]
    
    for chunk in message_chunks:
        time.sleep(0.6)  # Wait for 0.6 seconds between messages
        emoji = random.choice(emoticons)  # Random emoticon
        pb = {"stumble": "msg", "text": "🤖" + chunk + " " + emoji}
        ws.send(json.dumps(pb))
        print(f"{Fore.LIGHTYELLOW_EX}Sent public message:\n{pb} {Style.RESET_ALL}")
def YoutubeSearch(keyword):
    message = {
            'stumble': 'youtube',
            'type': 'add',
            'id': keyword,
            'time': 0
        }
    ws.send(json.dumps(message))

    SendPublicMessage(f'{videoid} added!')
def get_first_video_id(api_key, query):
    
    base_url = "https://www.googleapis.com/youtube/v3/search"
    params = {
        'part': 'snippet',
        'q': query,
        'type': 'video',
        'maxResults': 1,
        'key': youtube_api_key
    }
 
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()
        if 'items' in data and len(data['items']) > 0:
            video_id = data['items'][0]['id']['videoId']
            return video_id
        else:
            print("No videos found for the query.")
            return None
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None
def YoutubeAdd(videoid):
    video_id_match = re.search(r'v=([a-zA-Z0-9_-]+)', videoid)
    
    if video_id_match:
        video_id = video_id_match.group(1)
        print(f"Video ID extracted: {video_id}")
        message = {
            'stumble': 'youtube',
            'type': 'add',
            'id': videoid,
            'time': 0
        }
        ws.send(json.dumps(message))
        SendPublicMessage(f'{videoid} added!')

    else:
        SendPublicMessage('Invalid YouTube URL. Could not extract video ID.')
def search_imgur(keyword, num_results=1):
    
    imgur_headers = {
        'Authorization': f'Client-ID {imgur_ID}'
    }
    search_url = 'https://api.imgur.com/3/gallery/search'
    params = {
        'q': keyword,
        'limit': num_results
    }
    response = requests.get(search_url, headers=imgur_headers, params=params)
    
    if response.status_code == 200:
        data = response.json()
        images = data.get('data', [])
        return [image['link'] for image in images if 'link' in image]
    else:
        print('Failed to retrieve data:', response.status_code)
        return []
def CheckMessage(username, msg):
    if badwords in msg:
        pass

        if kob == False:
            ws.send(json.dumps({"stumble": "kick","user": username}))
        else:
            ws.send(json.dumps({"stumble": "ban","user": username}))

def add_handle(handle_id):
    
    with open('allowed.txt', 'a') as file:
        file.write(f"{handle_id}\n")
    accepted.append(handle_id)
    SendPublicMessage(f"{handle_id} added to allowed.txt!")

def remove_handle(handle_id):
    try:
        with open('allowed.txt', 'r') as file:
            lines = file.readlines()
        with open('allowed.txt', 'w') as file:
            for line in lines:
                if line.strip() != handle_id:
                    file.write(line)
    except FileNotFoundError:
        print("The file 'allowed.txt' does not exist.")

def CheckCamBan(handle):
    with open('allowedcam.txt', 'a+') as allowed:
        known_users = allowed.read().splitlines()
        if handle not in known_users:
            SendPublicMessage(f'{handle} is not on the allowed list, @knownadd {handle}.')
            print(f"User in cam bans: {handle}!")
            #SendCloseCam(handle)
        else:
            print(f"User not in cam bans: {handle}.")

def get_handle_by_nick_or_username(nick_or_username, userlist):
    for user in userlist:
        if user.nick == nick_or_username or user.username == nick_or_username:
            return user.handle
    return None

def Handle_Joined(data):
    #print(f'[HANDLEJOINED] {data}')
    try:
        room_info = data['room']
        self_info = data['self']
        self_userlist = data['userlist']
        self_broadcasts = data['broadcasts']

        #print(f"Userlists: {self_userlist}")
        #print(self_broadcasts)
        global userlist
        #print(userlist)
        for user_data in self_userlist:
            user = User(
                handle=user_data['handle'],
                avatar=user_data['avatar'],
                backgroundcolor=user_data['backgroundcolor'],
                namebackgroundcolor=user_data['namebackgroundcolor'],
                messagetextcolor=user_data['messagetextcolor'],
                username=user_data['username'],
                nick=user_data['nick'],
                mod=user_data['mod'],
                guest=user_data['guest']
            )
            userlist.append(user)
            #print(f'[USERLIST] {userlist}')
 
        room_avatar = room_info.get('avatar', 'N/A')
        room_biography = room_info.get('biography', 'No biography available')
        room_location = room_info.get('location', 'Unknown location')
        room_name = room_info.get('name', 'Unknown room')


        self_avatar = self_info.get('avatar', 'N/A')
        self_chatcolor = self_info.get('chatcolor', '#000000')
        self_namecolor = self_info.get('namecolor', '#FFFFFF')
        self_handle = self_info.get('handle', 'Unknown handle')
        self_mod = self_info.get('mod', False)
        if self_mod > 2:
            operators.append(self_handle)
            print(f'{self_handle} has been added to operators')
        
        print(f'Joined room "{room_name}" as "{self_handle}".')

        # testing
        test_nick_or_username = "goofygoobers"
        handle = get_handle_by_nick_or_username(test_nick_or_username, userlist)
        if handle:
            print(f"Handle for '{test_nick_or_username}' is {handle}.")
        else:
            print(f"No user found with nick or username '{test_nick_or_username}'.")

    except KeyError as e:
        print(f"Missing expected data: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
def Handle_Ping():
    ws.send(json.dumps({"stumble":"0"}))
    print("Pong!")
def Handle_YoutubePlay(data):

    handletype = data['type']
    if 'play' in handletype:
        title = data['title']
        videoid = data['id']
        queueid = data['queueid']
        vidtime = data['time']
        
        log_entry = {
            'title': title,
            'videoid': videoid,
            'queueid': queueid,
            'time': vidtime
        }
        
        log_file = 'youtubelog.json'
        if os.path.exists(log_file):
            with open(log_file, 'r') as file:
                try:
                    existing_entries = json.load(file)
                except json.JSONDecodeError:
                    existing_entries = []
        else:
            existing_entries = []

        
        if not any(entry['videoid'] == videoid for entry in existing_entries):
            
            existing_entries.append(log_entry)
            
            with open(log_file, 'w') as file:
                json.dump(existing_entries, file, indent=4)
            print(f"Logged entry: {log_entry}")
        else:
            print("Entry already exists in the log.")
    else:

        if 'stop' in handletype:
            print('Youtube Stopped!')
def Handle_OnSys(data):

    text = data['text']
    print('[SYS MESSAGE] %s'  % text) 
def SendPublicMessage2(message):
    time.sleep(0.6)
    ws.send(json.dumps({"stumble": "msg","text": message}))
def PlayTwitch(channel):
    ws.send(json.dumps({'stumble': 'twitch','type': 'play','name': channel}))
    SendPublicMessage(f"Added {channel} to the Twitch Player. https://www.twitch.tv/{channel} ")
def PlayWSHH(url):
    ws.send(json.dumps({'stumble': 'wshh','type': 'play','url': url}))
def StopWSHH():
    ws.send(json.dumps({'stumble': 'wshh','type': 'stop'}))
def PlayDailyMotion(url):
    ws.send(json.dumps({'stumble': 'dailymotion','type': 'play','url': url}))
def StopDailyMotion():
    ws.send(json.dumps({'stumble': 'dailymotion','type': 'stop'}))

def PlayOutPost():
    ws.send(json.dumps({'stumble': 'soundcloud','type': 'play','url': 'https://soundcloud.com/semperzombie/outpost-more-like-inpost-official-version?utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing'}))

def StopTwitch():
    ws.send(json.dumps({'stumble': 'twitch','type': 'stop'}))
def HandleTwitchShout():
    message = "📺 🚀 ⭐ SemperZombie is Live! Watch here: https://www.twitch.tv/semperzombie ⭐ 🚀 📺 "
    ws.send(json.dumps({"stumble": "msg","text": message}))
    Channel = 'semperzombie'
    ws.send(json.dumps({'stumble': 'twitch','type': 'play','name': Channel}))

def GuestAllowed():
    ws.send(json.dumps({'stumble': 'room', 'type': 'guests', 'enabled': '1'}))
def PublicRoom():
    ws.send(json.dumps({'stumble': 'room', 'type': 'public', 'enabled': '1'}))
def GreenRoom():
    ws.send(json.dumps({'stumble': 'room', 'type': 'greenroom', 'enabled': '1'})) 

def HandleCheers():

    cheers = [
                '̷🅒🅗🅔🅔🅡🅢',
                'ᶜᴴᴱᴱᴿˢ',
                '𝒞𝐻𝐸𝐸𝑅𝒮',
                'ℭℌ𝔈𝔈ℜ𝔖',
                'C҉H҉E҉E҉R҉S҉',
                'ꏳꃬꏂꏂꋪꑄ',
                'ςђєєгร',
                'ɔɥǝǝɹs',
                '⊂Ꮒ∈∈ᖇ⟆',
                '𝕔𝕙𝕖𝕖𝕣𝕤',
                '❰ █▬█ █☰ █☰ 🆁 ▟▛ ',
                'ｃ∙ｈ∙ｅ∙ｅ∙ｒ∙ｓ',
                '(っ◔◡◔)っ ♥ Cheers! ♥'
            ]
    emoji = f'~~🔥🔥🔥 {random.choice(cheers)}!!! 🔥🔥🔥 ~~'
    ws.send(json.dumps({"stumble": "msg","text": emoji}))
def SendPrivateMessage(handle, message):
    ws.send(json.dumps({"stumble": "pvtmsg","handle": handle, "text": message}))
def SendPublicEmoji(message):
    emoji = message + ' ~~🔥~~'
    ws.send(json.dumps({"stumble": "msg","text": emoji}))
def HandleChangeNickname(name):
    ws.send(json.dumps({"stumble": "nick","nick": name}))
    print("sent!")
def HandleChatgpt(input_text):
    try:
        
        response = openai.completions.create(
            model="gpt-3.5-turbo",
            prompt=input_text,
            max_tokens=50
        )
        
        return response['choices'][0]['text']
        
    except Exception as e:
        
        return f"An error occurred: {str(e)}"

triviasingle = True
def HandleTrivia():
    if triviasingle:

        choices = ["Entertainment", "Sports", "Science", "Animals", "Mythology", "Politics", "Geography", "History"]
        static = random.choice(choices)
        url = f"https://beta-trivia.bongo.best/?search={static}&type=multiple&difficulty=easy&limit=1"
        req = requests.get(url).text
        data = json.loads(req)
        question = data[0]['question']
        answer = data[0]['correct_answer']
        SendPublicMessage(f"{static} Question: {question}")
        time.sleep(20) 
        SendPublicMessage(f"{static} Answer: {answer}")

def HandleTriviaBot():
    if not triviastarted:
        while(1):

            choices = ["Entertainment", "Sports", "Science", "Animals", "Mythology", "Politics", "Geography", "History"]
            static = random.choice(choices)
            url = f"https://beta-trivia.bongo.best/?search={static}&type=multiple&difficulty=easy&limit=1"
            req = requests.get(url).text
            data = json.loads(req)
            question = data[0]['question']
            answer = data[0]['correct_answer']
            SendPublicMessage(f"{static} Question: {question}")
            time.sleep(20) 
            SendPublicMessage(f"{static} Answer: {answer}")
def TokeTimerBot():
    # Calculate the time until the next 20th minute
    now = datetime.now()
    current_minute = now.minute
    current_second = now.second

    # Calculate the remaining seconds until the 20th minute of the next hour
    if current_minute < 20:
        # If it's before the 20th minute, calculate the time until 20th minute
        time_until_20th_minute = (20 - current_minute) * 60 - current_second
    else:
        # If it's after the 20th minute, calculate the time until 20th minute of next hour
        time_until_20th_minute = (60 - current_minute + 20) * 60 - current_second

    # Sleep until the 20th minute of the next hour
    time.sleep(time_until_20th_minute)
    #SendPublicMessage(f"https://i.imgur.com/bHEeZBI.gif")
    # After sleeping, run the task
    SendPublicMessage("🔥 420 somewhere! 🔥")

    # Restart the process to run every hour
    TokeTimerBot()

def HandleMusicGPT(message):
    messages = [{"role": "user", "content": "Roleplay"}]
    messages.append({"role": "user", "content": message})
    messages.append({"role": "system", "content": "Please respond in 200 characters or less."})
    messages.append({"role": "system", "content": "You are a new age DJ music store owner who can suggest artist and song. Answer questions in character. Show only artist and song title. Dont use classics."})
    
    # Get response from the assistant
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        web_search=False
    )

    # Remove only Discord links from the response
    def remove_discord_links(text):
        # Regex to match Discord-specific URLs
        discord_pattern = r'(https?://)?(www\.)?discord\.(gg|com)/\S+'
        return re.sub(discord_pattern, '', text)

    # Process assistant's reply
    assistant_reply = response.choices[0].message.content
    filtered_reply = remove_discord_links(assistant_reply)  # Remove Discord links
    filtered_reply = filtered_reply.strip()  # Clean up extra whitespace

    # Send the filtered reply
    SendGPTPublicMessage(f"{filtered_reply}")

def HandleGPT(message):
    messages = [{"role": "user", "content": "Roleplay"}]
    messages.append({"role": "user", "content": message})
    messages.append({"role": "system", "content": "Please respond in 400 characters or less.Never include new line characters like \n"})
    messages.append({"role": "system", "content": "You are a AI companion. Answer questions in character."})
    # Get response from the assistant
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        web_search=False
    )

    def remove_discord_links(text):
        # Regex to match Discord-specific URLs
        discord_pattern = r'(https?://)?(www\.)?discord\.(gg|com)/\S+'
        return re.sub(discord_pattern, '', text)
    
    assistant_reply = response.choices[0].message.content
    filtered_reply = remove_discord_links(assistant_reply)  # Remove Discord links
    filtered_reply = filtered_reply.strip()  # Clean up extra whitespace
    SendGPTPublicMessage(f"{filtered_reply}")

def HandleRPG(message):
    messages = [{"role": "user", "content": "Hello"}]
    messages.append({"role": "user", "content": message})
    messages.append({"role": "system", "content": "Please respond in 400 characters or less."})
    messages.append({"role": "system", "content": "You are a friendly shopkeepers parrot in a pirate town. Answer questions in character."})
    # Get response from the assistant
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        web_search=False
    )
    def remove_discord_links(text):
        # Regex to match Discord-specific URLs
        discord_pattern = r'(https?://)?(www\.)?discord\.(gg|com)/\S+'
        return re.sub(discord_pattern, '', text)

    assistant_reply = response.choices[0].message.content
    filtered_reply = remove_discord_links(assistant_reply)  # Remove Discord links
    filtered_reply = filtered_reply.strip()  # Clean up extra whitespace
    SendGPTPublicMessage(f"🦜: {filtered_reply}")

def HandleGPTImage(message):
    response = client.images.generate(
    model="flux",
    prompt=message,
    response_format="url"
    )
    SendGPTPublicMessage(f"Generated image URL: {response.data[0].url}")
def HandlePublicMessage(data):
    #print(f"[HANDLEPUBLICMESSAGE]\n{data}")
    if data:
        handle = data['handle']
        text = data['text'].strip()
        cmd_arg = text.split(' ')
        
        
        if debugging:
            print(f'Handle: {handle}, Text: "{text}"')

        if handle in admins:
            if text.startswith(bot_prefix + 'bitcoinbot'):
                #HandleBitcoinLoop()
                print("BitCoinBot Started!")

            elif text.startswith(bot_prefix + 'clear'):
                SendPublicMessage('https://i.imgur.com/ermaaAY.jpeg')

            elif text.startswith(bot_prefix + 'check'):
                HandleRoomCheck()

            elif text.startswith(bot_prefix + 'close'):
                name = cmd_arg[1]
                HandleUserCamClose(name)
            elif text.startswith(bot_prefix + 'knownadd'):
                add_handle(cmd_arg[1])
            elif text.startswith(bot_prefix + 'knownremove'):
                remove_handle(cmd_arg[1])
            elif text.startswith(bot_prefix + 'twitchadd'):
                PlayTwitch(cmd_arg[1])
            elif text.startswith(bot_prefix + 'twitchstop'):
                StopTwitch()
            elif text.startswith(bot_prefix + 'outpost'):
                PlayOutpost()
            elif text.startswith(bot_prefix + 'song'):
                SendPublicMessage('https://soundcloud.com/semperzombie/outpost-more-like-inpost-official-version?utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing')
            elif text.startswith(bot_prefix + "nick") and handle in operators:
                HandleChangeNickname(cmd_arg[1])
            elif text.startswith(bot_prefix + 'trivia'):
                start = HandleTrivia()
                trivia = threading.Thread(target=start)
                trivia.start()
            elif text.startswith(bot_prefix + 'triviabot'):
                start = HandleTriviaBot()
                trivia = threading.Thread(target=start)
                trivia.start()         
            elif text.startswith(bot_prefix + 'uptime'):
                HandleUptime(startTime)

            elif text.startswith(bot_prefix + 'semper'):
                HandleTwitchShout()
            elif text.startswith(bot_prefix + 'guests'):
                SendPublicMessage(f"{Level0}")
            elif text.startswith(bot_prefix + 'op') and handle in operators:
                if not operator:
                    SendPublicMessage("Not today satan!")
                if len(cmd_arg) > 1:
                    operators.append(cmd_arg[1])
                    SendPublicMessage(f"{cmd_arg[1]} has been added to operators!")
                else:
                    SendPublicMessage("No user specified.")
            elif text.startswith(bot_prefix + 'deop') and handle in operators:
                if not operator:
                    SendPublicMessage("Not today satan!")
                if len(cmd_arg) > 1:
                    operators.remove(cmd_arg[1])
                    SendPublicMessage(f"{cmd_arg[1]} has been removed from operators!")
                else:
                    SendPublicMessage("No user specified.")
        elif text.startswith(bot_prefix + 'handle'):
            send = f"Your handle is: {handle}. {bot_prefix}op {handle}"
            SendPublicMessage(str(handle))
        elif text.startswith(bot_prefix + 'urb'):
            msg = ' '.join(cmd_arg[1:])
            urb = funmanager.HandleUrb(msg)
            SendPublicMessage(urb)

        elif text.startswith(bot_prefix + 'wiki'):
            msg = ' '.join(cmd_arg[1:])
            wiki = funmanager.get_wikipedia_summary(msg)
            SendPublicMessage(wiki)
        elif text.startswith(bot_prefix + 'gpt'):
            #Elenora
            
            user_input = ' '.join(cmd_arg[1:])
            HandleGPT(user_input)

        elif text.startswith(bot_prefix + 'rpg'):
            #Elenora
            
            user_input = ' '.join(cmd_arg[1:])
            HandleRPG(user_input)
        elif text.startswith(bot_prefix + 'image'):
            #Elenora
            
            user_input = ' '.join(cmd_arg[1:])
            HandleGPTImage(user_input)

        elif text.startswith(bot_prefix + 'imgur') and handle in operators:
            if not operators:
                SendPublicMessage("Not today satan!")
            if len(cmd_arg) > 1:
                query = ' '.join(cmd_arg[1:]) 
                image_links = funmanager.search_imgur(query)
                
                SendPublicMessage(f" {image_links} ")
            else:
                SendPublicMessage("No search query specified.")
        elif text.startswith(bot_prefix + 'yt') and handle in operators:
                
            YoutubeAdd(cmd_arg[1])
            print(f"Playing {cmd_arg[1]}!")

        #### everyone

        
        elif text.startswith(bot_prefix + 'roll'):
            roll = funmanager.HandleRoll()
            SendPublicMessage(roll)

        elif text.startswith(bot_prefix + 'scope') or text.startswith(bot_prefix + 'horoscope'):
            sign = cmd_arg[1].lower()
            sign_id = funmanager.get_sign_id(sign)
            if sign_id:
                horoscope = funmanager.get_horoscope_from_web(sign_id)
                SendPublicMessage(horoscope)
            else:
                SendPublicMessage("Invalid zodiac sign. Please try again.")
        elif text.startswith(bot_prefix + 'advice'):
            advice = funmanager.HandleAdvice()
            SendPublicMessage(advice)

        elif text.startswith(bot_prefix + 'dice'):
            dice = funmanager.HandleRoll()
            SendPublicMessage(dice)
        elif text.startswith(bot_prefix + 'btc'):
            btc = funmanager.HandleBitcoins()
            SendPublicMessage(btc)
     
        elif text.startswith(bot_prefix + 'ltc'):
            ltc = funmanager.HandleLiteCoins()
            SendPublicMessage(ltc)
        elif text.startswith(bot_prefix + 'flip'):
            flip = funmanager.HandleFlip()
            SendPublicMessage(flip)
        elif text.startswith(bot_prefix + 'mood'):
            mood = funmanager.HandleMood()
            SendPublicMessage(mood)
        elif text.startswith(bot_prefix + 'line'):
            line = funmanager.HandleOneLiner()
            SendPublicMessage(line)
        elif text.startswith(bot_prefix + 'fact'):
            animal = funmanager.HandleAnimal()
            SendPublicMessage(animal)
        elif text.startswith(bot_prefix + 'joke'):
            joke = funmanager.HandleJoke()
            SendPublicMessage(joke)
        elif text.startswith(bot_prefix + 'dadjoke'):
            dad = funmanager.HandleDadJoke()
            SendPublicMessage(dad)
        elif text.startswith(bot_prefix + 'cookie'):
            cookie = funmanager.HandleFortune()
            SendPublicMessage(cookie)
        elif text.startswith(bot_prefix + 'mom'):
            mom = funmanager.HandleMom()  # Giggity
            SendPublicMessage(mom)
        elif text.startswith(bot_prefix + 'dad'):
            dad = funmanager.HandleDadJoke()  # Giggity
            SendPublicMessage(dad)
        elif text.startswith(bot_prefix + 'cn'):
            chuck = funmanager.HandleChuckNorris()
            SendPublicMessage(chuck)

        elif text.startswith(bot_prefix + 'gank'):
            SendPublicMessage('God\'s gift to woman.')

        elif text.startswith(bot_prefix + '8ball'):
            if len(cmd_arg) < 2:
                SendPublicMessage('Must have a question!')
            else:
                ballz = funmanager.Handle8Ball()
                SendPublicMessage(ballz)

        elif text.startswith(bot_prefix + 'cheers'):
            HandleCheers()
        
        elif "spamfairy" in text:
            SendPublicMessage("Hello, how can i help?")
        elif text.startswith(bot_prefix + 'bald'):
            SendPublicMessage("I'm balding!")
        elif text.startswith(bot_prefix + 'brunch'):
            SendPublicMessage("buncha brunch hat wearin emo fags!")
        else:    
            pass

def HandlePrivateMessage(data):
    if data:
        try:
            handle = data.get('handle')
            text = data.get('text', '').strip()       
            sec_key = secretkey

            if text.startswith(bot_prefix + sec_key):
                if handle not in operators:
                    operators.append(handle)
                if handle not in Level4:
                    Level4.append(handle)
                if debugging:
                    print(f"OPERATORS: {operators}")
                SendPrivateMessage(handle, "You have been added to operators.")
                time.sleep(0.6)
                SendPublicMessage(f"{handle} has entered the secretkey and gains Super Rights.")
            if handle is None:
                if debugging:
                    print(f"[Error] Missing 'handle' in private message data: {data}")
                return

            if not text:
                if debugging:
                    print(f"[Error] Empty message text from handle {handle}")
                return

            cmd_arg = text.split(' ')
            
            print(f'[Private Message] Handle: {handle}, Text: "{text}"')
            #SendPrivateMessage(handle, text)

        except KeyError as e:
            print(f"[Error] Missing expected key in private message data: {e}")
        except Exception as e:
            print(f"[Unexpected Error] {e}")


def HandleUserJoin(data):
    #print(f"HandleUserJoin: {data}\n")
    global debugging
    global guestnamesallowed
    global guestallowed
    global cambans
    # {"stumble":"join","backgroundcolor":"#9566EC","namebackgroundcolor":"#26655F",
    # "messagetextcolor":"#FFFFFF","avatar":0,"handle":"1073907",
    # "username":"69bc3e2c-3b57-46d0-b4b3-41cf6e1c12c6","guest":1,"nick":"p0zkr3w","mod":0}
    backgroundcolor = data['backgroundcolor']
    namebackgroundcolor = data['namebackgroundcolor']
    username = data['username']
    nickname = data['nick']
    mod = data['mod']
    handle = data['handle']
    isguest = data['guest']
    
    for handler in banned_handles:
        cambans.append(handler)
        #ws.send(json.dumps({'stumble': 'close', 'handle': handler}))
        print(handler)
    funny_gifts = [
        "giant rubber duck", "fake mustache kit", "whoopee cushion", "tiny cactus plant",
        "giant novelty pen", "inflatable crown", "mini disco ball", "pet rock",
        "fake lottery ticket", "dinosaur costume for pets", "unicorn horn for cats",
        "world's tiniest violin", "banana phone case", "mystery box", "squirrel feeder hat",
        "DIY sock puppet kit", "selfie toaster", "shower wine glass holder",
        "invisible ink pen", "USB-powered dancing Santa"
    ]
    getgift = random.choice(funny_gifts)
    
    #SendPublicMessage('Welcome to the room %s: %s (Level %s).' % (nickname, handle, mod))
    if mod == 0: #GUEST

        if guestnamesallowed == False:
            if kob:
                ws.send(json.dumps({'stumble': 'kick', 'handle': handle}))
            else:
                ws.send(json.dumps({'stumble': 'kick', 'handle': handle}))
        
        if greet:
            SendPublicMessage(f'Welcome Guest {nickname}\nYou get a {getgift}.')
        if debugging:
            print('[HandleUserJoin] %s(Level %s) has joined the room!' % (nickname, mod))
        if nickname not in Level0:
            Level0.append(nickname)
            if debugging:
                print("[User Join] %s added to Guests!" % nickname)


    if mod == 1: #EVERYONE
        if greet:
            SendPublicMessage(f'Welcome to the room {nickname}\nYou get a {getgift}.')
        if debugging:
            print('[Operator Join] %s(Level %s) has joined the room!' % (nickname, mod))
        if nickname not in Level1:
            Level1.append(nickname)
            if debugging:
                print("[User Join] %s added to everyone!" % nickname)

    if mod == 2: #OPERATOR
        if greet:
            SendPublicMessage(f'Welcome to the room {nickname}\nyou get a {getgift}')
        if debugging:
            print('[Moderator Join] %s(Level %s) has joined the room!' % (nickname, mod))
        if nickname not in Level2:
            Level2.append(nickname)
            operators.append(handle)
            if debugging:
                print("[User Join] %s added to Operators!" % nickname)

    if mod == 3: #COWNER
        if greet:
            SendPublicMessage(f'Welcome to the room {nickname}\nyou get a {getgift}')
        if debugging:
            print('[CoOwner Join] %s(Level %s) has joined the room!' % (nickname, mod))
        if nickname not in Level3:
            Level3.append(nickname)
            operators.append(handle)
            if debugging:
                print("[User Join] %s added to CoOwners!" % nickname)

    if mod == 4: #ADMIN
        if greet:
            SendPublicMessage(f'Welcome to the room Admin {nickname}\n You get a {getgift}.')
        if debugging:
            print('[Admin Join] %s(Level %s) has joined the room!' % (nickname, mod))
        if nickname not in Level4:
            Level4.append(nickname)
            operators.append(handle)
            if debugging:
                print("[User Join] %s added to Admins!" % nickname)

    if debugging:
        print(f"OPERATORS: {operators}")
        #print(f"USERS: {userlist}")
def HandleRoomCheck():
    roomcount = len(Level0)
    SendPublicMessage(str(roomcount))

def HandleProducers(data):
    #print(f"HandleProducers: {data}")
    producers = data['producers']
    #print(producers)
    
    for producer in producers:
        handle = producer['handle']
        
        
        if debugging:

            print(f'{handlename}:{handle} is broadcasting!')
            #SendPublicMessage(f"{handle} is broadcasting!")
def HandleQuit(data):
    handle = data['handle']
    print('%s has left the room!' % handle)
    userdata = {"username": username, "handle": handle}
    del userdata['username']
    del userdata['handle']
    
    if handle in Level0:
        Level0.remove(handle)
        SendPublicMessage(f"{handle} left the room.")
    elif handle in Level1:
        Level1.remove(handle)
        SSendPublicMessage(f"{handle} left the room.")
    elif handle in Level2:
        Level2.remove(handle)
        SendPublicMessage(f"{handle} left the room.")
    elif handle in Level3:
        Level3.remove(handle)
        SendPublicMessage(f"{handle} left the room.")
    elif handle in Level4:
        Level4.remove(handle)
        SendPublicMessage(f"{handle} left the room.")

def HandleUserlist(data):
    producers = data['users']
    
    #print("[HandleUserList]")
    for producer in producers:
        user_handle = producer['handle']
        user_avatar = producer['avatar']
        user_chatcolor = producer['chatcolor']
        user_namecolor = producer['namecolor']
        user_username = producer['username']
        user_nick = producer['nick']
        user_mod = producer['mod']
        print(producer)

def HandleCallBack(data):
    #print("[DATA] " + data)
    try:
        
        decode = json.loads(data)
        #print(decode)
        event = decode['stumble']
        if event.startswith("0"):
            Handle_Ping()
            pass
        if event == 'producers':
            handle = decode['producers'][0]['handle']
            isvideo = decode['producers'][0]['kind']
            if "video" in isvideo:
                print(f"{handle} is broadcasting video.")
            
                if handle in operators:
                    print("Is Operator!")
                if handle == 'test':
                    ws.send(json.dumps({'stumble': 'close', 'handle': handle2}))
                if handle in banned_handles:
                
                    #ws.send(json.dumps({"stumble": "close", "handle": handle}))
                    print(f"{handle} is banned and has been closed.")
                
            if "audio" in isvideo:
                print(f"{handle} is broadcasting audio.")
                #SendPublicMessage(f"{handle} is broadcasting! @close {handle}")
        if event == 'unsubscribe':
            handle = decode['handle'] 
            #SendPublicMessage(f"{handle} has stopped broadcasting.")
        
        if event.startswith('closed'):
            reason = decode['text']
            print(f"Closed! {reason}")

        if event.startswith('sysmsg'):
            Handle_OnSys(decode)

        if event.startswith('userlist'):
            print(decode)
            HandleUserlist(decode)

        if event.startswith('youtube'):
            Handle_YoutubePlay(decode)

        if event.startswith('quit'):
            HandleQuit(decode)

        if event.startswith('msg'):
            HandlePublicMessage(decode)
            
        if event.startswith('pvtmsg'):
            HandlePrivateMessage(decode)

        if 'joined' in event:
            event_room = decode['room']
            
            Handle_Joined(decode) 

        elif 'join' in event:
            HandleUserJoin(decode) 

    except json.JSONDecodeError:
        pass
        #print("Failed to decode JSON")


def preprocess_message(message):
    message = message.replace("'", '"')
    return str(message)
def on_message(ws, message):
    #print(f"[{timestamp}] {message} (Type: {type(message)})")
    log_message(f"Received message: {message} \n")
    
    try:
        if message.startswith("0"):
            ws.send("0")    
        if message:
            message = preprocess_message(message)
            try: 
                HandleCallBack(message)
            except json.JSONDecodeError as e:
                pass

    except KeyError as e:
        print(f"{Fore.LIGHTRED_EX}Missing expected key in message: {e}{Style.RESET_ALL}")  
def on_open(ws):
    join_message = {
        "stumble": "join",
        "token": token,
        "room": room_name,
        "nick": botsname
    }
    ws.send(json.dumps(join_message))
    print(f"{Fore.LIGHTYELLOW_EX}Joined room {room_name}{Style.RESET_ALL}")

    
    endpoint = room_name

    toketimer_thread = threading.Thread(target=TokeTimerBot)
    toketimer_thread.start()
    #print("%s is online! Connected to %s" % (botsname, endpoint))

    #SendPublicMessage("%s is online!" % botsname)
   
def on_error(ws, error):
    pass
    #print(f"{Fore.LIGHTRED_EX}Error: {error}{Style.RESET_ALL}")

def on_close(ws, close_status_code, close_msg):
    print(f"{Fore.LIGHTRED_EX}WebSocket closed with status {close_status_code}: {close_msg}{Style.RESET_ALL}")

def signal_handler(sig, frame):
    print(f"{Fore.LIGHTYELLOW_EX}Received SIGINT. Shutting down gracefully...{Style.RESET_ALL}")
    ws.close()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

endpoint, token = get_websocket_endpoint(room_name)
ws = websocket.WebSocketApp(endpoint,
                            on_message=on_message,
                            on_open=on_open,
                            on_error=on_error,
                            on_close=on_close)

print(f"{Fore.LIGHTYELLOW_EX}Starting WebSocket for room {room_name}{Style.RESET_ALL}")
ws.run_forever()
