from tornado import web, ioloop, websocket
from sockjs.tornado import SockJSConnection, SockJSRouter
import sockjs.tornado


class TornadoEchoConnection(SockJSConnection):
    participants = set()

    def on_open(self, msg):
        joe = "asdfasdfafsdf" \
              "asdfasdf"