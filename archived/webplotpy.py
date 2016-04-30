from __future__ import division
import webbrowser
import sys
sys.dont_write_bytecode = True
import os
import json
import ast
from tools import Functions
from plotter.plot import plot

"""
global vars 
"""
funcs_ = Functions()

"""
line plot/continous series plotting function
"""
class line_plot(object):
    def __init__(self, y, x=None, series_title=None, ylabel=None, xlabel=None, plot_title=None, color=None):
        self.x = x if x else range(0, len(y))
        self.y = y
        self.series_title = series_title if series_title else 'series'
        self.ylabel = ylabel if ylabel else 'y-axis'
        self.xlabel = xlabel if xlabel else 'x-axis'
        self.plot_title = plot_title if plot_title else 'Line Plot'
        self.color = color if color else 'cornflowerblue'
        self.url_ = 'file://'+os.path.dirname(os.path.abspath('__file__'))+'/plot_pages/line_plot.html'
        self.generate_plot()
    
    def generate_plot(self):
        if len(self.x) == len(self.y):
            object_ = {'x_axis': self.x,
                           'y_axis': self.y,
                           'count': len(self.y),
                           'mean': round(funcs_.mean(self.y), 2),
                           'ylabel': self.ylabel,
                           'xlabel': self.xlabel,
                           'line_label': self.series_title,
                           'plot_title': self.plot_title,
                           'line_color': self.color}
            p = plot(object_, self.url_, 'line_chart', 'line_chart_data', 'line_items_')
            p.gen_plot()


"""
Multi line plotting function
"""
class multi_line_plot(object):
    def __init__(self, ys, x=None, ylabel=None, xlabel=None, plot_title=None, colors=None):
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
        p = plot(object_, self.url_, 'multi_line_chart', 'multi_line_chart_data', 'multi_line_items_')
        p.gen_plot()


"""
histogram plotting function
"""
class histogram(object):
    def __init__(self, x, plot_title=None):
        self.plot_title = plot_title if plot_title else 'Histogram'
        self.url_ = 'file://'+os.path.dirname(os.path.abspath('__file__'))+'/plot_pages/histogram_plot.html'
        self.generate_plot(x)

    def generate_plot(self, x):
        if len(x):
            histo = funcs_.histogram(x)
            if len(histo) >= 200:
                show_values = False
                show_xaxis = False
            else:
                show_values = True
                show_xaxis = True
            hist_data = []
            for k,v in histo.iteritems():
                hist_data.append({'key': k, 'value': v})
            object_ = {'plot_data': [{'key': self.plot_title, 'values': hist_data}],
                           'count': len(x),
                           'plot_title': self.plot_title,
                           'show_values': show_values,
                           'show_xaxis': show_xaxis}
            p = plot(object_, self.url_, 'histogram_chart', 'histogram_chart_data', 'histogram_items_')
            p.gen_plot()


"""
scatter plot function
"""
class scatter_plot(object):
    def __init__(self, data, xlabel=None, ylabel=None, plot_title=None):
        self.xlabel = xlabel if xlabel else 'x-axis'
        self.ylabel = ylabel if ylabel else 'y-axis'
        self.plot_title = plot_title if plot_title else 'Scatterplot'
        self.url_ = 'file://'+os.path.dirname(os.path.abspath('__file__'))+'/plot_pages/scatter_plot.html'
        self.generate_plot(data)

    def generate_plot(self, data):
        for i in range(0, len(data)):
            if type(data[i][1]).__name__ == 'ndarray':
                data[i][1] = map(list, data[i][1])
            if type(data[i][0]) != type(''):
                data[i] = {'name': str(i+1), 'data': data[i][1]}
            else:
                data[i] = {'name': data[i][0].encode('utf-8'), 'data': data[i][1]}
        object_ = {
                       'data': data,
                       'plot_title': self.plot_title,
                       'xlabel': self.xlabel,
                       'ylabel': self.ylabel,
                       }
        p = plot(object_, self.url_, 'scatter_chart', 'scatter_chart_data', 'scatter_items_')
        p.gen_plot()


"""
Pie chart function
"""
class pie_chart(object):
    def __init__(self, data, plot_title=None, item_type=None):
        self.plot_title = plot_title if plot_title else 'Pie Chart'
        self.item_type = item_type if item_type else 'Segment'
        self.url_ = 'file://'+os.path.dirname(os.path.abspath('__file__'))+'/plot_pages/pie_plot.html'
        self.generate_plot(data)
    def generate_plot(self, data):
        #verify accuracy of structure
        for i in range(0, len(data)):
            if len(data[i]) == 1:
                data[i] = [i+1, data[i]]
        object_ = {
                        'data': data,
                        'plot_title': self.plot_title,
                        'item_type': self.item_type
                       }
        p = plot(object_, self.url_, 'pie_chart', 'pie_chart_data', 'pie_items_')
        p.gen_plot()


"""
Single Bar plot
"""
class bar_chart(object):
    def __init__(self, data, plot_title=None, xlabel=None, ylabel=None):
        self.plot_title = plot_title if plot_title else 'Bar Chart'
        self.xlabel = xlabel if xlabel else 'x-axis'
        self.ylabel = ylabel if ylabel else 'y-axis'
        self.url_ = 'file://'+os.path.dirname(os.path.abspath('__file__'))+'/plot_pages/bar_plot.html'
        self.generate_plot(data)

    def generate_plot(self, data):
        labels = map(lambda n: n[0], data)
        values = map(lambda n: n[1], data)
        object_ = {
                'data_labels': labels,
                'data_values': values,
                'plot_title': self.plot_title,
                'xlabel': self.xlabel,
                'ylabel': self.ylabel
        }
        
        p = plot(object_, self.url_, 'bar_chart', 'bar_chart_data', 'bar_items_')
        p.gen_plot()

        

