cwlVersion: cwl:draft-3	# not added to loom
class: CommandLineTool	# not added to loom(?)
baseCommand: echo				# first argument of "command" line
inputs:									# same as loom "inputs" section
  - id: message					# loom "channel"
    type: string			  # loom "type"
    inputBinding:				
      position: 1			  # indicates where argument will be placed on "command" line (?)
outputs: []							# same as loom "outputs"
