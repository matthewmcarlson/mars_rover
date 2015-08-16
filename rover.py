#!/usr/bin/env python2

class Rover_Download_Timer(object):
    def validator(f):
        """Validates input (throw assertion errors if parameters are outside 
        of the coinstraints given with the problem)."""
        def deco(self, N, L, B, chunks, debug=0):
            assert 1 <= N< 2**32
            assert 1 <= L < 2**32
            assert 1 <= B < 2**32
            assert 1 <= len(chunks) <= 100000
            f(self, N, L, B, chunks, debug)
        return deco

    @validator
    def __init__(self, N, L, B, chunks, debug=0):
        """Sets all the global attributes. Note that once they're all defined,
        the compute function will be triggered and set the answer attribute.
        (See __setattr__ for details)."""
        self.DEBUG=debug
        self.pr('#'*80)
        self.N_BYTES = N
        self.LATENCY = L
        self.BANDWIDTH = B
        self.CHUNKS = sorted(chunks)

    def compute(self, n_bytes, latency, bandwidth, chunks):
        """The meat and potatoes. Returns the minimum time to fetch the file
        (or None if it's not possible)."""
        solutions = self.compute_solutions(n_bytes, latency, bandwidth, chunks)
        if solutions:
            return min(map(lambda x:x[1], solutions))

    def compute_solutions(self, n_bytes, latency, bandwidth, chunks):
        """Get a list of all possible solutions where a solution looks like:
        (start byte, stop byte, total time)."""
        solutions = []
        new_solutions = []
        ### negative startings points don't really make sense, but why not 
        ### handle them anyways?
        for index in xrange(len(chunks)):
            start, stop = chunks[index]
            if start > n_bytes:
                break
            if start <= 0:
                solutions.append((stop, self.download_chunk_time(start, stop)))
            else:
                start, stop = chunks[index]
                for sol_stop, sol_time in solutions:
                    if start <= sol_stop and stop > sol_stop:
                        time = sol_time + self.download_chunk_time(start, stop)
                        new_solutions.append((stop, time))
                self.pr(new_solutions)
                while new_solutions:
                    solutions.append(new_solutions.pop())
                # solutions.extend(new_solutions)
                self.pr(solutions)
                self.prune_solutions(solutions, start)
                ### If we've ran out of candiates, there can't be a sollution
                if not solutions:
                    return []
        for i in xrange(len(solutions)-1, -1, -1):
            stop, time = solutions[i]
            if stop < n_bytes:
                solutions.pop(i)
        self.pr(solutions)
        return solutions

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

    def prune_solutions(self, solutions, chunk_start):
        """Stop wasting cycles trying obviously bad solutions."""
        ### Iterate backwards through the list, since we might be popping 
        ### bad solutions off.
        for i in xrange(len(solutions)-1, -1, -1):
            stop, time = solutions[i]
            if chunk_start > stop:
                solutions.pop(i)
            else:
                for j in xrange(i):
                    ### If there's another solution that's faster and further
                    ### (or equal), chuck this one.
                    if solutions[j][1]<=time and solutions[j][0]>=stop:
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
            self.answer_str = Rover_Download_Timer.answer_formatter(self.answer)

    @staticmethod
    def answer_formatter(answer):
        """Split this into a seperate function in case we want to do 
        something fancier down the road"""
        ### If we don't have an answer, return the empty string
        if answer is None:
            ret = ''
        else:
            ret = '{}'.format(answer)
            ### This is a bit of a hack, but from reading the str.format docs
            ### I can't find a way to make it fill with zeros. Normally I would
            ### search the internet and see if there's a solution, but that's
            ### not allowed here. Hence the hack.
            try:
                ret +='0'*(len(ret)-ret.index('.'))
            ### answers should always be floats because we took care that 
            ### latencies and bandwidth should always be floats
            except ValueError:
                ret+='.000'
        return ret

    def pr(self, s):
        if self.DEBUG: print s

if __name__ == '__main__':
    #1 <= N, L, B < 2**32
    ### The number of bytes in the original file.
    N = int(raw_input()) 
    ### The latency of the connection in seconds.
    L = float(raw_input()) 
    ### Bandwidth of the connection in bytes per second.
    B = float(raw_input()) 
    ### Number of chunks. 1 <= C <= 100000
    C = int(raw_input())
    chunks = []
    for i in xrange(C):
        input_ = raw_input().split(',')
        chunk = tuple(map(int, input_))
        chunks.append(chunk)
    rover = Rover_Download_Timer(N, L, B, chunks)
    if rover.answer_str:
        print rover.answer_str
    