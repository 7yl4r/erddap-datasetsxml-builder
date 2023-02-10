#!/usr/bin/env python
# NOTE: use python3 in the shebang line above if targeting py3 and not py2-compatible
""" example main file with cmd line interface """
from argparse import ArgumentParser
import glob
import logging
from logging.handlers import RotatingFileHandler
import os
import sys

PACKAGE_NAME = "erddap_datasetsxml_builder"
COMMAND_NAME = "build_datasetsxml"

def parse_args(argv):
   # =========================================================================
    # === set up arguments
    # =========================================================================
    parser = ArgumentParser(
        description='Read all your dataset xml and output an ERDDAP-compatible `datasets.xml` file.'
    )
    
    # === arguments for the main command
    parser.add_argument("-v", "--verbose", help="increase output verbosity",
                        action="count",
                        default=0
    )
    parser.add_argument("erddap_config_dir", help="path to erddap config directory")
    
    args = parser.parse_args()
    # =========================================================================
    # === set up logging behavior
    # =========================================================================
    if (args.verbose == 0):
        stream_log_level = logging.WARNING
    elif (args.verbose == 1):
        stream_log_level = logging.INFO
    else: #} (args.verbose == 2){
        stream_log_level = logging.DEBUG
    logging.basicConfig(level=stream_log_level)

    # === (optional) create custom logging format(s)
    # https://docs.python.org/3/library/logging.html#logrecord-attributes
    formatter = logging.Formatter(
       '%(asctime)s|%(levelname)s\t|%(filename)s:%(lineno)s\t|%(message)s'
    )

    # === (optional) create handlers
    # https://docs.python.org/3/howto/logging.html#useful-handlers
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(stream_log_level)
    stream_handler.setFormatter(formatter)
    
    log_path = f'{PACKAGE_NAME}_{COMMAND_NAME}.log'
    file_handler = RotatingFileHandler(
       log_path, maxBytes=1e6, backupCount=5
    )
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    # === add the handlers (if any) to the logger
    _handlers = [
        stream_handler,
        file_handler
    ]

    logging.basicConfig(
        handlers=_handlers,
        level=logging.DEBUG  # this must be set to lowest of all levels used in handlers
    )
    # =========================================================================
    return args

def build_datasetsxml(erddap_config_dir, **kwargs):
    PRE_FPATH = f"{erddap_config_dir}/_pre.xml"
    POST_FPATH = f"{erddap_config_dir}/_post.xml"
    DATASETS_XML_PATH = f"{erddap_config_dir}/datasets.xml"
    file_list = [PRE_FPATH]
    print("dataset.xml files found:")
    # open each dataset.xml
    for fpath in glob.iglob(os.path.join(
        erddap_config_dir, "datasets", "*", "dataset.xml"
    )):
        print(f"\t{fpath}")
        file_list.append(fpath)

    if len(file_list) < 2:
        raise ValueError(f"no dataset.xml files found in {erddap_config_dir}/datasets/")

    file_list.append(POST_FPATH)
    print(f"writing {len(file_list)} datasets to {DATASETS_XML_PATH}")
    # put all the stuff into datsets.xml
    with open(DATASETS_XML_PATH, "w") as outfile:
        for fpath in file_list:
            with open(fpath, "r") as f:
                text = f.read()
                outfile.write(text)
                outfile.write("\n")
    print("done.")
if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    build_datasetsxml(**vars(args))
else:
    raise AssertionError(
        f"{PACKAGE_NAME}.{COMMAND_NAME} CLI should called as __main__ and should not be imported."
    )
