Cyclic detector
===============

Input data: series of events, with status '2' (bad) or '0' (good). Each even has timestamp.

Algorithm:

All 'bad' data's timestamps are placed on cyclic ring consisted of N mods (buckets) with length of M seconds.
Algorithm tries each combination of N and M, with goal to find such values, that one bucket has much move
timestams then next largest. The combination with maximum difference between max and second max value
is a winner.

data.txt contains actual observations, and this algorithm shows, that each 71720 seconds amount of
'bad' events were doubled for duration 6520 seconds. (mods = 11, step=6520).

This algorithm is very slow, it takes about 20-30 minutes to finish.

