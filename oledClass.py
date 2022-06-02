import time

import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import time

class display:

    def __init__(self):
        RST = 24
        # Note the following are only used with SPI:
        DC = 23
        SPI_PORT = 0
        SPI_DEVICE = 0

        # 128x64 display with hardware I2C:
        self.disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST)

        # Initialize library.
        self.disp.begin()

        # Clear display.
        self.disp.clear()
        self.disp.display()

    def bienvenida(self):
        image = Image.open('panda1.ppm').convert('1')

        # Alternatively load a different format image, resize it, and convert to 1 bit color.
        #image = Image.open('happycat.png').resize((disp.width, disp.height), Image.ANTIALIAS).convert('1')

        # Display image.
        self.disp.image(image)
        self.disp.display()
        time.sleep(.8)

        image2 = Image.open('panda2.ppm').convert('1')
        self.disp.image(image2)
        self.disp.display()
        time.sleep(.8)

    def menu(self):
        width = self.disp.width
        height = self.disp.height
        image = Image.new('1', (width, height))

        # Get drawing object to draw on image.
        draw = ImageDraw.Draw(image)

        # Draw a black filled box to clear the image.
        draw.rectangle((0,0,width,height), outline=0, fill=0)

        # Draw some shapes.
        # First define some constants to allow easy resizing of shapes.
        padding = 2
        shape_width = 20
        top = padding
        bottom = height-padding
        # Move left to right keeping track of the current x position for drawing shapes.
        x = padding

        # Load default font.
        font = ImageFont.load_default()

        draw.text((x+25, top+10), '****MENU****', font=font, fill=255)
        draw.text((x, top+25), '1.- Snake', font=font, fill=255)
        draw.text((x, top+40), '2.- Tennis', font=font, fill=255)

        # Display image.
        self.disp.image(image)
        self.disp.display()

    def showText(self, txt):
        width = self.disp.width
        height = self.disp.height
        image = Image.new('1', (width, height))

        # Get drawing object to draw on image.
        draw = ImageDraw.Draw(image)

        # Draw a black filled box to clear the image.
        draw.rectangle((0,0,width,height), outline=0, fill=0)

        # Draw some shapes.
        # First define some constants to allow easy resizing of shapes.
        padding = 2
        shape_width = 20
        top = padding
        bottom = height-padding
        # Move left to right keeping track of the current x position for drawing shapes.
        x = padding

        # Load default font.
        font = ImageFont.load_default()

        draw.text((x, top+25), txt, font=font, fill=255)

        # Display image.
        self.disp.image(image)
        self.disp.display()
