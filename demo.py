import sys

import cairocffi as cairo
import random
import fractions

import math
import copy

import pycha.line
import pycha.scatter

lines = [ (2*math.pi*i)/4000.0 for i in range(10000) if (i % 10) == 0]
lines2 = [ (i,math.cos(i)) for i in lines ]
lines = [ (i,math.sin(i)) for i in lines ]

def lineChart(output):
    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, 800, 200)

    dataSet = (
        ('lines', [(i, l[1]) for i, l in enumerate(lines)]),
        )
    dataSet2 = [
        ('lines'+str(j), [(i, l[1]/2.0+random.uniform(0.5/(j+1),-0.5/(j+1))) for i, l in enumerate(lines2)])
        for j in
        range(3)
        ]

    options = {
        'axis': {
            'x': {
                'ticks': [dict(v=i, label=fractions.Fraction(l[0]/(2*math.pi))) for i, l in enumerate(lines) if (i % 100) == 0],
            },
            'y': {
                'tickCount': 4,
            },
            'tickFontSize' : 14,
            'legendFontSize': 14
        },
        'background': {
            'color': '#ffffffff',
            'lineColor': '#444444'
        },
        'colorScheme': {
            'name': 'gradient',
            'args': {
                'initialColor': 'blue',
            },
        },
        'legend': {
            'hide': True,
        },
        'stroke': {'shadow': False, 'color': '#aaaaaaff', 'width':6},
    }
    options2 = copy.deepcopy(options)
    options2['colorScheme']['args']['initialColor'] = '#8f1122ff'
    options2['background']['hide'] = True
    options2['axis']['x']['labelColor'] = '#000000ff' 
    options2['axis']['y']['labelColor'] = '#000000ff' 
    options2['axis']['y']['range'] = (-1, 1)
    options2['colorScheme']['name'] = 'itero'
    options2['colorScheme']['args']['itero'] = 100
    chart = pycha.line.LineChart(surface, options)
    chart2 = pycha.scatter.ScatterplotChart(surface, options2)

    chart.addDataset(dataSet)
    chart2.addDataset(dataSet2)
    chart.render()
    chart2.render()

    surface.write_to_png(output)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        output = sys.argv[1]
    else:
        output = 'linechart.png'
    lineChart(output)
