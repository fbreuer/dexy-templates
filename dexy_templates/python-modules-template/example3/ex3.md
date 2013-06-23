## Including Files in a Subdirectory

This example shows how to work with files in subdirectories.

To read a file contained in the `example3` subdirectory, you have to use 
paths relative to this subdirectory. For example, to read 
`example3/data1.json` from within `example3/code.py` you would run

The `example2` directory contains a file `use-fib.py`. Because we are in a
subdirectory we need to modfiy the python path to include the `sharedcode`
directory.

{{ d['code.py|idio|pycon|pyg']['read'] }}

Same thing if you want to write a file to the subdirectory `example3`.

{{ d['code.py|idio|pycon|pyg']['write'] }}

For these inclusions to work you have to reference these files from 
`dexy.yaml`. Also, to support writing files, you need to pass the parameter 
`{ add-new-files: True }` to the filter you use to run your code.

{{ d['../dexy.yaml|idio']['example3'] }}

Note that if you want to include a file such as `example3/data2.csv` into
this markdown document, you also have to use relative paths:

{{ d['data2.csv|idio'] }}

Again, files have to be referenced in `dexy.yaml`:

{{ d['../dexy.yaml|idio']['docs'] }}
