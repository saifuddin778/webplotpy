import sys
import os
sys.dont_write_bytecode = True
import json
import webbrowser
global_new = 2

"""
Primary plotting method
"""
class plot(object):
    def __init__(self, object_, url_, repo, source_name, var_name):
        self.object_ = object_
        self.url_ = url_
        self.repo = repo
        self.source_name = source_name
        self.var_name = var_name
        
    def gen_plot(self):
        uri = os.path.dirname(os.path.abspath('__file__'))+'/plot_pages/sources/'+self.repo+'/'+self.source_name+'.js'
        self.var_name = 'var '+self.var_name
        f = open(uri, 'wb')
        f.write(self.var_name + ' = ' + json.dumps(self.object_) +';')
        f.close()
        webbrowser.open(self.url_, global_new)
