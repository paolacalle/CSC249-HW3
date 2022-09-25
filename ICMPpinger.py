# Attribution: this assignment is based on ICMP Pinger Lab from Computer Networking: a Top-Down Approach by Jim Kurose and Keith Ross. 
# It was modified for use in CSC249: Networks at Smith College by R. Jordan Crouser in Fall 2022

from socket import * 
import os
import sys 
import struct 
import time 
import select 
import binascii


ICMP_ECHO_REQUEST = 8

# -------------------------------------
# This method takes care of calculating
#   a checksum to make sure nothing was
#   corrupted in transit.
#  
# You do not need to modify this method
# -------------------------------------


def checksum(string):  #input: string is pram of checksum; ouput: a string (based on the info on this string it is determined if some sort of failures occured?)
    csum = 0
    countTo = (len(string) // 2) * 2 #wouldn't this just cancel the 2 out? why do this?
    count = 0

    while count < countTo: 
        thisVal = ord(string[count+1]) * 256 + ord(string[count]) #ord returns the unicode associated with a character 
        csum = csum + thisVal #checsum value is added to the value unicode count value 
        csum = csum & 0xffffffff 
        count = count + 2 #count increments by 2
    
    
    if countTo < len(string): #runs only if countTo is less than the length of the given string 
        csum = csum + ord(string[len(string) - 1]) #if the length of the string is less than countTo, it updates csum to be the sum of csum and unicode of string length menus one
        csum = csum & 0xffffffff

    csum = (csum >> 16) + (csum & 0xffff) #>> shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off
    csum = csum + (csum >> 16) 

    answer = ~csum #Inverts all the bits

    answer = answer & 0xffff
 
    answer = answer >> 8 | (answer << 8 & 0xff00) 
    return answer

#a socket is end point of communication 
def receiveOnePing(mySocket, ID, timeout, destAddr): 
    
    timeLeft = timeout #used for TTL tracking?
    
    while True:
        startedSelect = time.time() #returns the number of seconds passed since epoch (transmitting data back/forth) 

        whatReady = select.select([mySocket], [], [], timeLeft) 
        howLongInSelect = (time.time() - startedSelect) #how much time from started time till select has passed
        if whatReady[0] == []: # Timeout if the data that is ready is empty 
            return "Request timed out."

        timeReceived = time.time() #caluate the amount time to data finally be recieved 
        recPacket, addr = mySocket.recvfrom(1024) #reads 1024 number of bits sent from mySocket at a time
        #recvfrom() Returns a bytes object read from mySocket and the address of the client socket as a tuple.
        #---------------#
        # Fill in start #
        #---------------#
        icmpHeader = recPacket[20:28] #breaks packect into ICMP header, which starts at 20bytes (160 bits) and ends at 28 bytes (224 bits)
        #requestType, code, revChecksum, revId, revSequence = struct.unpack('bbHHh',icmpHeader)
            # TODO: Fetch the ICMP header from the IP packet

        type = icmpHeader[0:1]
        code = icmpHeader[1:2]
        checksum = icmpHeader[2:4]
        ID = icmpHeader[0:2]
        sequence = icmpHeader[2:4]

        #-------------#
        # Fill in end #
        #-------------#

        timeLeft = timeLeft - howLongInSelect 
        
        if timeLeft <= 0:
            return "Request timed out."



def sendOnePing(mySocket, destAddr, ID):
    # Header is type (8), code (8), checksum (16), id (16), sequence (16)
    myChecksum = 0

    # Make a dummy header with a 0 checksum
 
    # struct -- Interpret strings as packed binary data
    header = struct.pack("bbHHh", ICMP_ECHO_REQUEST, 0, myChecksum, ID, 1) 
    data = struct.pack("d", time.time())

    # Calculate the checksum on the data and the dummy header. 
    myChecksum = checksum(''.join(map(chr, header+data)))

    # Get the right checksum, and put in the header 
    if sys.platform == 'darwin':
        # Convert 16-bit integers from host to network byte order 
        myChecksum = htons(myChecksum) & 0xffff
    else:
        myChecksum = htons(myChecksum)

    header = struct.pack("bbHHh", ICMP_ECHO_REQUEST, 0, myChecksum, ID, 1) 
    packet = header + data

    mySocket.sendto(packet, (destAddr, 1)) # AF_INET address must be tuple, not str 
    # Both LISTS and TUPLES consist of a number of objects
    # which can be referenced by their position number within the object.



def doOnePing(destAddr, timeout): 
    icmp = getprotobyname("icmp")

    # SOCK_RAW is a powerful socket type. For more details:	
    # http://sock-raw.org/papers/sock_raw

    mySocket = socket(AF_INET, SOCK_RAW, icmp)

    myID = os.getpid() & 0xFFFF # Return the current process i 
    sendOnePing(mySocket, destAddr, myID)
    delay = receiveOnePing(mySocket, myID, timeout, destAddr)
 
    mySocket.close() 
    return delay


def ping(host, timeout=1):

    # timeout=1 means: If one second goes by without a reply from the server,

    # the client assumes that either the client's ping or the server's pong is lost 
    dest = gethostbyname(host)
    print("Pinging " + dest + " using Python:") 
    print("")

    # Send ping requests to a server separated by approximately one second 
    while True :
        delay = doOnePing(dest, timeout) 
        print(delay)
        time.sleep(1) # one second 
    return delay

# Runs program
ping("google.com")
