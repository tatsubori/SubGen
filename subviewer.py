import sys
import re
import datetime
from datetime import timedelta


def parseTimestamp(text):
    return datetime.datetime.strptime(text, "%M:%S")


def duration(ts, seconds, offset=0, margin=1):
    start_ts = ts + timedelta(seconds=offset - margin)
    end_ts = ts + timedelta(seconds=offset + seconds + margin)
    if start_ts < datetime.datetime.strptime("0:00", "%M:%S"):
        start_ts = datetime.datetime.strptime("0:00", "%M:%S")
    return start_ts, end_ts


# dump subviewr format
def printSub(header, body):
    if header and body:
        text = ' '.join(body)
        ts = parseTimestamp(header)
        seconds = len(text) // 10
        start_ts, end_ts = duration(ts, seconds=seconds)
        
        print('{},{}'.format(start_ts.strftime("%H:%M:%S"),
                             end_ts.strftime("%H:%M:%S")))
        #print('{},{}'.format(start_ts.isoformat(),
        #                     end_ts.isoformat()))
        print(text)
        print()


def main(argv):
    matcher = re.compile('(\\d+:\\d+)\\s+(.*)$')
    
    current_header = None
    current_body = []
    
    with open(argv[1], 'r') as tomy:
        
        while True:
            line = tomy.readline()
            if not line:
                printSub(current_header, current_body)
                break
            result = matcher.match(line)
        if not result:
            current_body.append(line.strip())
        else:
            printSub(current_header, current_body)
            #print(result.group(1))
            current_header = result.group(1)
            #print(result.group(2).strip())
            current_body = [ result.group(2).strip() ]


if __name__ == '__main__':
    main(sys.argv)
