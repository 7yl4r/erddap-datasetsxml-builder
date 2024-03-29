# erddap datasetsxml builder

This tool aims to maximize human-editability for ERDDAP's dataset configuration.

## Usage:
* create a separate git repo for your ERDDAP datasets documentation
* within the repo:
  * a _pre.xml file containing "prefix" xml to put in the datsets.xml before the datasets themselves
  * a _post.xml file containing "postfix" xml to put in datasets.xml after the datasets
  * a datasets folder exists
  * within the datasets folder:
    * each dataset has a folder containing
      * a dataset.xml file
      * (optional) a README.md file & other documentation
* run `build_datasetsxml.py path/to/your/repo_root_folder`
  * a `datasets.xml` file will be produced containing xml for all your datasets
  * you can now copy the `datasets.xml` file to your ERDDAP server

```bash
python erddap_datasetsxml_builder/build_datasetsxml.py ../erddap-config/
```

# installation

```
python -m pip install -e .
````
