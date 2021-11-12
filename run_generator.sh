#!/bin/bash
# Script to execute Edx Generator

edx_generator_script="./edx_generator.py"
input="./test_course/input"
output="./test_course/output"

python3 $edx_generator_script $input $output