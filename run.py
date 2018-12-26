# -*- coding: utf-8 -*-
import os

import tornado.ioloop
import tornado.web

# from backend.handler import BaseRequestHandler
from backend import views


PROJ_ROOT = os.path.dirname(os.path.abspath(__name__))
favicon_path = os.path.join(PROJ_ROOT, 'favicon.ico')
robots_path = os.path.join(PROJ_ROOT, 'robots.txt')
static_path = os.path.join(PROJ_ROOT, 'static')
node_modules_path = os.path.join(PROJ_ROOT, 'node_modules')
template_path = os.path.join(PROJ_ROOT, 'templates')
settings = {
    'debug': True,
    'static_url_prefix': '/static/',
    'static_path': static_path,
    'template_path': template_path,
    'xsrf_cookies': True,
    'cookie_secret': 'very safe and secret string'
}
handlers = [
    (r'/favicon.ico', tornado.web.StaticFileHandler, {'path': favicon_path}),
    (r'/robots.txt', tornado.web.StaticFileHandler, {'path': robots_path}),
    (r'/static/(.*)', tornado.web.StaticFileHandler, {'path': static_path}),
    (r'/node_modules/(.*)', tornado.web.StaticFileHandler, {'path': node_modules_path}),
]
handlers.extend([
    (r'/', views.IndexView),
    (r'/diff/?', views.DiffView),
])
port = 13579
application = tornado.web.Application(handlers, **settings)
application.listen(port, address='0.0.0.0')
print('visit by: http://127.0.0.1:{0}/'.format(port))
tornado.ioloop.IOLoop.instance().start()
