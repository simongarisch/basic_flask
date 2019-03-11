from flask import Flask, render_template
app = Flask(__name__)

###################################################################
import os
from math import pi
import pandas as pd
import json
from bokeh.plotting import figure, show, output_file, save
from bokeh.sampledata.stocks import MSFT

df = pd.DataFrame(MSFT)[:50]
df["date"] = pd.to_datetime(df["date"])

inc = df.close > df.open
dec = df.open > df.close
w = 12*60*60*1000 # half day in ms

TOOLS = "pan,wheel_zoom,box_zoom,reset,save"

p = figure(x_axis_type="datetime", tools=TOOLS, plot_width=1000, title = "MSFT Candlestick")
p.xaxis.major_label_orientation = pi/4
p.grid.grid_line_alpha=0.3

p.segment(df.date, df.high, df.date, df.low, color="black")
p.vbar(df.date[inc], w, df.open[inc], df.close[inc], fill_color="#D5E1DD", line_color="black")
p.vbar(df.date[dec], w, df.open[dec], df.close[dec], fill_color="#F2583E", line_color="black")

file_name = "candlestick.html"
dire_path = os.path.dirname(os.path.realpath(__file__))
file_path = os.path.join(dire_path, "templates", file_name)
output_file(file_name, title="candlestick.py example")
save(p, file_path)
###################################################################
# example here https://github.com/bokeh/bokeh/blob/1.0.4/examples/embed/json_item.py
# https://www.fullstackpython.com/blog/responsive-bar-charts-bokeh-flask-python-3.html
# http://hplgit.github.io/web4sciapps/doc/pub/._web4sa_flask013.html
from bokeh.plotting import figure
from bokeh.resources import CDN
from bokeh.embed import components

script, div = components(p)
#print("script..." + "*" * 20)
#print(script)
#print("div..." + "*" * 20)
#print(div)

###################################################################

@app.route("/")
def index():
    return render_template("index.html", div=div, script=script)

if __name__ == "__main__":
    app.run(debug=True)
