import re
import os
from flask import current_app
from authlib.jose import jwt, JoseError
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
from base64 import b64encode
import string
import random

def isVaildEmail(email:str) -> bool:
    email = email.strip().lower();
    pattern = '^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$';
    return re.match(
        pattern,
        email
    );

def isVaildPassword(password:str) -> bool:
    pattern = '^(?![0-9]+$)(?![a-zA-Z]+$)[0-9A-Za-z]{6,}$';
    return re.match(
        pattern,
        password
    )

def generateToekn(*args,**kwargs) -> str:
    header = { 'alg': 'HS256' };

    key = current_app.secret_key;

    return jwt.encode(
        header=header,
        payload=kwargs,
        key=key,
        check=True
    ).decode();


def generateSessionId() -> str:
    return os.urandom(4).hex();


class CaptchaGenerator:

    def __init__(self, width=250, height=60, font_size=48,number:int=4,font:str=None):

        self.number = number

        self.width = width

        self.height = height

        self.font_size = font_size

        self.chars = string.ascii_letters + string.digits  # 验证码字符集合

        self.bgcolor = (255, 255, 255)  # 图片背景颜色

        self.linecolor = (random.randint(0, 128), random.randint(0, 128), random.randint(0, 128))  # 干扰线颜色

        self.dotcolor = (random.randint(0, 128), random.randint(0, 128), random.randint(0, 128))  # 干扰点颜色

        self.fontcolor = (random.randint(0, 128), random.randint(0, 128), random.randint(0, 128))  # 字体颜色

        self.font = None

        if font is not None:
            if os.path.exists(font):
                self.font = font
                # self.font = ImageFont.truetype(
                #     os.path.join(font),
                #     self.font_size
                # )

    def generate_captcha_code(self):
        return ''.join(random.choice(self.chars) for _ in range(self.number))


    def generate_captcha(self,format=None):

        captcha_text = self.generate_captcha_code()

        image = Image.new('RGB', (self.width, self.height), self.bgcolor)

        draw = ImageDraw.Draw(image) 
        
        if not self.font:
            font = ImageFont.load_default().font_variant(size=self.font_size)  
        else:
            font = ImageFont.truetype(
                os.path.join(self.font),
                self.font_size
            )
        

        for i in range(5):

            x1 = random.randint(0, self.width)

            y1 = random.randint(0, self.height)

            x2 = random.randint(0, self.width)

            y2 = random.randint(0, self.height)

            draw.line((x1, y1, x2, y2), fill=self.linecolor, width=3)


        # 绘制干扰点

        for i in range(200):

            x = random.randint(0, self.width)

            y = random.randint(0, self.height)

            draw.point((x, y), fill=self.dotcolor)


        # 绘制验证码文字，包括阴影效果

        for i, char in enumerate(captcha_text):

            shadow_offset = random.randint(0, 3)

            shadow_color = (0, 0, 0)

            draw.text((20 + i * 50 + shadow_offset, 5 + shadow_offset), char, font=font, fill=shadow_color)  # 绘制阴影效果的文字

            draw.text((20 + i * 50, 5), char, font=font, fill=self.fontcolor)

        data = BytesIO()
        image.save(data,format='PNG')
        dataBytes = data.getvalue()
        imageData = b64encode(dataBytes).decode()
        return imageData,captcha_text;