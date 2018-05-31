# coding: utf-8

from twisted.internet import protocol, reactor


class Echo(protocol.Protocol):
    def dataReceived(self, data):
        print "Client said:", data
        self.transport.write(data)


class EchoFactory(protocol.Factory):
    def buildProtocol(self, addr):
        return Echo()


reactor.listenTCP(9000, EchoFactory())
reactor.run()
