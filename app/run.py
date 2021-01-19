# import libraries
import json
import pandas as pd
import plotly
import plotly.graph_objs as go
from flask import Flask
from flask import render_template

app = Flask(__name__)

# index webpage displays cool visuals and receives user input text for model
@app.route("/")
@app.route("/index")
def index():
    """Generate Plots in the HTML index page.

        Args:
            None

        Returns:
            render_template(render_template): Render template for the plots

    """
    # create table for original dataset
    table_1 = data_table_low(filepath = "sparkify_data.csv", title='Raw Sparkify Data')

    table_2 = data_table_low(filepath = "cleaned_data.csv", title='Cleaned Sparkify Data')

    # create and append plotly visuals into an array to be passed later for graphJSON file
    graphs = [table_1, table_2]

    # encode plotly graphs in JSON
    ids = ["graph-{}".format(i) for i, _ in enumerate(graphs)]
    graphJSON = json.dumps(graphs, cls=plotly.utils.PlotlyJSONEncoder)

    # render web page with plotly graphs
    return render_template("master.html", ids=ids, graphJSON=graphJSON)

@app.route("/Engineered Features")
def engineeredfeatures():

    # create table for original dataset
    table_1 = data_table(filepath = "feat_eng_data.csv", title='Engineered Features Data')

    # create and append plotly visuals into an array to be passed later for graphJSON file
    graphs = [table_1]

    # encode plotly graphs in JSON
    ids = ["graph-{}".format(i) for i, _ in enumerate(graphs)]
    graphJSON = json.dumps(graphs, cls=plotly.utils.PlotlyJSONEncoder)

    # render web page with plotly graphs
    return render_template("engineeredfeatures.html", ids=ids, graphJSON=graphJSON)

@app.route("/Analysis")
def analysis():

    # create and append plotly visuals into an array to be passed later for graphJSON file
    graphs = [plot_1(),plot_2()]

    # encode plotly graphs in JSON
    ids = ["graph-{}".format(i) for i, _ in enumerate(graphs)]
    graphJSON = json.dumps(graphs, cls=plotly.utils.PlotlyJSONEncoder)

    # render web page with plotly graphs
    return render_template("analysis.html", ids=ids, graphJSON=graphJSON)

@app.route("/Results")
def results():

    table_1 = data_table(filepath = "results_data.csv", title='Machine Learning Model Evaluation Results')

    # create and append plotly visuals into an array to be passed later for graphJSON file
    graphs = [table_1]

    # encode plotly graphs in JSON
    ids = ["graph-{}".format(i) for i, _ in enumerate(graphs)]
    graphJSON = json.dumps(graphs, cls=plotly.utils.PlotlyJSONEncoder)

    # render web page with plotly graphs
    return render_template("results.html", ids=ids, graphJSON=graphJSON)

def data_table(
               filepath="sparkify_data.csv",
               title="Engineered Features Dataframe",
               ):
    """Displaying table in Plotly.

        Args:
            filepath (string): path to read the data
            title (string): table title

        Returns:
            Table (fig): a table view using plotly
    """
    df = read_data_csv(filepath)
    fig = go.Figure(
        data=[
            go.Table(
                header=dict(
                    values=list(df.columns), align="left"
                ),
                cells=dict(
                    values=[df[col] for col in df.columns],
                    align="left",
                ),
            )
        ]
    )

    fig.update_layout(title=go.layout.Title(text=title, x=0.5))

    return fig

def data_table_low(
               filepath="sparkify_data.csv",
               title="Engineered Features Dataframe",
               ):
    """Displaying table in Plotly for adjusted csv files.

        Args:
            filepath (string): path to read the data
            title (string): table title

        Returns:
            Table (fig): a table view using plotly
    """
    df = read_data_csv_low(filepath)
    fig = go.Figure(
        data=[
            go.Table(
                header=dict(
                    values=list(df.columns), align="left"
                ),
                cells=dict(
                    values=[df[col] for col in df.columns],
                    align="left",
                ),
            )
        ]
    )

    fig.update_layout(title=go.layout.Title(text=title, x=0.5))

    return fig

def plot_1():
    """Create a plot for users subscription page visit averages.

        Args:

        Returns:
            Figure (fig): a plotly figure

    """
    plot_1 = read_data_csv('plot_1_data.csv')
    x_axis="Variable"
    y_axis="Average Value"
    title="Page Interactions for Paid and Free Subscriptions"

    fig = go.Figure(
        [
            go.Bar(
                x=plot_1[plot_1['Paid'] ==1].variable,
                y=plot_1[plot_1['Paid'] ==1].value,
                text=plot_1[plot_1['Paid'] ==1].variable,
            ),
            go.Bar(
                x=plot_1[plot_1['Paid'] ==1].variable,
                y=plot_1[plot_1['Paid'] ==0].value,
                text=plot_1[plot_1['Paid'] ==1].variable,
            )

        ]
    )
    fig.update_layout(
        barmode='group',
        title=go.layout.Title(text=title, x=0.5),
        xaxis=go.layout.XAxis(title=go.layout.xaxis.Title(text=x_axis)),
        yaxis=go.layout.YAxis(title=go.layout.yaxis.Title(text=y_axis)),
    )

    return fig

def plot_2():
    """Create a plot for users subscription page visit averages.

        Args:

        Returns:
            Figure (fig): a plotly figure

    """
    plot_2 = read_data_csv('plot_2_data.csv')
    x_axis="Variable"
    y_axis="Average Value"
    title="Page Interactions for Cancelled and Active Users"

    fig = go.Figure(
        [
            go.Bar(
                x=plot_2[plot_2['Churn'] ==1].variable,
                y=plot_2[plot_2['Churn'] ==1].value,
                text=plot_2[plot_2['Churn'] ==1].variable,
            ),
            go.Bar(
                x=plot_2[plot_2['Churn'] ==1].variable,
                y=plot_2[plot_2['Churn'] ==0].value,
                text=plot_2[plot_2['Churn'] ==1].variable,
            )

        ]
    )
    fig.update_layout(
        barmode='group',
        title=go.layout.Title(text=title, x=0.5),
        xaxis=go.layout.XAxis(title=go.layout.xaxis.Title(text=x_axis)),
        yaxis=go.layout.YAxis(title=go.layout.yaxis.Title(text=y_axis)),
    )

    return fig

def read_data_csv(path):
    """Read the csv data from the specified path.

        Args:
            path (string): path to the csv file
        Returns:
            DataFrame (df): DataFrame Object

    """
    df = pd.read_csv(path)
    df.drop(["Unnamed: 0"], axis=1, inplace=True)
    return df

def read_data_csv_low(path):
    """Read the csv data from the specified path.

        Args:
            path (string): path to the csv file
        Returns:
            DataFrame (df): DataFrame Object

    """
    df = pd.read_csv(path, low_memory=False)
    df.drop(["Unnamed: 0"], axis=1, inplace=True)
    return df

def main():
    app.run(host="127.0.0.1", port=3001, debug=True)


if __name__ == "__main__":
    main()
