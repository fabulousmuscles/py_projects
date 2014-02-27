#!/usr/bin/env python
#########################################
## A very simple port scanner written in python. Doesn't have much yet in terms
## of error checking (e.g. for bad input). It goes through a sequence of
## port numbers and attempts to connect to each one. I also added the
## method 'bye' that attempts to gracefully close the connection (if one is
## made) because I noticed that when I had a simple node.js echo server
## running, and this port scanner connected to it and then abruptly
## disconnected, it threw ECONNRESET, likely because the message sent out by
## the echo server wasn't read (see: http://stackoverflow.com/a/2979806).
## So the 'bye' method was introduced to prevent that error. The 'bye' method
## itself is modified from:
## http://code.activestate.com/recipes/408997-when-to-not-just-use-socketclose/
#########################################

import socket

# note that 1 is not subtracted from MAX b/c it's going to be used in xrange
MAX = pow(2, 16)
MIN = 1


def main(prompt):
    print "Welcome."
    print "Enter the host IP you'd like scanned (default is localhost)"
    host = prompt()
    host = host if host else '127.0.0.1'
    print("Enter the port number where the scanner should BEGIN scanning "
          "(default is 1).")
    port1 = prompt()
    port1 = int(port1) if port1 else MIN
    print("Enter the port number where the scanner should END scanning "
          "(default is 65535).")
    port2 = prompt()
    port2 = int(port2) if port2 else MAX
    print "Beginning scan..."
    conn(host, port1, port2)


def myprompt():
    return raw_input("> ")


def bye(s, host):
    """Attempts to 'gracefully' close the connection."""
    s.shutdown(1)
    result = []
    while True:
        message = s.recv(2)
        if not message:
            break
        result.append(message)
    s.close()
    if result:
        print "The host '%s' said: " % host + ''.join(result).strip('\n')


def conn(host, port1, port2):
    socket.setdefaulttimeout(2)
    count = 0
    for port in xrange(port1, port2):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((host, port))
            print "Successfully connected to port %d" % port
            count += 1
            bye(s, host)
        except socket.error:
            s.close()
            pass
    if not count:
        print "No open ports found."
    else:
        print "Found %d open ports." % count

if __name__ == "__main__":
    main(myprompt)
