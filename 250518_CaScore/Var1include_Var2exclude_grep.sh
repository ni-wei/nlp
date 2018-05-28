#!/bin/bash
#ToDo: integrate the --color=always option for a better view.
grep -n $1 ../word_seg/dataFromNing_backup/eighty_reports.txt | grep -v $2

## use the command below to exclude multiple strings. 
## Enter the multiple strings as $2, e.g., '涂抹|涂布|...',
## i.e., separate them with the | sign, and put them between quotation marks.
#grep -n $1 report_in_txt.txt | grep -Ev $2

