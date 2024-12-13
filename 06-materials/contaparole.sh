#!/bin/bash

file=$1

cat $file | tr " " "\n" | sort | uniq -c
