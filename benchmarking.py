"""Benchmarking for 3 different SockJS libraries"""

import benchmark

import websocket

from tornado import web, ioloop, websocket
from sockjs.tornado import SockJSConnection, SockJSRouter
import sockjs.tornado

import sys
import cyclone.web
from twisted.internet import reactor
from twisted.python import log
import sockjs.cyclone

from twisted.internet.protocol import Factory
from twisted.protocols.basic import LineReceiver
from twisted.internet import reactor


class SockJS_SpeedTests(benchmark.Benchmark):
    label = 'SockJS Speed Tests'
    each = 100

    def setupGeneral(self):
        #self.ws = self.create_connection("ws://echo.websocket.org/")
        pass

    def setupTornado(self):
        self.TOR_ws = self.create_connection("ws://echo.websocket.org/")


        pass


    # def setupTornado(self):
    #
    #     self.EchoRouter = SockJSRouter(TornadoEchoConnection, '/echo')
    #
    #     self.app = web.Application(self.EchoRouter.urls)
    #     self.app.listen(6000)
    #     self.ioloop.IOLoop.instance().start()

    def TestTornado(self):


        return ""


class TornadoEchoConnection(SockJSConnection):
    participants = set()

    def on_message(self, msg):
        self.send(msg)
