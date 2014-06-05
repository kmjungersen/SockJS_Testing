# import execjs
#
# node = execjs.get()
# js = "function() {" \
#      "var sock = 1;" \
#      "return sock}()"
#
# sockjs = "function() {" \
#          "var conn = new SockJS('http://127.0.0.1:6000');" \
#          "conn.send(\"hello world\");" \
#          "} ()"
#
# print node.eval(js)

from twisted.internet import protocol, reactor

class Echo(protocol.Protocol):
    def dataReceived(self, data):
        self.transport.write(data)
        print data

class EchoFactory(protocol.Factory):
    def buildProtocol(self, addr):
        return Echo()

reactor.listenTCP(1234, EchoFactory())
reactor.run()