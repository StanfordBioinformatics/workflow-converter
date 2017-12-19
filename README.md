# workflow_converter

Transform workflow definitions into different file formats.

Initial goal is to support CWL and Loom workflow definition formats

## Design notes

### Philosophy

Each language has its own vocabulary; challenge is how to convert 
between languages. 
* If I use a standard dictionary as the means of converting between 
formats then I am restricting the expanse of my workflow definitions.
* Instead of writing a program to define conversion rules; define a 
protocol for defining conversion rules
* Initially all workflows will be handled as yaml objects, but should 
probably design program so that support for other markdown languages 
can be added in future

### How does it work?
* WorkflowConverter class will have two essential functions: import 
and export
* Workflows will be imported as yaml objects
* Import function will require workflow file and optional conversion rules
* Conversion rules will tell the program how to manipulate the 
workflow definition provided in the workflow, e.g:
** Changes the names of attributes
** Adding static attributes
** Removing attributes
** Telling the program where to look for other workflow definition files 
(CWL template + job file)
* Export function will require an output file path and optional conversion rules
** If no conversion rules are specified, workflow will be written in yaml
format exactly how it was imported
** If conversion rules are specified, those will be applied to the imported 
workflow before export
* If the export rules require attributes not defined in stored workflow, 
program should throw error
* Should also have a function that compares conv
