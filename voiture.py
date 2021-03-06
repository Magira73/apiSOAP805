from spyne import Application, rpc, ServiceBase, Iterable, Integer, Unicode
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
import lxml
import spyne
from wsgiref.simple_server import WSGIServer
from wsgiref.simple_server import make_server


import logging
import os

voitureL = [["Renault Zoe", 395, 3], ["Tesla Model 3", 602, 1.5], ["Volkswagen ID. 3", 425, 1.33], ["Porsche Taycan", 463, 1] ]

class Voiture(ServiceBase):
    @rpc(_returns=Iterable(Unicode))
    def list_voitures(ctx):
        for i in range(len(voitureL)):
            for j in range(len(voitureL[i])):
                yield u'%s' % voitureL[i][j]

"""
application = Application([Voiture], 'spyne.examples.hello.soap',
                          in_protocol=Soap11(validator='lxml'),
                          out_protocol=Soap11())


wsgi_application = WsgiApplication(application)


if __name__ == '__main__':

    server = make_server('127.0.0.1', 8080, wsgi_application)
    server.serve_forever()
"""

if __name__=='__main__':
  try:
      from wsgiref.simple_server import make_server
  except ImportError:
      print ("Error: server requires Python >= 2.5")

  logging.basicConfig(level=logging.INFO)
  logging.getLogger('rpclib.protocol.xml').setLevel(logging.DEBUG)

  application = Application([Voiture], 'org.temporary.soap',
               in_protocol=Soap11(), out_protocol=Soap11())

  port = int(os.environ.get('PORT', 5000))

  server = make_server('0.0.0.0', port, WsgiApplication(application))

  print ("listening to http://0.0.0.0:%s" % port)
  print ("wsdl is at: http://0.0.0.0:%s/?wsdl" % port)

  server.serve_forever()
