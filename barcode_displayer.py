#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os

picdir = os.path.join('/home/pi/Documents/eMod/sample/e-Paper/RaspberryPi&JetsonNano/python', 'pic')
libdir = os.path.join('/home/pi/Documents/eMod/sample/e-Paper/RaspberryPi&JetsonNano/python/', 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)


import logging
import time
from PIL import Image,ImageDraw,ImageFont
from waveshare_epd import epd2in9
import traceback
import barcode

def barcode_displayer(displayed_code: str) -> None:
    try:
        epd = epd2in9.EPD()

        epd.init(epd.lut_full_update)
        #epd.Clear(0xFF)
        
        ean = barcode.get('code128', displayed_code, writer = barcode.writer.ImageWriter())
        image = ean.render()

        epd.display(epd.getbuffer(image.resize((epd.height, epd.width))))

        time.sleep(1)


    except IOError as e:
        logging.info(e)
        
    except KeyboardInterrupt:    
        logging.info("ctrl + c:")
        epd2in9.epdconfig.module_exit()
        exit()

    except Exception as e:
        logging.info(str(e))

    finally:
        epd.Clear(0xFF)


if __name__ == '__main__':
    barcode_displayer(str('5651332000156513321001'))
