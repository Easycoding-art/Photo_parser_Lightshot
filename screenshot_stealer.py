import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import random
from progress.bar import Bar
from PIL import Image, ImageChops, UnidentifiedImageError
import os
import colorama
from colorama import Fore
colorama.init()
from art import * 
text = text2art("Easycoding-art", "random",)
text2 = text2art("presents...", "random",)
fore_color = random.randint(1, 7)
if fore_color == 1 :
    print(Fore.RED + text)
elif fore_color == 2 :
    print(Fore.GREEN + text)
elif fore_color == 3 :
    print(Fore.YELLOW + text)
elif fore_color == 4 :
    print(Fore.BLUE + text)
elif fore_color == 5 :
    print(Fore.MAGENTA + text)
elif fore_color == 6 :
    print(Fore.CYAN + text)
elif fore_color == 7 :
    print(Fore.WHITE + text)

fore_color_2 = random.randint(1, 7)
if fore_color_2 == 1 :
    print(Fore.RED + text2)
elif fore_color_2 == 2 :
    print(Fore.GREEN + text2)
elif fore_color_2 == 3 :
    print(Fore.YELLOW + text2)
elif fore_color_2 == 4 :
    print(Fore.BLUE + text2)
elif fore_color_2 == 5 :
    print(Fore.MAGENTA + text2)
elif fore_color_2 == 6 :
    print(Fore.CYAN + text2)
elif fore_color_2 == 7 :
    print(Fore.WHITE + text2)

def parse(images):
    symbols = "qwertyuiopasdfghjklzxcvbnm1234567890"
    symbols_list = list(symbols)
    code_list = [""]*images
    number = 0
    bar = Bar('Parsing', max=images)
    for number in range(images) :
        error = 1
        while error != 0 :
            code = ""
            for letter in range(6) :
                i = random.randint(0, len(symbols_list) - 1)
                code = code + str(symbols_list[i])
            file  = open('used_codes.txt', 'r')
            for line in file :
                used_code = file.read(6)
                url = "https://prnt.sc/" + code
                headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 YaBrowser/19.10.2.195 Yowser/2.5 Safari/537.36'}
                html = requests.get(url, headers=headers).text
                soup = bs(html, 'lxml')
                img_tag = soup.find('img', {'id': 'screenshot-image'})
                if img_tag == None :
                    error = 1
                    break
                photo_url = img_tag['src']
                arr = list(photo_url)
                if code == used_code or arr[0] != "h" :
                    error = 1
                    break
                else :
                    error = 0
            file.close()
        file  = open('used_codes.txt', 'a')
        file.write(code)
        file.close()
        url = "https://prnt.sc/" + code
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 YaBrowser/19.10.2.195 Yowser/2.5 Safari/537.36'}
        html = requests.get(url, headers=headers).text
        soup = bs(html, 'lxml')
        img_tag = soup.find('img', {'id': 'screenshot-image'})
        if img_tag != None :
            photo_url = img_tag['src']
            photo = requests.get(photo_url, headers=headers).content
            with open('Unsorted/' + code + '.png', 'wb') as f:
                f.write(photo)
        code_list[number] = code
        number+=1
        bar.next()
    bar.finish()

    cracked=Image.open('cracked_screenshot.png')
    ads=Image.open('ads.png')
    deleted = 0
    bar_delete = Bar('Deleting trash', max=images)
    for number in range(0, images) :
        try:
            test_image=Image.open('Unsorted/' + code_list[number] + '.png')
        except UnidentifiedImageError:
            file_path = 'Unsorted/' + code_list[number] + '.png'
            os.remove(file_path)
            deleted+=1
        else :
            test_image=Image.open('Unsorted/' + code_list[number] + '.png')
            result=ImageChops.difference(test_image.convert('RGB'), cracked.convert('RGB'))
            w, h = result.size
            err = 0
            for x in range(w):
                for y in range(h):
                    r, g, b = result.getpixel((x, y))
                    if r == 0 and g == 0 and b == 0 :
                        err+=1
            if err == w*h :
                file_path = 'Unsorted/' + code_list[number] + '.png'
                os.remove(file_path)
                deleted+=1
            else :
                result=ImageChops.difference(test_image.convert('RGB'), ads.convert('RGB'))
                w, h = result.size
                err = 0
                for x in range(w):
                    for y in range(h):
                        r, g, b = result.getpixel((x, y))
                        if r == 0 and g == 0 and b == 0 :
                            err+=1
                if err == w*h :
                    file_path = 'Unsorted/' + code_list[number] + '.png'
                    os.remove(file_path)
                    deleted+=1
        bar_delete.next()
    bar_delete.finish()
    print("Done! Deleteted " + str(deleted) + " usless files")
    return deleted

if __name__ == '__main__' :
    if not os.path.exists("Unsorted") :
        os.mkdir("Unsorted")
    images_number = int(input(Fore.GREEN +"Количество скриншотов: "))
    while images_number != 0 :
        images_number = parse(images_number)