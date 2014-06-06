"""Benchmarking for 3 different SockJS libraries"""

import benchmark

from tornado import web, ioloop
from sockjs.tornado import SockJSConnection, SockJSRouter
import sockjs.tornado
#from Benchmark_Tornado import TornadoChatConnection
#from Benchmark_Tornado import TornadoIndexHandler
#import logging
import tornado.web
import tornado.ioloop

import sys
import cyclone.web
from twisted.internet import reactor
from twisted.python import log
import sockjs.cyclone

from twisted.internet.protocol import Factory
from twisted.protocols.basic import LineReceiver
from twisted.internet import reactor


# class SockJS_SpeedTests(benchmark.Benchmark):
#      label = 'SockJS Speed Tests'
#      each = 100
#      participants = set()
#
#     def setupGeneral(self):
#         #self.ws = self.create_connection("ws://echo.websocket.org/")
#         pass
#
#     def setupTornado(self):
#         self.TOR_ws = self.create_connection("http://127.0.0.1:6000")
#

from sockjs.tornado import SockJSConnection, SockJSRouter
import sockjs.tornado
import tornado.web
import tornado.ioloop

class IndexHandler(tornado.web.RequestHandler):
    """Regular HTTP handler to serve the chatroom page"""
    def get(self):
        self.render('index.html')

class ChatConnection(sockjs.tornado.SockJSConnection):
    """Chat connection implementation"""
    # Class level variable
    participants = set()

    def on_open(self, info):
        # Send that someone joined
        self.broadcast(self.participants, "Someone joined.")

        # Add client to the clients list
        self.participants.add(self)

    def on_message(self, message):
        # Broadcast message
        self.broadcast(self.participants, message)

    def on_close(self):
        # Remove client from the clients list and broadcast leave message
        self.participants.remove(self)

        self.broadcast(self.participants, "Someone left.")


    # def setupTornado(self):





if __name__ == "__main__":
    import logging
    logging.getLogger().setLevel(logging.DEBUG)

    # 1. Create chat router
    TornadoRouter = sockjs.tornado.SockJSRouter(ChatConnection, '/chat')

    # 2. Create Tornado application
    tornado_app = tornado.web.Application(
            [(r"/", IndexHandler)] + TornadoRouter.urls
    )

    # 3. Make Tornado app listen on port 8080
    tornado_app.listen(8088)

    # 4. Start IOLoop
    tornado.ioloop.IOLoop.instance().start()


# if __name__ == '__main__':
#     import logging
#     logging.getLogger().setLevel(logging.DEBUG)
#
#     TornadoRouter = sockjs.tornado.SockJSRouter(
#         ChatConnection, '/chat')
#
#     TornadoApp = tornado.web.Application(
#         [(r'/', IndexHandler)],
#         TornadoRouter.urls)
#
#     TornadoApp.listen(8088)
#
#     tornado.ioloop.IOLoop.instance().start()
#
