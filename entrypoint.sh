#!/bin/bash
#set -e

ls -lah .

tree

python erddap_datasetsxml_builder/build_datasetsxml.py ${INPUT_DATASETS_DIR}

# echo "::set-output name=successful_dataset_count::$TODO_GET_THAT_OUTPUT_HERE_SOMEHOW"
