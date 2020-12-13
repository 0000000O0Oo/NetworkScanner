#!/usr/bin/env python
#Make sure to run on python3.8 and under, python3.9 does not work with scapy.

import os
import optparse
import scapy.all as scapy

def getIP():
    parser = optparse.OptionParser()
    parser.add_option("-g", "--address", dest="ip", help="Your router gateway, by default it should be something like 192.168.1.0 or 192.168.0.1, if you don't know what is a gateway go learn networking boy !")
    (options, arguments) = parser.parse_args()
    if not options.ip:
        parser.error("Please specify a gateway you want to scan using -g or --address, if you need help you can also run --help")
    return options.ip


def scan(ip):
    arp_request = scapy.ARP(pdst=ip) #ARP Packet Object
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff") #Ethernet Frame with Broadcast MAC Address
    arp_request_broadcast = broadcast/arp_request #Scapy allows to combine using a forward slash
    iterator = 1
    answered_list = scapy.srp(arp_request_broadcast, timeout=1)[0]
    print("-----------------------------------------------\nIP\t\t\tMAC Address\n-----------------------------------------------")

    for element in answered_list:
        #print("[+] Client Found [#{0}]".format(iterator))
        #print(element[1].show())
        print(element[1].psrc + "\t\t" + element[1].hwsrc)
        #print("-> IP Address : " + element[1].psrc)
        #print("-> MAC Address : " + element[1].hwsrc + "\n")
        iterator+=1
    
ip = str(getIP()) + "/24"
scan(ip)

    
