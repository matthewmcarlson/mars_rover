# mars_rover
Counsyl Programming Challenge- Mars Rover 


Mars Rover

Mars Rover

While working the night shift in the Mars Rover control room at a certain Space Agency, you get an urgent message from the rover that it has captured the first ever photographic evidence of water flowing on the surface of Mars. Excitedly, you begin the procedure for transmitting the image back to Earth. However, to your dismay you realize that some negligent government contractor has bungled writing the software for the image storage system on the rover. In the name of "redundancy" (and presumably a larger contract), instead of simply storing the file in one contiguous block, the contractor has directed the software to split the image file up into many smaller chunks that overlap seemingly at random.

Undeterred, but in a rush to make sure that the picture makes it into the morning's papers, you put your thinking cap on to figure out how to get the file to Earth in time. If you try to download all of the chunks it will take far too long. But perhaps if you're smart you can still reconstruct the image file with only a subset of the chunks.

The rover has already sent you an index of the starting and ending byte positions of each of the file chunks with respect to the original file. Doing the math in your head, you determine that the radio connection from Earth to the rover has a latency of L seconds (and likewise, from the rover to the Earth). In addition, the connection has a bandwidth of B bytes / second. So to download a chunk of size S bytes would takes 2 * L seconds of round-trip time to initiate the download, followed by S / B seconds to transfer the chunk itself. Unfortunately the radio link is such that only one connection can be active at any given time (so no sending out another request before the previous one has finished).

Your mission now is to determine, given the constants L, B, and the byte indices of each chunk, the optimal set of chunks to download such that the total time is minimized. Assume that all local computation time Earth-side and on the rover is negligible.
Input

The input will be provided to your program via standard input.

The first line contains integer N, the number of bytes in the original file.

The second line contains integer L, the latency of the connection in seconds.

The third line contains integer B, the bandwidth of the connection in bytes per second.

The fourth line contains integer C, the number of chunks.

C lines follow, each formatted as A,B, with integer A being the byte index of the start of the chunk, and integer B being the byte index of the end of the chunk. These are zero-indexed byte intervals [A, B), meaning that they contain all byte indices i, such that A <= i < B.
Output

Output the minimum amount of time, in seconds, it would take to download sufficient chunks to reconstruct the original file given the assumptions listed above. Round your answer to 3 decimal places. If it is impossible to reconstruct the original file given the chunks provided, do not output anything.
Constraints

1 <= N, L, B < 2**32
1 <= C <= 100000

Sample Input 1

2000
15
10
7
0,200
200,400
400,600
600,800
800,1000
1000,2000
0,1800

Sample Output 1

340.000

Sample Input 2

2000
5
10
7
0,200
200,400
400,600
600,800
800,1000
1000,2000
0,1800

Sample Output 2

260.000

Explanation

In the first example, latency dominates the transfer time for the small chunks. It's better to download the two large chunks [0, 1800) (210 seconds) and [1000, 2000) (130 seconds) for a total time of 340 seconds and eat the additional overlap rather than download the smaller chunks (total time of 380 seconds).

In the second example, no inputs change except the value of L has been decreased from 15 seconds down to 5 seconds. This means that it is now preferable to download all of the smaller chunks (total time of 260 seconds) instead of the two big chunks (total time of 300 seconds).