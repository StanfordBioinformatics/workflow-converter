#!/usr/bin/env python2

import yaml

class Workflow:
    """Transform workflow definitions into different formats.

    Each workflow format will have base import & export functions
    as well as child functions for different format versions. Child
    functions will implement version specific modifications.

    Note:

    Args:

    Attributes:

    """

    def __init__(self):
        self.inputs
        self.outputs

    def import(self, workflow_path, rules):

    def export(self, workflow_path, rules):

    def import_cw(self, workflow_path):

    def import_loom(self, workflow_path):

    def export_loom(self, workflow_path):

    def export_cw(self, workflow_path):

class Output:

class Input:

class Metadata:



class WorkflowConverter:

    def __init__(self):
        variable = None

    def import_cw_3_3(self, workflow_path):

    def import_loom(self):



    def cwl2loom(self, cwl_path, name):
        """In order to go from cwl to loom... I think it makes sense
        to first convert from cwl to yaml, then edit everything as
        a yaml file. Loom workflows are already written in yaml

            Get a simple CWL workflow
            convert to yaml
            figure out how to convert it to Loom
                from changes, try to generate generalizable rules
        """

        stream = file(cwl_path, 'r')
        workflow = yaml.load(stream)

        print(workflow)




    def loom2cwl(self, workflow, file_format):

    # function
