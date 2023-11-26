import tornado.web
# from . import *
import os
from config import *
from schemas import *


class indexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")
    
class blogHandler(tornado.web.RequestHandler):
    def post(self):
        uid = self.get_argument("username")
        password = self.get_argument("password")
        self.write(f"{uid}{password}")
                
