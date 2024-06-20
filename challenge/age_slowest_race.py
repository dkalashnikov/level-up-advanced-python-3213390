# Source of data: https://www.arrs.run/
# This dataset has race times for women 10k runners from the Association of Road Racing Statisticians
# Assume a year has 365.25 days
import datetime,re
from math import floor, ceil

def get_data():
    with open('10k_racetimes.txt', 'rt') as file:
        content = file.read()
    return content

def get_rhines_times():
    """Return a list of Jennifer Rhines' race times"""
    races = get_data()
    rhines_rows = [re.split(r"\s\s+", race) for race in races.splitlines()]
    return [row for row in rhines_rows if row[2].find('Jennifer Rhines') == 0]

def get_event_time(line):
    """Given a line with Jennifer Rhines' race times from 10k_racetimes.txt, 
       parse it and return a tuple of (age at event, race time).
       Assume a year has 365.25 days"""
    birth_date = parse_date(line[3]) 
    race_date = parse_date(line[2])
    age = race_date - birth_date
    years = floor(age.days/365.25)
    days = age.days - floor(years*365.25)
    return ("%dy%dd" % (years, days), line[0])

def parse_time(str):
    match = re.match(r"(\d+):(\d+)(\.\d+)?", str)
    if match:
        min = int(match.group(1))
        sec = int(match.group(2))
        mil = match.group(3)
        if mil:
            frac = float('0' + mil)
        else:
            frac = 0.0
        return 60*min + sec + frac

def parse_date(str):
    date = datetime.datetime.strptime(str, '%d %b %Y')
    return date.date()

def parse_row(str):
    edges = [14,57,74,87]
    cols = []
    begin = 0
    for end in edges:
        cols.append(str[begin:end-1].strip())        
        begin = end
    cols.append(str[end:].strip())
    return cols

def get_age_slowest_times():
    '''Return a tuple (age, race_time) where:
       age: AyBd is in this format where A and B are integers'''
    races = get_data()
    rows = [parse_row(race) for race in races.splitlines()]
    rhines_rows = [row for row in rows if row[1].find('Jennifer Rhines') == 0]
    max_time = 0
    max_index = 0
    for i in range(0, len(rhines_rows)):
        time = parse_time(rhines_rows[i][0])
        if time > max_time:
            max_time = time
            max_index = i
    return get_event_time(rhines_rows[max_index])

