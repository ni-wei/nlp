#!/bin/bash
grep --color=always -i -n $1 report_in_txt.txt
# can use "grep –c" to count number of matches.
