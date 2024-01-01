import plotly.graph_objects as go
import plotly 
from plotly.subplots import make_subplots
import plotly.express as px
import pandas as pd
import numpy as np
try:
    import matplotlib.pyplot as plt
    import seaborn as sns
except:
    print('Matplotlib and Seaborn not installed.')

# Function to plot multiple histograms using Plotly. Show different colours based on classification.
def plot_int_hist(
    df, groupby, columns=None, classification=None, label=1, 
    agg='sum', title=True, y_order=False,
    barmode='stack', n_columns=1, height=150
    ):
    """
    Use Plotly to plot multiple histograms using the specified columns of a dataframe.
    https://plotly.com/python/histograms/#specify-aggregation-function

    Arguments:
    - df: Dataframe.
    - columns (optional): Columns of dataframe on which to create the histogram. If blank, all numeric data will be plotted.
    - classification (optional): Provide name of column containing binary classification values (e.g. 0 and 1). 
        Data points classified as 1 will be in red.
    - label (optional): Value of classification column. Default is 1.
    - agg ('count', 'sum', 'avg', 'median', 'mode', 'rms', 'stddev', 'min', 'max', 'first', and 'last'; 
        string, optional): Aggregate function to apply. Default is sum. 
    - barmode ('stack', 'group', or 'overlay'; optional): How the different will be shown. Default is 'stack'.
    - n_columns (optional): Number of columns in the figure. Default is 2.
    - height (optional): Height of each subplot in pixels. Default is 150.
    - y_order (optional): List of values to specify the order of the y axis. Default is None.

    """
    if columns == None:
        columns = df.dtypes[df.dtypes != 'object'].index.tolist()
    n_rows = (len(columns)-1) // n_columns + 1
    fig = make_subplots(rows=n_rows, cols=n_columns, subplot_titles=columns)
    for i, feature in enumerate(columns):
        if classification:
            zero = df.sort_values(feature)[df.sort_values(feature)[classification] != label]
            one = df.sort_values(feature)[df.sort_values(feature)[classification] == label]
            fig.add_trace(go.Histogram(y=zero[groupby], x=zero[feature],
                histfunc=agg, 
                marker_color='blue',
                orientation='h',
                opacity=0.5), 
                row=i//n_columns+1, col=i % n_columns + 1
                )
            fig.add_trace(go.Histogram(y=one[groupby], x=one[feature],
                histfunc=agg, 
                marker_color='red',
                orientation='h',
                opacity=0.5),
                row=i//n_columns+1, col=i % n_columns + 1)
        else:
            fig.add_trace(go.Histogram(
                histfunc=agg, x=df[feature], y=df[groupby],
                orientation='h'
                ), 
            row=i//n_columns+1, col=i % n_columns + 1)
    
    if classification:
        title = f'Observations with {classification} of value {label} are indicated in red'
    else:
        title = 'Value counts'
    fig.update_layout(
        showlegend=False,
        height=(n_rows+1)*height if height else None,
        barmode=barmode,
        # bargap=0.1,
        title=title,
        title_x=0.5,
        title_xanchor='center',
        # title_y=0.1,
        title_yanchor='top'
    )
    if title:
        fig.update_xaxes(title=dict(
            standoff=0,
            ),
            title_text=title if type(title) == str else f'{agg}'.upper(),
            row=n_rows
        )
    if y_order:
        aggregate_df = df[columns + [groupby]].groupby(
            groupby
            ).sum().sort_values(by=[columns[0]], ascending=True)
        index_list = aggregate_df.index.tolist()
        print(f'y_order: {index_list}')
        fig.update_yaxes(categoryorder='array', categoryarray=index_list)
    fig.show()
    return fig

# Function to plot multiple bar charts using Plotly. Show different colours based on classification.
def plot_int_bar(df, columns=None, classification=None, label=1, barmode='stack', n_columns=1, height=150, y_order=None):
    """
    Use Plotly to plot multiple histograms using the specified columns of a dataframe.
    Arguments:
    - df: Dataframe.
    - columns (optional): Columns of dataframe on which to create the histogram. If blank, all numeric data will be plotted.
    - classification (optional): Provide name of colum containing binary classification values 0 and 1. 
        Data points classified as 1 will be in red.
    - label (optional): Label of classification column. Default is 1.
    - barmode ('stack', 'group', or 'overlay'; optional): How the different will be shown. Default is 'stack'.
    - n_columns (optional): Number of columns in the figure. Default is 2.
    - height (optional): Height of each subplot in pixels. Default is 150.
    - y_order (optional): List of values to specify the order of the y axis. Default is None.

    """
    if columns == None:
        columns = df.dtypes[df.dtypes != 'object'].index.tolist()
    n_rows = (len(columns)-1) // n_columns + 1
    fig = make_subplots(rows=n_rows, cols=n_columns, subplot_titles=columns)
    for i, feature in enumerate(columns):
        if classification:
            zero = df.sort_values(feature)[df.sort_values(feature)[classification] != label]
            one = df.sort_values(feature)[df.sort_values(feature)[classification] == label]
            fig.add_trace(go.Histogram(y=zero[feature],
                marker_color='blue',
                orientation='h',
                opacity=0.5), 
                row=i//n_columns+1, col=i % n_columns + 1
                )
            fig.add_trace(go.Histogram(y=one[feature],
                marker_color='red',
                orientation='h',
                opacity=0.5),
                row=i//n_columns+1, col=i % n_columns + 1)
        else:
            fig.add_trace(go.Histogram(x=df[feature]), 
            row=i//n_columns+1, col=i % n_columns + 1)
    
    if classification:
        title = f'Observations with {classification} of value {label} are indicated in red'
    else:
        title = 'Value counts'
    fig.update_layout(
        showlegend=False,
        height=(n_rows+1)*height,
        barmode=barmode,
        # bargap=0.1,
        title=title,
        title_x=0.5,
        title_xanchor='center',
        # title_y=0.1,
        title_yanchor='top'
    )
    fig.update_xaxes(title=dict(
        standoff=0,
        ),
        title_text='number of observations',
        row=n_rows
    )
    if y_order:
        fig.update_yaxes(categoryorder='array', categoryarray=y_order)
    fig.show()

# Function to plot multiple histograms
def plot_hist(df, columns=None):
    """
    Plot multiple histograms using the specified columns of a dataframe.
    Arguments:
    df: Dataframe.
    columns (optional): Columns of dataframe on which to create the histogram. If blank, all numeric data will be plotted.
    
    Make sure to `import seaborn as sns`.
    """
    if columns == None:
        columns = df.dtypes[df.dtypes != 'object'].index.tolist()
    nrows = round((len(columns)+.5)/2)
    fig, ax = plt.subplots(nrows=nrows, ncols=2, figsize=(10,nrows*2))
    for i, feature in enumerate(columns):
        sns.histplot(data=df,x=feature,ax=ax[i//2, i % 2])
    plt.tight_layout()

def correlation_plot(df):
    """
    Plot the correlation matrix.
    Returns the dataframe with the correlation values.
    """

    # Create a mask to exclude the redundant cells that make up half of the graph.
    mask = np.triu(np.ones_like(df.corr(), dtype=bool))

    # Create the heatmap with the mask and with annotation
    sns.heatmap(data=abs(df.corr(numeric_only=True)),mask=mask,annot=True)
    return df.corr()

# Function to plot multiple box plots
def plot_box(df, columns=None,category=None, hue=None):
    """
    Plot multiple histograms using the specified columns of a dataframe.
    Arguments:
    - df: Dataframe.
    - columns (optional): Columns of dataframe on which to create the histogram. If blank, 
        all numeric data will be plotted.
    - category (optional): Categorical feature for y-axis of box plot. If None, 
        only one box will be plotted per dependent variable.
    - hue (optional): Categorical feature by which to split the box plots.

    """
    if columns == None:
        columns = df.dtypes[df.dtypes != 'object'].index.tolist()
    nrows = round((len(columns)+.5)/2)
    fig, ax = plt.subplots(nrows=nrows, ncols=2, figsize=(10,nrows*2))
    for i, feature in enumerate(columns):
        if (category != None) & (hue !=None):
            sns.boxplot(data=df,x=feature,y=category,ax=ax[i//2, i % 2], hue=hue)
        elif category:
            sns.boxplot(data=df,x=feature,y=category,ax=ax[i//2, i % 2])
        else:
            sns.boxplot(data=df,x=feature,ax=ax[i//2, i % 2])
    plt.tight_layout()

# Function to make an interactive histogram combined with a box plot (or violin or rug plot).
def hist_box(df, column=None, marginal='box', color=None):
    """
    Make an interactive histogram combined with a box plot (or violin or rug plot).
    Parameters:
    - column: Column name to plot.
    - color (optional): Column for grouping data. If argument is provided, barmode is 'overlay'.
    - marginal ('box', 'violin', or 'rug'): The second type of plot to include.
    """
    fig = px.histogram(df, x=column, color=color,
        marginal=marginal, # or violin, rug
        opacity=0.5,
        hover_data=df.columns,
        barmode='overlay')
    fig.show()

# Function to plot bar charts where data are normalized for each group. Show different colours based on classification.
def plot_proportion(df, columns=None, classication='Loan_Status', label=1, 
    barmode='stack', n_columns=1, height=150):
    """
    Use Plotly to plot bar charts where data are normalized for each group. 
    Show different colours based on classification.
    Arguments:
    - df: Dataframe.
    - columns (optional): Columns of dataframe containing the categorical variables to plot. 
        If blank, all categorical data will be plotted.
    - classication: Provide name of colum containing binary classification values. 
        Data points classified as 1 will be in red.
    - label (optional): Label of classification column. Default is 1.
    - barmode ('stack', 'group', or 'overlay'; optional): How the different will be shown. Default is 'stack'.
    - n_columns (optional): Number of columns in the figure. Default is 2.

    """
    if columns == None:
        columns = df.dtypes[df.dtypes == 'object'].index.tolist()
    n_rows=round((len(columns)+.5)/n_columns) - 1
    fig = make_subplots(
        rows=n_rows+1, 
        cols=n_columns,subplot_titles=columns)
    for i, feature in enumerate(columns):
        try:
            pivot = df.sort_values(feature).fillna(0).replace('',0).pivot_table(
                df.sort_values(feature).columns[-1], index=[classication], columns=[feature],aggfunc='count')
        except:
            pivot = df.sort_values(feature).fillna(0).replace('',0).pivot_table(
                df.sort_values(feature).columns[0], index=[classication], columns=[feature],aggfunc='count')
        try:
            zero_label = list(set(pivot.index)-set(label))[0] 
        except:
            zero_label = list(set(pivot.index)-set([label]))[0] 
        pivot.index = pivot.index.fillna(zero_label)
        zero = pivot.loc[zero_label,:]/pivot.sum()*100
        yes = pivot.loc[label,:]/pivot.sum()*100
        fig.add_trace(go.Bar(y=pivot.columns,  # Change x to y
            x=zero,  # Change y to x
            orientation='h',  # Add orientation
            marker_color='blue',
            opacity=0.5), 
            row=i//n_columns+1, col=i % n_columns + 1
            )
        fig.add_trace(go.Bar(y=pivot.columns,  # Change x to y
            x=yes,  # Change y to x
            orientation='h',  # Add orientation
            marker_color='red',
            opacity=0.5),
            row=i//n_columns+1, col=i % n_columns + 1)
    
    title = f'Percentage with {classication} of value {label} by category (indicated in red).'
    fig.update_layout(
        barmode=barmode,
        height=(n_rows+1)*height,
        showlegend=False,
        title = title,
        title_x=0.5,
        title_xanchor='center',
        # title_y = .96,
        title_yanchor = 'bottom',
        # xaxis_title='% of Total',  # Add x-axis title
        yaxis_title='',  # Remove y-axis title
        )
    fig.update_xaxes(title=dict(
        standoff=0,
        ),
        title_text='% of Total',
        row=n_rows
    )
    fig.show()

def lineplots_comparison(df, x='Year', columns=['Value', 'Value'], scale_axis=[True,False], match_yaxis=False,
    title=None,
    filter_by='Age', filter_value=12, hue='Percentile', show_legend=True, yaxis_label=None, xticks=None):
    """
    Plot data for the same rows side by side.
    Parameters:
    - df: Dataframe.
    - x (string): Name of variable for x-axis.
    - columns (list): List of column names to plot side by side. 
    - scale_axis (list): Boolean or list of boolean values. If true, scale axes to the min and max for the entire dataframe.
        If more than one value, must match length of columns list.
    - filter_by and filter_value: e.g. df[df[filter_by] == filter_value]
    * hue: Same as for seaborn parameter, i.e. categorical variable for creating different lines.
    * yaxis_label: Label of y-axis. If none, will default to the name of the data column.
    * xticks: Ticks of the x-axis. If none, will be set to default.
    * title: Subplot title. If none, will be blank.
    """
    subplot_label = 'abcdefghijklmnopq'
    if (type(scale_axis) != list):
        scale_axis = [scale_axis for column in columns]
    if type(title) != list:
        title = [title for column in columns]
    if type(yaxis_label) != list:
        yaxis_label = [yaxis_label for column in columns]
    if type(match_yaxis) != list:
        match_yaxis = [match_yaxis for column in columns]
    ncols = len(columns)
    fig, ax = plt.subplots(nrows=1 ,ncols=ncols, figsize=(10,3))
    # colors = sns.color_palette("vlag", n_colors=len(df[hue].unique()))
    colors = sns.color_palette("coolwarm", n_colors=len(df[hue].unique()))
    # colors = sns.mpl_palette('PRGn', n_colors=len(df[hue].unique()))
    
    ax = ax.flatten()
    ax_index = 0

    for index, column in enumerate(columns):
        if (show_legend==True) & (index==0):
            legend = 'full'
        else:
            legend = False

        sns.lineplot(data=df[df[filter_by] == filter_value], y=column, 
            hue=hue, x=x, marker='o', alpha=0.9, palette=colors,
            legend=legend, 
                ax = ax[ax_index])
        
        # ax[ax_index].set_title(f'{filter_by} {filter_value}')
        if title[index]:
            ax[ax_index].set_title(f'{subplot_label[ax_index]}) {title[index]}', loc='left')

        if (scale_axis[index]==True) & (match_yaxis==True):
            ymin = df[columns].min().min()
            ymax = df[columns].max().max()
            ax[ax_index].set_ylim([ymin,ymax]) 
        elif scale_axis[index]:
            ymin = df[column].min()
            ymax = df[column].max()
            ax[ax_index].set_ylim([ymin,ymax]) 
        elif match_yaxis[index]: 
            ymin = df[df[filter_by] == filter_value][columns].min().min()
            ymax = df[df[filter_by] == filter_value][columns].max().max()
            ax[ax_index].set_ylim([ymin,ymax]) 

        if yaxis_label:
            ax[ax_index].set_ylabel(yaxis_label[ax_index])
        if xticks:
            ax[ax_index].xaxis.set_ticks(xticks)
        if (legend == 'full'):
            # Reverse order of legend entries, then position the legend
            handles, labels = ax[ax_index].get_legend_handles_labels()
            ax[ax_index].legend(handles[::-1], labels[::-1])
            sns.move_legend(ax[ax_index],'center left',bbox_to_anchor=(1, 0.5), title=hue)
        ax_index += 1
        
    plt.tight_layout()
    return fig

def lineplots(df, y='Value', x='Year', column='Sex', row='Age', hue='Percentile',
    show_legend=True, yaxis_label=None, xticks=None, title=None):

    """
    Make a figure containing subplots with lineplots. Subplots titles are labelled from a-z.

    Parameters:
    * df: Dataframe.
    * y: Column name with y-axis data.
    * x: Column name with x-axis data.
    * column: Column name of categorical data for creating the different columns in the subplot. 
        Default is Female/Male.
    * row: Column name of categorical data for creating the different rows in the subplot.
    * hue: Same as for seaborn parameter, i.e. categorical variable for creating different lines.
    * yaxis_label: Label of y-axis. If none, will default to the name of the data column.
    * xticks: Ticks of the x-axis. If none, will be set to default.
    * title: Subplot title. If none, will be blank.
    """

    subplot_label = 'abcdefghijklmnopqrstuvwxyz'
    column_values = sorted(df[column].unique())
    row_values = sorted(df[row].unique())
    nrows = len(row_values)
    ncols = max([len(column_values),2])
    title_variable = df[row].name
    fig, ax = plt.subplots(nrows=nrows ,ncols=ncols, figsize=(10,nrows*3))
    fig.suptitle(title, fontsize=20)
    ymin = df[y].min()
    ymax = df[y].max()
    ax = ax.flatten()
    # colors = sns.color_palette("rocket", as_cmap = True)
    # colors = sns.diverging_palette(250, 30, l=65, center="dark", as_cmap = True)
    colors = sns.color_palette("coolwarm", n_colors=len(df[hue].unique()))
    # colors = sns.color_palette("Spectral", n_colors=len(df[hue].unique()))

    ax_index = 0
    for row_number in range(nrows):
        for col_number in range(len(column_values)):
            # print(ax_index)
            if (show_legend==True) & (col_number==0):
                legend = 'full'
            else:
                legend = False
            filter = (df[row] == row_values[row_number]) & (df[column] == column_values[col_number])

            sns.lineplot(data=df[filter], y=y, 
                hue=hue, x=x, marker='o', alpha=0.9,
                legend=legend, palette=colors,
                    ax = ax[ax_index])
            if nrows > 1:
                ax[ax_index].set_title(f'{subplot_label[ax_index]}) {title_variable} {row_values[row_number]}, {column_values[col_number]}', fontsize=12, loc='left')
            else:
                ax[ax_index].set_title(f'{subplot_label[ax_index]}) {column_values[col_number]}', fontsize=12, loc='left')
            ax[ax_index].set_ylim([ymin,ymax]) # Make the y axes all the same
            if yaxis_label:
                ax[ax_index].set_ylabel(yaxis_label)
            if xticks:
                ax[ax_index].xaxis.set_ticks(xticks)
            if (legend == 'full'):
                # Reverse order of legend entries, then position the legend
                handles, labels = ax[ax_index].get_legend_handles_labels()
                ax[ax_index].legend(handles[::-1], labels[::-1])
                sns.move_legend(ax[ax_index],'center left',bbox_to_anchor=(1, 0.5), title=hue)

            ax_index += 1
        
    plt.tight_layout()
    return fig

def correlation(df):
    """
    Plot the correlation matrix.
    Returns the dataframe with the correlation values.
    """

    # Create a mask to exclude the redundant cells that make up half of the graph.
    mask = np.triu(np.ones_like(df.corr(), dtype=bool))

    # Create the heatmap with the mask and with annotation
    sns.heatmap(data=df.corr(numeric_only=True),mask=mask,annot=True)
    return df.corr()