from __future__ import division
import webbrowser
import sys
import os
import json
import ast
from tools import Functions

funcs_ = Functions()

"""
line plot/continous series plotting function
"""
class line_plot(object):
    def __init__(self, y, x=None, series_title=None, ylabel=None, xlabel=None, plot_title=None, color=None):
        self.funcs_ = funcs_
        self.new = 2
        self.x = x if x else range(0, len(y))
        self.series_title = series_title if series_title else 'series'
        self.ylabel = ylabel if ylabel else 'y-axis'
        self.xlabel = xlabel if xlabel else 'x-axis'
        self.plot_title = plot_title if plot_title else 'Line Plot'
        self.color = color if color else 'cornflowerblue'
        
        self.url_ = 'file://'+os.path.dirname(os.path.abspath('__file__'))+'/plot_pages/line_plot.html'
        self.generate_plot()
    
    def generate_plot(self):
        if len(x) == len(y):
            object_ = {'x_axis': self.x,
                           'y_axis': self.y,
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
Multi line plotting function
"""
class multi_line_plot(object):
    def __init__(self, ys, x=None, ylabel=None, xlabel=None, plot_title=None, colors=None):
        self.funcs_ = funcs_
        self.new = 2
        g = lambda n: len(n[1])
        self.x = x if x else range(0, max(map(g, ys)))
        self.ylabel = ylabel if ylabel else 'y-axis'
        self.xlabel = xlabel if xlabel else 'x-axis'
        self.plot_title = plot_title if plot_title else 'Multi Line Plot'
        self.colors = colors if colors else 'default'

        self.url_ = 'file://'+os.path.dirname(os.path.abspath('__file__'))+'/plot_pages/multi_line_plot.html'
        self.generate_plot(ys)
    
    def prepare(self, y):
        prepared = []
        for a,b in zip(self.x, y):
            prepared.append({'x': a, 'y': b})
        return prepared
        
    def generate_plot(self, ys):
        data = []
        for i in range(0, len(ys)):
            if type(ys[i][0]) != type(''):
                ys[i] = {'key': i, 'values': self.prepare(ys[i][1]), 'length': len(ys[i][1])}
            else:
                ys[i] = {'key': ys[i][0], 'values': self.prepare(ys[i][1]), 'length': len(ys[i][1])}
        
        object_ = {'data': ys,
                       'colors': self.colors,
                       'plot_title': self.plot_title,
                       'ylabel': self.ylabel,
                       'xlabel': self.xlabel}
        f = open('plot_pages/sources/multi_line_chart/multi_line_chart_data.js', 'wb')
        f.write('var multi_line_items_ = '+json.dumps(object_)+';')
        f.close()
        webbrowser.open(self.url_, self.new)

"""
histogram plotting function
"""
class histogram(object):
    def __init__(self, x, plot_title=None):
        self.funcs_ = funcs_
        self.new = 2
        self.plot_title = plot_title if plot_title else 'Histogram'
        self.url_ = 'file://'+os.path.dirname(os.path.abspath('__file__'))+'/plot_pages/histogram_plot.html'
        self.generate_plot(x)

    def generate_plot(self, x):
        if len(x):
            histo = self.funcs_.histogram(x)

            if len(histo) >= 200:
                show_values = False
                show_xaxis = False
            else:
                show_values = True
                show_xaxis = True
                
            hist_data = []
            for k,v in histo.iteritems():
                hist_data.append({'key': k, 'value': v})
            
            object_ = {'plot_data': [{'key': self.title, 'values': hist_data}],
                           'count': len(x),
                           'plot_title': self.plot_title,
                           'show_values': show_values,
                           'show_xaxis': show_xaxis}
            
            f = open('plot_pages/sources/histogram_chart/histogram_chart_data.js', 'wb')
            f.write('var histogram_items_ = '+json.dumps(object_)+';')
            f.close()
            webbrowser.open(self.url_, self.new)


"""
scatter plot function
"""
class scatter_plot(object):
    def __init__(self, data, xlabel=None, ylabel=None, plot_title=None):
        self.funcs_ = funcs_
        self.new = 2
        self.xlabel = xlabel if xlabel else 'x-axis'
        self.ylabel = ylabel if ylabel else 'y-axis'
        self.plot_title = plot_title if plot_title else 'Scatterplot'
        self.url_ = 'file://'+os.path.dirname(os.path.abspath('__file__'))+'/plot_pages/scatter_plot.html'
        self.generate_plot(data)

    def generate_plot(self, data):
        for i in range(0, len(data)):
            if type(data[i][0]) != type(''):
                data[i] = {'name': i, 'data': data[i][1]}
            else:
                data[i] = {'name': data[i][0].encode('utf-8'), 'data': data[i][1]}
        
        object_ = {
                       'data': data,
                       'plot_title': self.plot_title,
                       'xlabel': self.xlabel,
                       'ylabel': self.ylabel,
                       }

        f = open('plot_pages/sources/scatter_chart/scatter_chart_data.js', 'wb')
        f.write('var scatter_items_ = '+json.dumps(object_)+';')
        f.close()
        webbrowser.open(self.url_, self.new)
        
