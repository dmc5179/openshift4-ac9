import socketserver
#from datetime import datetime
import time

class SyslogUDPHandler(socketserver.BaseRequestHandler):
    """
    Simple server that listens for syslog messages and searches for login attempts
    """

    def handle(self):

        data = bytes.decode(self.request[0].strip(), encoding="utf-8")

        print('At {} recieved following message: {}'.format(time.time(), data))

if __name__ == "__main__":

    HOST, PORT = "0.0.0.0", 12312

    print('Starting syslog processing')

    server = socketserver.UDPServer((HOST, PORT), SyslogUDPHandler)
    #self defined variables which are needed in handle()

    #handle requests until explicit shutdown(), see python docs
    server.serve_forever()
