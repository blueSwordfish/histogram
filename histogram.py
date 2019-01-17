
import pandas as pd
import numpy as np
from bokeh.plotting import figure, output_file, show
from bokeh.layouts import widgetbox
from bokeh.models.widgets import Select
from bokeh.layouts import row

from bokeh.io import curdoc

binCount = 20
intputFile = "../data/test.xlsx"
#output_file('output_file_test.html',title='Total Revenue Figure')
revenueColumn = 'total_revenue'

df = pd.read_excel(intputFile,sheet_name="Sheet1")
dfRevenue = df[revenueColumn]

def make_plot(title, hist, edges, x, y):
    fig = figure(title=title, tools='', background_fill_color='white')
    fig.y_range.start = 0
    fig.xaxis.axis_label = x
    fig.yaxis.axis_label = y
    fig.quad(top=hist, bottom=0, left=edges[:-1], right=edges[1:],
         fill_color="#036564", line_color="#033649")
    return fig


hist,edges = np.histogram(dfRevenue.values, bins=binCount)
plot = make_plot("Total Revenue in $", hist, edges, "Revenue", "Organizations")


def callback(attr, old, new):
    binCount=int(select.value)
    hist,edges = np.histogram(dfRevenue.values, bins=binCount)
    plot = make_plot("Total Revenue in $", hist, edges, "Revenue", "Organizations")
    layout=row(plot, widgetbox(select))
    curdoc().add_root(layout)

select = Select(title="Bin Count:", value="20", options=["20", "40","60", "80", "100", "120"])
select.on_change('value', callback)

layout=row(plot, widgetbox(select))
curdoc().add_root(layout)
