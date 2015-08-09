#!/usr/bin/env python2

class Rover_Download_Timer(object):
    def __init__(self, N, L, B, chunks):
        pass

if __name__ == '__main__':
    #1 <= N, L, B < 2**32
    #the number of bytes in the original file.
    N = int(raw_input()) 
    #the latency of the connection in seconds.
    L = float(raw_input()) 
    #bandwidth of the connection in bytes per second.
    B = float(raw_input()) 
    #number of chunks. 1 <= C <= 100000
    C = int(raw_input())
    chunks = []
    for i in xrange(c):
        chunks.append(int(raw_input()))
    rover = Rover_Download_Timer(N, L, B, chunks)
