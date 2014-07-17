from __future__ import division
import webbrowser
import sys
import os
import json
import ast
from tools import Functions

funcs_ = Functions()

"""
line plot/xontinous series plotting function
"""
class line_plot(object):
    def __init__(self, y, x=None, series_title=None, ylabel=None, xlabel=None, plot_title=None, color=None):
        self.funcs_ = funcs_
        self.new = 2
        
        self.series_title = series_title if series_title else 'series'
        self.ylabel = ylabel if ylabel else 'y-axis'
        self.xlabel = xlabel if xlabel else 'x-axis'
        self.plot_title = plot_title if plot_title else 'Line Plot'
        self.color = color if color else 'cornflowerblue'
        
        self.url_ = 'file://'+os.path.dirname(os.path.abspath('__file__'))+'/plot_pages/line_plot.html'
        self.generate_plot(y, x)
    
    def generate_plot(self, y, x):
        if len(x) == len(y):
            object_ = {'x_axis': x,
                           'y_axis': y,
                           'count': len(y),
                           'mean': self.funcs_.mean(y),
                           'ylabel': self.ylabel,
                           'xlabel': self.xlabel,
                           'line_label': self.series_title,
                           'plot_title': self.plot_title,
                           'line_color': self.color}
            f = open('plot_pages/sources/line_chart/line_chart_data.js', 'wb')
            f.write('var line_items_ = '+json.dumps(object_)+';')
            f.close()
            webbrowser.open(self.url_, self.new)

"""
histogram function
"""
class histogram(object):
    def __init__(self, x, title=None, color=None):
        self.funcs_ = funcs_
        self.new = 2
        self.url_ = 'file://'+os.path.dirname(os.path.abspath('__file__'))+'/plot_pages/histogram.html'
        self.generate_plot(x)

    def generate_plot(self, x):
        if len(x):
            object_ = self.funcs_.histogram(x)
            f = open('plot_pages/sources/histogram/histogram_data.js', 'wb')
            f.write('var histogram_items_ = '+json.dumps(object_)+';')
            f.close()
            webbrowser.open(self.url_, self.new)

    
    
