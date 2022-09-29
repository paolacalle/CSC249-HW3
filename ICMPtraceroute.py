# Attribution: this assignment is based on ICMP Traceroute Lab from Computer Networking: a Top-Down Approach by Jim Kurose and Keith Ross. 
# It was modified for use in CSC249: Networks at Smith College by R. Jordan Crouser in Fall 2022

from socket import *
from ICMPpinger import checksum
import os
import sys
import struct
import time
import select
import binascii

ICMP_ECHO_REQUEST = 8
MAX_HOPS = 30
TIMEOUT = 2.0
TRIES = 2

# The packet that we shall send to each router along the path is the ICMP echo
# request packet, which is exactly what we had used in the ICMP ping exercise.
# We shall use the same packet that we built in the Ping exercise
def build_packet():
    # In the sendOnePing() method of the ICMP Ping exercise, firstly the header of our
    # packet to be sent was made, secondly the checksum was appended to the header and
    # then finally the complete packet was sent to the destination.
    #---------------#
    # Fill in start #
    #---------------#

    myChecksum = 0

    ID = os.getpid() & 0xFFFF  # copied off ICMPpinger.py doOnePing method, not sure how else to define ID

    header = struct.pack("bbHHh", ICMP_ECHO_REQUEST, 0, myChecksum, ID, 1)

    data = struct.pack("d", time.time())

    myChecksum = checksum(''.join(map(chr, header + data)))

    if sys.platform == 'darwin':
        # Convert 16-bit integers from host to network byte order
        myChecksum = htons(myChecksum) & 0xffff
    else:
        myChecksum = htons(myChecksum)

    # Append checksum to the header.
    header = struct.pack("bbHHh", ICMP_ECHO_REQUEST, 0, myChecksum, ID, 1)
        # TODO: Make the header in a similar way to the ping exercise.
        
    #-------------#
    # Fill in end #
    #-------------#

    # Don’t send the packet yet , just return the final packet in this function.
    packet = header + data
    return packet

def get_route(hostname):
    timeLeft = TIMEOUT
    for ttl in range(1,MAX_HOPS):
        for tries in range(TRIES):
            destAddr = gethostbyname(hostname)

            #---------------#
            # Fill in start #
            #---------------#
            #currentProtocol = "ICMP" #https://pythontic.com/modules/socket/getprotobyname, oh I just noticed pinger uses it
            icmp = getprotobyname("icmp")
            mySocket = socket(AF_INET, SOCK_RAW, icmp)
            # TODO: Make a raw socket named mySocket

            #-------------#
            # Fill in end #
            #-------------#

            mySocket.setsockopt(IPPROTO_IP, IP_TTL, struct.pack('I', ttl))
            mySocket.settimeout(TIMEOUT)

            try:
                d = build_packet()
                mySocket.sendto(d, (hostname, 0))
                t= time.time()
                startedSelect = time.time()
                whatReady = select.select([mySocket], [], [], timeLeft)
                howLongInSelect = (time.time() - startedSelect)

                if whatReady[0] == []: # Timeout
                    print(" * * * Request timed out...")

                recvPacket, addr = mySocket.recvfrom(1024)
                timeReceived = time.time()
                timeLeft = timeLeft - howLongInSelect

                if timeLeft <= 0:
                    print(" * * * Request timed out!")

            except timeout:
                continue

            else:
                #---------------#
                # Fill in start #
                #---------------#
                icmpHeader = recvPacket[20:21]
                types = struct.unpack('b', icmpHeader)[0]
                #recType, recCode, recChecksum, recID, recSequence = struct.unpack('bbHHh', icmpHeader)
                print(types)
                    #TODO: Fetch the icmp type from the IP packet

                #-------------#
                # Fill in end #
                #-------------#
                
                if types == 11:
                    bytes = struct.calcsize("d")
                    timeSent = struct.unpack("d", recvPacket[28:28 +bytes])[0] #I used this for pinger
                    print(" %d rtt=%.0f ms %s" %(ttl, (timeReceived -t)*1000, addr[0]))

                elif types == 3:
                    bytes = struct.calcsize("d")
                    timeSent = struct.unpack("d", recvPacket[28:28 + bytes])[0]
                    print(" %d rtt=%.0f ms %s" %(ttl, (timeReceived-t)*1000, addr[0]))

                elif types == 0:
                    bytes = struct.calcsize("d")
                    timeSent = struct.unpack("d", recvPacket[28:28 + bytes])[0]
                    print(" %d rtt=%.0f ms %s" %(ttl, (timeReceived - timeSent)*1000, addr[0]))
                    return

                else:
                    print("error")

                break

            finally:
                mySocket.close()

#get_route("smith.edu")
#get_route("delallama.net")
#get_route("goldrestaurant.co.za")
get_route("eatandcook.asia")

