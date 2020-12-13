#!/usr/bin/env python
import os
import optparse
import scapy.all as scapy


def getIP():
    parser = optparse.OptionParser()
    parser.add_option("-g", "--address", dest="ip", help="Your router gateway, by default it should be something like 192.168.1.0 or 192.168.1.1, if you don't know what is a gateway go learn networking boy !")
    (options, arguments) = parser.parse_args()
    if not options.ip:
        parser.error("Please specify a gateway you want to scan using -g or --address, if you need help you can also run --help")
    return options.ip

def scan(ip):
    scapy.arping(ip) #Send arp request to the specified IP address

ip = getIP()
scan(ip + "/24")


