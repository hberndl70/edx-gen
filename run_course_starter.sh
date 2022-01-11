#!/bin/bash
# run edx generator to create course starter

edx_generator_script="./edx_generator.py"
input="./course_starter/input"
output="./course_starter/output"

python3 $edx_generator_script $input $output
