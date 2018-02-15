#!/usr/bin/python3
import array
from dateutil import parser

STATUS_OF_INTEREST = '2'


def load_data(filename):
    with open(filename, 'r') as f:
        for line in f.readlines():
            timestr, status = line.strip().split("  ")
            if status == STATUS_OF_INTEREST:
                date = parser.parse(timestr)
                yield date


def trim_time(data):
    start = min(data)
    for element in data:
        yield int((element - start).seconds)


def split_modes(data, m, modes, step_size):
    output = array.array('H', [0] * modes)
    ring = (modes * step_size)
    whole_cap = m - m % ring
    for event_ts in data:
        if event_ts > whole_cap:
            pass
        gross = event_ts % ring
        mod = int(gross / step_size)
        output[mod] += 1
    return output


def suspicious(mode_data, max_res):
    maximum, second_maximum = sorted(mode_data, reverse=True)[0:2]
    if second_maximum == 0:
        return 9999999999999999999
    rate = float(maximum)/float(second_maximum)
    if rate > max_res:
        return rate
    return 0


raw_data = list(load_data('data.txt'))
data = array.array('i', (trim_time(raw_data)))

m = max(data)
print(len(data), m)


max_res = 0.0
for modes in range(500, 2, -1):
    for step in range(1, 13000):
        if modes * step > m:
            continue
        output = split_modes(data, m, modes, step)
        res = suspicious(output, max_res)
        if res >= max_res:
            max_res = res
            print(
                "Significance: %0.3f, modes x step: %s x %s =%s, output: %s (max mode %s)" % (
                 max_res, modes, step, modes*step, list(output), max(output)
            ))
