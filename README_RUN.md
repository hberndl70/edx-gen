# Running the edX Generator

Important note:

**WARNING: any existing contents in the output folder (i.e. in this case `./output/chapter`) will be deleted.**

**WARNING: When you upload the .tar.gz file to Edx, any existing course contents in edx will be deleted.**

Make sure to save backups!

## Dependencies

This Python3 script requires three python modules. These can be installed with `pip` as follows:

* `pip install markdown`
* `pip install lxml`
* `pip install boto3`

Markdown is processes using the python markdown module.
- https://python-markdown.github.io

The following extensions are used:
- https://python-markdown.github.io/extensions/extra/
- https://python-markdown.github.io/extensions/fenced_code_blocks/
- https://python-markdown.github.io/extensions/tables/

extensions = ['extra', 'sane_lists']

## Execution

There is the `edx_generator.py` Python script:
It generates all the edX files which comprise the course, including the `.tar.gz` file for the import of the course into edX.

Execute the generator:
```
python ./edx_generator.py ./academy/input/course-starter ./output/course-starter
```

The `__SETTINGS__.py` file in the edX course root input folder specifies a set of global settings that you can set for your context. 

**WARNING: any existing contents in the output folder (i.e. in this case `./output/chapter`) will be deleted.**

## Upload the .tar.gz File

After running the edX generator (assuming no errors), a `tar.gz` file will be generated. This file can be uploaded to the edX platform.

**WARNING: When you upload the .tar.gz file to edX, any existing course contents in this edX course will be deleted.**
