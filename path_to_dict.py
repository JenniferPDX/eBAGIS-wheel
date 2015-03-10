import os
import json

folder_extensions_to_skip = ['.gdb', '.git']

py_file_extension = '.py'
html_file_extension = '.html'

directoryColor  = '#667A66'
pyColor         = '#C0CCC0'
htmlColor       = '#fd8d3c'
miscColor       = '#fdbe85'

def path_to_dict(path):
    b_use_folder = True
    name = os.path.basename(path)
    d = {'name': name}
    
    # TODO: I'd like to omit these folders from the JSON entirely, 
    # but I don't know how to get around the need to return the d object
    for extension in folder_extensions_to_skip:
        if name.endswith( extension ):
            b_use_folder = False
    
    if (os.path.isdir(path)): 
        d['colour'] = directoryColor
        if ( b_use_folder ):
            # TODO: If the folder is empty, it should get a size, but I'd rather not 
            # give every single folder a size, since it will be ignored unless the folder is terminal
            d['children'] = [path_to_dict(os.path.join(path,x)) for x in os.listdir (path)]
        else:
            # Since I can't exclude such folders, 
            # they are terminal nodes and need to have a size
            d['size'] = 2

    else:
        # TODO: I'd like to omit some files (*.pyc; *.log) from the JSON entirely, 
        # but I don't know how to get around the need to return the d object
        d['size'] = 2
        if ( d[ 'name' ].endswith( py_file_extension )):
            d[ 'colour' ] = pyColor
        elif ( d[ 'name' ].endswith( html_file_extension )):
            d[ 'colour' ] = htmlColor
        else:
            d[ 'colour' ] = miscColor

    return d

# Output needs to be in an array to be used by the executeWheel() function
print '['
print json.dumps(path_to_dict('.'))
print ']'