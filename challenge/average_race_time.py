# Source of data: https://www.arrs.run/
# This dataset has race times for women 10k runners from the Association of Road Racing Statisticians

import re
from datetime import time
from math import floor

def get_data():
    """Return content from the 10k_racetimes.txt file"""
    with open('10k_racetimes.txt', 'rt') as file:
        content = file.read()
    return content

def get_rhines_times():
    """Return a list of Jennifer Rhines' race times"""
    races = get_data()
    rhines_rows = [re.split(r"\s\s+", race) for race in races.splitlines()]
    return [row[1] for row in rhines_rows if row[2].find('Jennifer Rhines') == 0]

def get_average():
    """Return Jennifer Rhines' average race time in the format:
       mm:ss:M where :
       m corresponds to a minutes digit
       s corresponds to a seconds digit
       M corresponds to a milliseconds digit (no rounding, just the single digit)"""
    racetimes = get_rhines_times()
    sum = 0.0
    num = 0
    for racetime in racetimes:
        match = re.match(r"(\d+):(\d+)(\.\d+)?", racetime)
        if match:
            min = int(match.group(1))
            sec = int(match.group(2))
            mil = match.group(3)
            if mil:
                frac = float('0' + mil)
            else:
                frac = 0.0
            sum = sum + 60*min + sec + frac
            num = num + 1
    avg_sec = sum/num
    min = avg_sec//60
    sec = floor(avg_sec) - min*60
    ms = avg_sec - min*60 - sec
    ret = "%d:%d" % (min, sec)
    if ms:
        ret = ret + ("%1.1f" % ms)[1:]
    return ret
    

