Use this file to record your reflection on this assignment and answer the prompts.

What worked, what didn't, what advice would you give someone taking this course in the future?

What did not work was me not reading all the directions before attempting this assignment! What did work was going through each method on both files and using that as hints as how to write my own code. Not sure if was cheating, but at lot of the functions/code lines that I used to complete the assignment came from code lines that were already written. I had to just modify it a bit to accommodate what I needed it to do. That said, doing this gave me a better understanding of how the methods co-work with each-other. Thus, I 100%%%%% recommend someone who takes this course to do this. Also, I googled so may of the functions (I ONLY KNEW what PRINT() did) and asked so many questions to the wonderful TA because I did not know what I 99.99% of it was doing.  Now, I probably only understant 50% of it, but I have a better understanding of how pinging (reciving and sending), ICMP, Checksum, unpacking/packing, and sockets, which I think was the ultimately the goal. 

Test your `ping` and `traceroute` programs on 4 target hosts, each on a different continent and include the output below.

1) North America (www.smith.edu): 
- Ping:
  0.003838062286376953
  0.010593175888061523
  0.0324709415435791
  0.005795955657958984
  0.004724979400634766
  0.013242244720458984
  0.013152122497558594
  0.013080835342407227
  0.012907981872558594
  0.012464761734008789
  0.012155294418334961
  0.004115104675292969
  0.0116729736328125
  0.004176139831542969
  0.004024982452392578
  0.013306140899658203
  0.0042171478271484375
  0.0033309459686279297
  0.012936115264892578
  0.012952089309692383
  0.013070821762084961
  0.012637138366699219
  0.0044710636138916016
  0.003126859664916992
  0.004830121994018555
  0.013279914855957031
  0.027652978897094727
  0.004448652267456055
  0.012754201889038086
  0.004770994186401367
  0.004249095916748047
  0.0042569637298583984
  0.007372140884399414
  0.01346898078918457
  0.013153076171875
  0.01306605339050293
  0.013396978378295898
  0.006736040115356445
  0.013213157653808594
  0.013229131698608398
  0.01310110092163086
  0.004410982131958008
  0.012722969055175781
  0.004673004150390625
  0.011526823043823242
 
- traceroute: 
11
 1 rtt=26 ms 131.229.41.254
11
 2 rtt=21 ms 131.229.11.113
0
 3 rtt=6 ms 131.229.65.117

 11 rtt=16 ms 142.250.80.46


2) South America (delallama.net)
- Ping: 
  0.014039039611816406
  0.014246225357055664
  0.022465944290161133
  0.022463083267211914
  0.02237224578857422
  0.021872997283935547
  0.022505998611450195
  0.022839069366455078
  0.022291183471679688
  0.02855086326599121
- Trace Route:
11
 1 rtt=19 ms 131.229.41.254
11
 2 rtt=20 ms 131.229.11.113
11
 3 rtt=20 ms 131.229.10.104
11
 4 rtt=4 ms 134.241.249.33
11
 5 rtt=4 ms 69.16.1.33
11
 6 rtt=6 ms 18.2.136.89
11
 7 rtt=10 ms 64.57.20.18
11
 8 rtt=18 ms 163.253.1.11
11
 9 rtt=17 ms 163.253.1.229
11
 10 rtt=17 ms 163.253.2.123
 * * * Request timed out...
 * * * Request timed out...
0
 12 rtt=23 ms 199.232.37.84
 
3) Africa (goldrestaurant.co.za)
- Ping: 
0.3105592727661133
0.28642988204956055
0.3663771152496338
0.3251469135284424
0.3257558345794678
0.32546186447143555
0.32552289962768555
0.35232114791870117
- Traceroute: 
11
 1 rtt=18 ms 131.229.41.254
11
 2 rtt=43 ms 131.229.11.113
11
 3 rtt=24 ms 131.229.10.104
11
 4 rtt=4 ms 134.241.249.33
11
 5 rtt=4 ms 69.16.1.33
11
 6 rtt=5 ms 18.2.136.89
11
 7 rtt=8 ms 64.57.20.18
11
 8 rtt=24 ms 163.253.1.11
11
 9 rtt=21 ms 163.253.1.229
11
 10 rtt=21 ms 163.253.1.116
11
 11 rtt=22 ms 163.253.1.133
11
 12 rtt=112 ms 206.126.236.147
11
 13 rtt=19 ms 193.5.122.151
 * * * Request timed out...
 * * * Request timed out...
 * * * Request timed out...
 * * * Request timed out...
 * * * Request timed out...
 * * * Request timed out...
 * * * Request timed out...
 * * * Request timed out...
 * * * Request timed out...
 * * * Request timed out...
11
 19 rtt=351 ms 80.84.20.31
11
 20 rtt=402 ms 41.84.12.108
11
 21 rtt=267 ms 41.84.12.37
11
 22 rtt=274 ms 41.84.12.161
11
 23 rtt=355 ms 192.168.14.5
 * * * Request timed out...
 * * * Request timed out!
11
 24 rtt=329 ms 41.66.132.246

4) Asia (eatandcook.asia)
- Ping:
  0.36000585556030273
  0.3267672061920166
  0.3278348445892334
  0.3427317142486572
  0.3129699230194092
  0.32327699661254883
  0.3308398723602295
  0.325242280960083
  0.32875609397888184
  0.3266129493713379
  0.32698774337768555
  0.32553696632385254
  0.3286902904510498
  0.3265879154205322
  0.3253469467163086
  0.3269917964935303
  0.32582998275756836
  0.3256850242614746
  0.3252739906311035
  0.3306140899658203
  0.3307068347930908
  0.3295130729675293
  0.3254399299621582
  0.3297438621520996
  0.32570719718933105
  0.3015320301055908
  0.3079230785369873
- Traceroute: 
11
 1 rtt=17 ms 131.229.41.254
11
 2 rtt=25 ms 131.229.11.113
11
 3 rtt=17 ms 131.229.10.104
11
 4 rtt=4 ms 134.241.249.33
11
 5 rtt=4 ms 69.16.1.33
11
 6 rtt=7 ms 69.16.0.9
11
 7 rtt=7 ms 38.104.218.13
11
 8 rtt=8 ms 154.54.40.181
11
 9 rtt=15 ms 154.54.40.154
11
 10 rtt=21 ms 154.54.40.106
11
 11 rtt=37 ms 154.54.7.158
11
 12 rtt=49 ms 154.54.24.146
11
 13 rtt=50 ms 154.54.88.226
11
 14 rtt=45 ms 154.54.9.46
 * * * Request timed out...
11
 15 rtt=373 ms 66.110.57.145
11
 16 rtt=305 ms 66.110.57.21
 * * * Request timed out...
 * * * Request timed out...
 * * * Request timed out...
11
 18 rtt=345 ms 64.86.252.71
11
 19 rtt=303 ms 223.28.26.154
11
 20 rtt=304 ms 223.28.35.225
 * * * Request timed out...
 * * * Request timed out!
11
 21 rtt=304 ms 210.19.226.122

It struggled in the last one 

