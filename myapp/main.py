import tornado.ioloop
from controllers.handler import *

if __name__ == "__main__":
    app = tornado.web.Application([
                             (r"/",indexHandler),
                             (r"/blog",blogHandler) 
                                             
                                        ])
    print("app running")
    http_server =  tornado.httpserver.HTTPServer(app)
    http_server.listen(8123)
    tornado.ioloop.IOLoop.current().start()
 