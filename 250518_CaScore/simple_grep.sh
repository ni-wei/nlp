#!/bin/bash
grep --color=always -i -n $1 ../word_seg/dataFromNing_backup/eighty_reports.txt
# can use "grep –c" to count number of matches.
