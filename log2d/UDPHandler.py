"""
UDPHandler.py
A 'logging' (and hence log2d) datagram handler that sends a log
message to an arbitrary UDP port as a json dict. Json is used as it
is faster and mores secure than pickle (has issues)

V0.1  2/12/22  MDP alpha

"""
import json
import logging
import logging.config
import logging.handlers
import struct
import socket
from logging.handlers import SocketHandler




"""  Typical json log record
{'name': 'testlogname', 'msg': 'My log message', 'args': None, 'levelname': 'DEBUG', 
'levelno': 10, 'pathname': '/home/mike/PythonProjects/log2d/log2d/log2d/__init__.py', 
'filename': '__init__.py', 'module': '__init__', 'exc_info': None, 'exc_text': None, 
'stack_info': None, 'lineno': 119, 'funcName': '__call__', 'created': 1670015256.365754, 
'msecs': 365.7538890838623, 'relativeCreated': 27.306079864501953, 'thread': 140241014282048, 
'threadName': 'MainThread', 'processName': 'MainProcess', 'process': 72843, 'command': 'LOG'}

Not required items

ignoreList = ['args', 'pathname', 'exc_info', 'exc_text', 'stack_info', 'lineno',
    'filename', 'msecs', 'relativeCreated', 'thread', 'threadName', 'processName', 'process']

"""

_ignoreList = ['pathname', 'exc_info', 'exc_text', 'stack_info', 'lineno',
    'filename', 'msecs', 'relativeCreated', 'thread', 'threadName', 'processName', 'process'] # args


class UDPHandler(logging.handlers.DatagramHandler):  # Inherit from logging.Handler
    """
    Handler class which writes logging records, in json format, to
    a UDP socket.  The logRecord's dictionary (__dict__), is abstracted 
    for required items which makes it a smaller packet to transmit and 
    simpler to decode at the recieving end - just use json.dumps()
    """

    def __init__(self, host, port):
        """
        Initializes the handler with a specific host address and port.
        Host can be ip or name - 'localhost', '<broadcast>' etc.
        """
        SocketHandler.__init__(self, host, port)
        self.closeOnError = False

    def makeSocket(self):
        """
        The factory method of SocketHandler is here overridden to create
        a UDP socket (SOCK_DGRAM).
        """
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        s.settimeout(5)
        return s

    def send(self, s: bytes):
        """
        Send the jason string to the socket.
        """
        if self.sock is None:
            self.createSocket()
        self.sock.sendto(s, self.address)

    def makePickle(self, record) -> str:
        """
        Convert the message data to json dump, prefixed with length
        """
        exInf = record.exc_info
        if exInf:
            # TODO: sort any traceback text 
            _ = self.format(record)
        # Will only work when record only contains json serialisable objects
        M = dict(record.__dict__)
        # Hardwire just to LOG stuff at this stage - find etc later
        M['command'] = 'LOG'
        # Add two formatting strings
        M['datefmt'] = self.formatter.datefmt
        M['fmt'] = self.formatter._fmt
        msg = M.get("msg", record.getMessage())
        M['msg'] = msg
        # pop other crap we don't need
        #for item in _ignoreList:
        #    M.pop(item, None)
        # Now return preceed by 4 byte length
        d = json.dumps(M, default=str).encode()
        dl = struct.pack(">L", len(d))
        return dl + d