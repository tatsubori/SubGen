import datetime

from subviewer import parseTimestamp, duration

def test_parseTimestamp():
    ts = parseTimestamp('1:02')
    assert (ts.minute, ts.second) == (1, 2)


def test_duration():
    ts = parseTimestamp('2:59')
    start_ts, end_ts = duration(ts, 10)
    assert start_ts.isoformat()[-8:] == '00:02:58'
    assert end_ts.isoformat()[-8:] == '00:03:10'


def test_duration_minus():
    ts = parseTimestamp('0:00')
    start_ts, end_ts = duration(ts, 10)
    assert start_ts.isoformat()[-8:] == '00:00:00'
    assert end_ts.isoformat()[-8:] == '00:00:11'
    
