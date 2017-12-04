#!/usr/bin/env bash
set -o errexit      # exit on error
set -o nounset      # exit undeclared var used
source ~/.bash_aliases

# cat day12.in | sed 's/[^[0-9\.\-]]*/ /g' | sed 's/\[//g' | sed 's/ \+/ /g' | tr '\n' ' ' | awk '{sum=0; for (i=1; i<=NF; i++) { sum+= $i } print sum}'



cat day12.in | sed 's/[^[0-9\.\-]]*/ /g' | sed 's/\[//g'
head day12.in


# | sed 's/ \+/ /g' | tr '\n' ' ' | awk '{sum=0; for (i=1; i<=NF; i++) { sum+= $i } print sum}'

