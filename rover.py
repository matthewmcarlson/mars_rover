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
        """Sets all the global attributes. Note that once they're all defined,
        the compute function will be triggered and set the answer attribute.
        (See __setattr__ for details)."""
        self.DEBUG=2
        self.pr('#'*80)
        self.N_BYTES = N
        self.LATENCY = L
        self.BANDWIDTH = B
        self.CHUNKS = sorted(chunks)

    def compute(self, n_bytes, latency, bandwidth, chunks):
        """The meat and potatoes."""
        solutions = self.compute_solutions(n_bytes, latency, bandwidth, chunks)
        if solutions:
            return min(map(lambda x:x[2], solutions))


    def compute_solutions(self, n_bytes, latency, bandwidth, chunks):
        """"""
        solutions = []
        ### negative startings points don't really make sense, but why not 
        ### handle them anyways?
        for index in xrange(len(chunks)):
            start, stop = chunks[index]
            if start <= 0:
                solutions.append((start, stop, 
                                  self.download_chunk_time(start, stop)))
            else:
                break
        for index in xrange(index, len(chunks)):
            new_solutions = []
            start, stop = chunks[index]
            for sol_start, sol_stop, sol_time in solutions:
                if start <= sol_stop and stop > sol_stop:
                    time = sol_time + self.download_chunk_time(start, stop)
                    new_solutions.append((sol_start, stop, time))
            solutions.extend(new_solutions)
            self.pr(new_solutions)
            self.pr(solutions)
            self.prune_solutions(solutions)
        ret = filter(lambda x:x[1]>=n_bytes, solutions)
        return ret

    def prune_solutions(self, solutions):
        ### iterate backwards through the list
        for i in xrange(len(solutions)-1, -1, -1):
            start, stop, time = solutions[i]
            for j in xrange(i):
                ### if there's another solution that's faster and further
                ### (or equal), chuck this one.
                if solutions[j][2]<=time and solutions[j][1]>=stop:
                    solutions.pop(i)
                    break

    def __setattr__(self, attr, val):
        """If the user tweaks one of the input values, recompute the answer."""
        ### Attrs that trigger a recompute
        essential_attrs = ('CHUNKS', 'N_BYTES', 'LATENCY', 'BANDWIDTH')
        ### Latency and Bandwidth should always be floats so that the answer 
        ### will always be a float
        if attr in ('LATENCY', 'BANDWIDTH'):
            object.__setattr__(self, attr, float(val))
        else:
            object.__setattr__(self, attr, val)
        ### Only recompute if all of the neccesary attributes are defined and
        ### the attributes that was changed is one that effects the answer.
        if (all(map(lambda x:hasattr(self, x), essential_attrs)) and
            attr in essential_attrs):
            self.answer = self.compute(self.N_BYTES, 
                                   self.LATENCY, 
                                   self.BANDWIDTH, 
                                   self.CHUNKS)

    def download_chunk_time(self, start, stop, latency=None, bandwidth=None):
        """Returns how long it takes to download a given chunk"""
        if latency is None:
            latency = self.LATENCY
        if bandwidth is None:
            bandwidth = self.BANDWIDTH
        # if start > stop:
        #             return 2*latency + (start - stop)/bandwidth
        # else:
        return 2*latency + (stop - start)/bandwidth

    def pr(self, s):
        if self.DEBUG: print s

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
    pprint = '{:.4}'.rover.answer
    print pprint
    