import base64
from io import BytesIO
from PIL import Image


class ImageTranform:
    def to_base64(self, response):
        '''
        Converts PIL image to Base64
        '''
        image = Image.open(BytesIO(response.content))
        buffered = BytesIO()
        image.save(buffered, format="PNG")
        img_str = base64.b64encode(buffered.getvalue()).decode()
        return img_str
    
    def to_PIL_image(self, img_str):
        '''
        Converts base64 image to PIL image.
        '''
        image_bytes = base64.b64decode(img_str)
        buffer = BytesIO(image_bytes)
        img = Image.open(buffer)
        return img
