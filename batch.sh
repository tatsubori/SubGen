#!/bin/bash

for i in *.txt ; do \
    python SubGen/subviewer.py $i > $i.sub
done
