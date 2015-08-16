#!/usr/bin/env python2

from rover import Rover_Download_Timer



tests = [
         ### First example given
         ((2000, 15, 10, 7, 
           [(0,200), (200,400), (400,600), (600,800), 
            (800,1000), (1000,2000),(0,1800)]), 
          '340.000'),
         ### Second example given
         ((2000, 5, 10, 7, 
           [(0,200), (200,400), (400,600), (600,800), 
            (800,1000), (1000,2000),(0,1800)]), 
          '260.000'),
         ### The third test case given
         ((2000, 10, 10, 9, 
           [(0,200), (200, 400), (400, 600), (600, 800), (800, 1000), 
            (1200, 1400),(1400, 1600),(1600, 1800),(1800, 2000)]), 
          ''),

         ### Negative indexes okay?
         ((2000, 15, 10, 7, 
           [(0,200), (200,400), (400,600), (600,800), 
            (800,1000), (1000,2000),(-10,1790)]), 
          '340.000'),
         ### No valid solution
         ((20000, 15, 10, 7, 
           [(0,200), (200,400), (400,600), (600,800), 
            (800,1000), (1000,2000),(-10,1800)]), 
          ''),
         ### proper formatting of large numbers
         ((20000, 15, 10, 1, 
           [(0,20000)]), 
          '2030.000'),
         ### don't keep going once we get all the bits we need
         ((2000, 5, 10, 7, 
           [(0,200), (200,400), (400,600), (600,800), 
            (800,1000), (1000,2400), (2200, 2600), (0,1800)]), 
          '300.000'),
]

for input_, expected_result in tests:
    N, L, B, C, chunks = input_
    rover = Rover_Download_Timer(N, L, B, chunks, debug=0)
    res = rover.answer_str
    if res == expected_result:
        print 'Pass!'
    else:
        print '{res} = Rover_Download_Timer({inp})'.format(res=res, inp=input_)
        print '(epected {ex})!'.format(ex = expected_result)