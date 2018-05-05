
'''
A really dirty attempt to capture traffic camera jpgs to a file by camera and by day


'''

import urllib.request
from datetime import datetime
import os
import time

cameraDict = {

    'I-5  Washington - Vancouver at SR-14': 'https://images.wsdot.wa.gov/sw/005vc00050.jpg',
    'I-84 at 148th': 'https://tripcheck.com/roadcams/cams/i84@148th_pid1579.jpg',
    'I-84 at 53rd': 'https://tripcheck.com/roadcams/cams/i8453rd_pid580.jpg',
    'I-84 at Grand': 'https://tripcheck.com/roadcams/cams/i84grand_pid584.jpg',
    'I-84 at Metro Bldg.': 'https://tripcheck.com/roadcams/cams/i84metro_pid588.jpg',
    'I-5 at Morrison': 'https://tripcheck.com/roadcams/cams/i5morrison_pid569.jpg',
    'I-205 at Killingsworth': 'https://tripcheck.com/roadcams/cams/i205Killingsworth_pid534.jpg',
    'I-84 at 223rd': 'https://tripcheck.com/roadcams/cams/i84@223rd_pid1582.jpg',
    'I-84 at 67th': 'https://tripcheck.com/roadcams/cams/i8467th_pid581.jpg',
    'I-84 at 37th': 'https://tripcheck.com/roadcams/cams/i8437th_pid579.jpg',
    'I-84 at Celilo': 'https://tripcheck.com/RoadCams/cams/I-84%20at%20Celilo_pid2748.JPG',
    'I-5 at North Albany': 'https://tripcheck.com/roadcams/cams/NorthAlbany_pid1489.jpg',
    'Portland - 8th at Division': 'https://tripcheck.com/roadcams/cams/8th%20at%20Division_pid3189.JPG',
    'US97 at Colorado': 'https://tripcheck.com/RoadCams/cams/US97%20at%20Colorado_pid3157.JPG'
}


count = -1
while True:
    count = (count+1) % 5
    if count == 0 and 4 < datetime.now().hour < 22:
        for camera in cameraDict.keys():
            cameraName = camera
            image = cameraDict[camera]
            if not os.path.exists(cameraName):
                os.makedirs(cameraName)
            cameraDir = os.path.join(os.getcwd(), cameraName)
            fileDay = str(datetime.now()).split(' ')[0]
            path = os.path.join(cameraDir, fileDay)
            if not os.path.exists(path):
                os.makedirs(path)
            fileTime = str(datetime.now()).split('.')[0]
            filename = cameraName + ' ' + fileTime
            file = os.path.join(path, filename)
            imagefile = open(file + ".jpg", 'wb')
            try:
                imagefile.write(urllib.request.urlopen(image).read())
            except Exception as err:
                imagefile.close()
                os.remove(file + '.jpg')
                print(str(err) + ' ' + filename)
            time.sleep(1)
    time.sleep(24)
