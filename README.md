# erddap datasetsxml builder

This tool aims to maximize human-editability for ERDDAP's dataset configuration.

## Usage:
* create a separate git repo for your ERDDAP datasets documentation
* within the repo:
  * a datasets folder exists
  * within the datasets folder:
    * each dataset has a folder containing
      * a dataset.xml file
      * (optional) a README.md file & other documentation
* run `build_datasetsxml.py path/to/your/repo_root_folder`
  * a `datasets.xml` file will be produced containing xml for all your datasets
  * you can now copy the `datasets.xml` file to your ERDDAP server

# setup checklist:
## setup as package checklist
1. [X] add name to setup.py
2. [ ] add info to setup.cfg
3. [X] rename `projname` folder
4. [X] update `{projname}/__init__.py`

# installation

```
python -m pip install -e .
````
