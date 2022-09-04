
import os

import requests

import wget

class APOD:
    api_key = os.environ.get('apod_api_key')
    def img(self, file_path):
        data = requests.get(f"https://api.nasa.gov/planetary/apod?api_key={self.api_key}").json()
        url = data['hdurl']
        filename = wget.download(url)

        
        return file_path+filename, data
    
    
    
    def imgByDate(self, date,file_path):
        data = requests.get(f"https://api.nasa.gov/planetary/apod?api_key={self.api_key}&date={date}").json()
        url = data['hdurl']
        filename = wget.download(url) 
        
        return file_path+filename, data
if __name__ == '__main__':

    im = APOD()
    print(im.img('./'))
    print(im.imgByDate('2006-11-06','./'))
