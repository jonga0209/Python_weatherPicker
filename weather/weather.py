# -*- coding: utf-8 -*-
#pip install bs4
#pip install html5lib

from urllib.request import urlopen, Request
import urllib
import bs4

class weather:

    def __init__(self):
        self.location ='서울'
        self.temperature =''


    def __str__(self):
        print('현재 ' + self.location + ' 날씨는 ' + self.temperature + '도 입니다.')

        #return self.location

    def setLocation(self):
        self.location = input("지역을 입력해주세요: ")

    def getWeather(self):
        enc_location = urllib.parse.quote(self.location + '+날씨')
        url = 'https://search.naver.com/search.naver?ie=utf8&query=' + enc_location
        req = Request(url)
        page = urlopen(req)
        html = page.read()
        soup = bs4.BeautifulSoup(html, 'html5lib')
        self.temperature = soup.find('p', class_='info_temperature').find('span',class_='todaytemp').text
        #print(self.temperature)





if __name__ == '__main__':
    weather = weather()
    weather.setLocation()
    weather.getWeather()
    weather.__str__()
