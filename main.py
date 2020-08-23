import requests
import os
import random
import ctypes
import threading

if not os.path.exists('Images'): os.makedirs('Images') # Makes Folder Called Images
lock = threading.Lock()
Valid = 0
Invalid = 0

def Clear(): # Simple Clear Console Function
    os.system('cls')

def UpdateTitle(): # Update The Title
    ctypes.windll.kernel32.SetConsoleTitleW("[Imgur Bruteforcer] By Dropout | Valid: %s | Invalid: %s" % (Valid, Invalid))
    
def Bruteforce(Img_Type):
    global Valid, Invalid
    Ran = ''.join(random.choice('QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcbnm123456789') for i in range(7))
    Link = f'https://i.imgur.com/{Ran}.{Img_Type}'
    img = requests.get(Link, allow_redirects=True)
    if img.url == "https://i.imgur.com/removed.png":
        lock.acquire()
        print('[\u001b[31mINVALID\u001b[37m] i.imgur.com/%s.%s' % (Ran, Img_Type))
        Invalid += 1
        UpdateTitle()
        lock.release()
    else:
        lock.acquire()
        with open(f'Images/{Ran}.{Img_Type}', 'wb') as f: f.write(img.content)
        print('[\u001b[32mVALID\u001b[37m]   i.imgur.com/%s.%s' % (Ran, Img_Type))
        Valid += 1
        UpdateTitle()
        lock.release()

if __name__ == "__main__":
    Clear()
    ctypes.windll.kernel32.SetConsoleTitleW("[Imgur Bruteforcer] By Dropout")
    print(
        '\n[\u001b[31mPNG\u001b[37m]    Bruteforce Images With A PNG Extension',
        '\n[\u001b[31mJPEG\u001b[37m]   Bruteforce Images With A JPEG Extension',
        '\n[\u001b[31mWEBP\u001b[37m]   Bruteforce Images With A WEBP Extension',
        '\n[\u001b[31mGIF\u001b[37m]    Bruteforce Images With A GIF Extension',
        '\n[\u001b[31mCUSTOM\u001b[37m] Bruteforce Images With A CUSTOM Extension\n'
    )
    Img_Type = input('\u001b[31m>\u001b[37m Image Type\u001b[32m:\u001b[37m ')
    if "PNG" in Img_Type:
        Type = 'png'
    elif "JPEG" in Img_Type:   
        Type = 'jpeg'
    elif "WEBP" in Img_Type:      
        Type = 'webp' 
    elif "GIF" in Img_Type:     
        Type = 'gif'
    elif "CUSTOM" in Img_Type:      
        Type = input('\u001b[31m>\u001b[37m Custom\u001b[32m:\u001b[37m ') 
    else:
        print('\u001b[31m>\u001b[37m Invalid Option')
        os.system('pause >NUL')    
    print()
    while True:
        for i in range(100):
            threads = threading.Thread(target=Bruteforce, args=(Type,))    
            threads.start()