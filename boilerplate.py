from seleniumbase import BaseCase
import logging

class WebScraper(BaseCase):
    def __init__(self, url):
        super().__init__()
        self.url = url
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(messag  
e)s')
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)
        self.logger.addHandler(  
stream_handler)