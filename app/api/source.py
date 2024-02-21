import requests
from app.config.settings import settings
from app.helpers.image import ImageTranform


class ThirdParty:
    def __init__(self) -> None:
        self.base_url = settings.pokemon_api_url
        self.image_transform = ImageTranform()
    
    def handle_requests(self, url: str, req_data: bool=True):
        '''
        Perform get request to provided url.
        '''
        try:
            response = requests.get(url) 
        except Exception as e:
            print("RequestsError", e)
        if req_data and response:
            return response
        
    def get_source_data(self, url: str=''):
        if not url:
            url = self.base_url
        response = self.handle_requests(url)
        if response:
            response = response.json()
        return response
        
    def parse_data(self, data):
        '''
        Parse the dict data to extract required information.
        '''
        if isinstance(data, dict):
            img_url = data.get('sprites').get('front_default')
            img_str = self.get_base64_image(img_url)
            types = []
            for type in data['types']:
                types.append(type['type']['name'])

            types = ', '.join(types)
            return img_str, types
        return [None] * 2
    
    def get_base64_image(self, url: str):
        '''
        download image data and convert to base64 string.
        '''
        try:
            response = self.handle_requests(url)
            return self.image_transform.to_base64(response)
        except Exception as e:
            print('Error', e)
            return None


        
            
            



