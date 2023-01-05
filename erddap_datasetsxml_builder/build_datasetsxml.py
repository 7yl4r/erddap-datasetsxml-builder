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
    # open each dataset.xml
    for filename in glob.iglob(os.path.join(erddap_config_dir, "datasets", "*", "dataset.xml")):
        print(filename)
        # TODO: append to datsets.xml
    else:
        raise ValueError(f"no dataset.xml files found in {erddap_config_dir}/datasets/")

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    build_datasetsxml(**vars(args))
else:
    raise AssertionError(
        f"{PACKAGE_NAME}.{SCRIPT_NAME} CLI should called as __main__ and should not be imported."
    )
