#!/usr/bin/env python2

from rover import Rover_Download_Timer



tests = [((2000, 15, 10, 7, 
           [(0,200), (200,400), (400,600), (600,800), 
            (800,1000), (1000,2000),(0,1800)]), 
          340.000),
         ((2000, 5, 10, 7, 
           [(0,200), (200,400), (400,600), (600,800), 
            (800,1000), (1000,2000),(0,1800)]), 
          260.000),
]

for input_, expected_result in tests:
    N, L, B, C, chunks = input_
    rover = Rover_Download_Timer(N, L, B, chunks)    
    res = rover.answer
    if res == expected_result:
        print 'Pass!'
    else:
        print '{res} = Rover_Download_Timer({inp})'.format(res=res, inp=input_)
        print '(epected {ex})!'.format(expected_result)