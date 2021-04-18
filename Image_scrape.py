import requests
from bs4 import BeautifulSoup
import os

def get_images(url, folder):
    #url = 'https://unsplash.com/s/photos/dna'
    os.mkdir(os.path.join(os.getcwd(), folder))
    os.chdir(os.path.join(os.getcwd(), folder))
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    atags = soup.find_all('a', {'class' : '_2Mc8_'})
    for link in atags:
        urls = 'https://unsplash.com' + link['href']
        titles = link['title']
        with open(titles + '.jpg', 'wb') as f:
            out = requests.get(urls)
            f.write(out.content)
            print('downloaded: ', titles)
            

get_images('https://unsplash.com/s/photos/rna', 'output')