#!/bin/bash
# Script to execute edX Generator

edx_gen="./edx_generator.py"
input="./input"
output="./output"

python3 $edx_gen $input $output
