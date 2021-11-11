#!/bin/bash
# Script to execute Edx Generator

#mob_uploader_script="./mob_uploader.py"
edx_generator_script="./edx_generator.py"
input="./test_academy/input"
output="./test_academy/output"

#python3 $mob_uploader_script $input
python3 $edx_generator_script $input $output``