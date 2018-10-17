import sys
import re
from datetime import timedelta
from datetime import datetime


# dump subviewr format
def printSub(header, body):
    if header and body:
        text = ' '.join(body)
        ts = datetime.strptime(header, "%M:%S")
        start_ts = (ts + timedelta(seconds=-1)).strftime("%H:%M:%S")
        end_ts = (ts + timedelta(seconds=int(len(text) / 10) + 1)).strftime("%H:%M:%S")
        print('{},{}'.format(start_ts, end_ts))
        print(text)
        print()


matcher = re.compile('(\\d+:\\d+)\\s+(.*)$')


current_header = None
current_body = []

with open(sys.argv[1], 'r') as tomy:
    
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
