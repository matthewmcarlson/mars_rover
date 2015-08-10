#!/usr/bin/env python2

class Rover_Download_Timer(object):
    def validator(f):
        """Validates input (throw assertion errors if parameters are outside 
        of the coinstraints given with the problem)."""
        def deco(self, N, L, B, chunks):
            assert 1 <= N< 2**32
            assert 1 <= L < 2**32
            assert 1 <= B < 2**32
            assert 1 <= len(chunks) <= 100000
            f(self, N, L, B, chunks)
        return deco

    @validator
    def __init__(self, N, L, B, chunks):
        pass

    def download_chunk_time(self, n_bytes, latency, bandwidth):
        """Returns """
        return 2*latency + n_bytes/bandwidth

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
    for i in xrange(C):
        input_ = raw_input().split(',')
        chunk = tuple(map(int, input_))
        chunks.append(chunk)
    rover = Rover_Download_Timer(N, L, B, chunks)
