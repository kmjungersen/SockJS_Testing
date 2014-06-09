import cyclone.web
from twisted.internet import reactor

import sockjs.cyclone
import time
import webbrowser

class CycloneIndexHandler(cyclone.web.RequestHandler):
    """ Serve the chat html page """
    def get(self):
        self.render('Static/index.html')


class CycloneChatConnection(sockjs.cyclone.SockJSConnection):
    """ Chat sockjs connection """
    participants = set()
    MessageCount = 0
    MessageTarget = 100
    MessageStartTime = 0
    MessageStopTime = 0
    SetupStopTime = 0
    TeardownStartTime = 0
    Summary = ''

    def connectionMade(self, info):
        with open('SetupStopTime.txt', 'w') as SetupStopFile:
            self.SetupStopTime = time.time()
            SetupStopFile.writelines(self.SetupStopTime)

        self.participants.add(self)

        with open('MessageStartTime.txt', 'w') as MessageStartFile:
            self.MessageStartTime = time.time()
            MessageStartFile.writelines(self.MessageStartTime)


    def messageReceived(self, message):

        self.broadcast(self.participants, message)
        self.MessageCount += 1
        if self.MessageCount == self.MessageTarget:
            self.close()

    def connectionLost(self):

        with open('MessageStopTime.txt', 'w') as MessageStopFile:
            self.MessageStopTime = time.time()
            MessageStopFile.writelines(self.MessageStopTime)

        # self.Summary += '=========================================\n'
        # self.Summary += 'CYCLONE SUMMARY\n'
        # self.Summary += str(self.MessageCount)
        # self.Summary += ' total messages were sent/received in '
        # self.Summary += str(self.MessageStopTime - self.MessageStartTime)
        # self.Summary += ' seconds.\n'
        # self.Summary += '=========================================\n'

        with open('TeardownStartTime.txt', 'w') as TeardownStartFile:
            self.TeardownStartTime = time.time()
            TeardownStartFile.writelines(self.TeardownStartTime)

        #print self.Summary

        self.participants.remove(self)
        reactor.stop()


def ServerSetup(port):

    CycloneRouter = sockjs.cyclone.SockJSRouter(CycloneChatConnection, '/chat')

    app = cyclone.web.Application( [ (r"/", CycloneIndexHandler) ] +
                                   CycloneRouter.urls )
    reactor.listenTCP(port, app)
    address = 'http://127.0.0.1:' + str(port)
    webbrowser.open_new_tab(address)
    reactor.run()

#ServerSetup(8010)