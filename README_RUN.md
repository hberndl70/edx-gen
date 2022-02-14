# Running the edX Generator

Important note:

**WARNING: any existing contents in the output folder (i.e. in this case `./out/MOOC1`) will be deleted.**

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

There are two Python scripts:
* `edx_generator.py`: Generates all the MOOC files, including the `.tar.gz` file that can be uploaded to directly to Edx.
* `mob_uploader.py`: Uploads `.mob` files to your AWS s3 bucket.

Execute the generator:
```
python ./edx_generator.py "C:/xxxx/mooc1-procedural-modelling" "C:/Data/xxxx/mooc1"
```

The `__SETTINGS__.py` file in the MOOC root input folder specifies a set of global settings that you can set for your context. 

**WARNING: any existing contents in the output folder (i.e. in this case `./out/MOOC1`) will be deleted.**

## Upload the .tar.gz File

After running the edx generator (assuming no errors), a `tar.gz` file will be generated. This file can be uploaded to your MOOC.

**WARNING: When you upload the .tar.gz file to Edx, any existing course contents in edx will be deleted.**
