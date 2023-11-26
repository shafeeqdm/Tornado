import tornado.web
import tornado.ioloop

class basicRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello world")

class staticRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("a.html")

class evenorodd(tornado.web.RequestHandler):
    def get(self):
        n = int(self.get_argument("n"))
        r = "odd" if n % 2 else "even"
        self.write(f"{n} is {r}")

class idcheck(tornado.web.RequestHandler):
    def get(self , id):
        self.write(f"he has entered {id}")

if __name__ == "__main__":
    app = tornado.web.Application([ 
        (r"/", basicRequestHandler),
        (r"/blog", staticRequestHandler),
        (r"/even", evenorodd),
        (r"/checkid/([0-9]+)", idcheck)
    ])

    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()