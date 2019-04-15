import os
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from flask import Flask, render_template
app = Flask(__name__)

CHART_NAME = "MyChart"
CHART_PATH = os.path.join("static", "images", "%s.png" % CHART_NAME)

'''
For bokeh charts also see
http://biobits.org/bokeh-flask.html
'''

def generate_chart():
    # https://matplotlib.org/gallery/lines_bars_and_markers/simple_plot.html
    t = np.arange(0.0, 2.0, 0.01)
    s = 1 + np.sin(2 * np.pi * t)
    fig, ax = plt.subplots()
    ax.plot(t, s)

    ax.set(xlabel='time (s)', ylabel='voltage (mV)',
           title='About as simple as it gets, folks')
    ax.grid()
    dire_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(dire_path, CHART_PATH)
    fig.savefig(file_path)


def generate_df():
    # create a random pandas data frame
    # https://stackoverflow.com/questions/32752292/how-to-create-a-dataframe-of-random-integers-with-pandas
    return pd.DataFrame(np.random.randn(6, 4), columns=list("ABCD"))


@app.route("/")
def index():
    generate_chart()
    df = generate_df()
    # for the df see
    # https://stackoverflow.com/questions/52644035/how-to-show-a-pandas-dataframe-into-a-existing-flask-html-table
    return render_template("index.html", chart_name = CHART_NAME,
                                         chart_path = CHART_PATH,
                                         tables=[df.to_html(classes="data")], titles=df.columns.values)


if __name__ == '__main__':
    app.run(debug = True)
