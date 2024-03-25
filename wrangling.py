import pandas as pd
import sys
import os
sys.path.append(r"C:\Users\silvh\OneDrive\lighthouse\custom_python")
from silvhua import *
from datetime import datetime, timedelta
import re
import json
from Custom_Logger import *

def decode_json_string(json_str):
    decoded_dict = json.loads(json_str, object_hook=lambda d: {eval(k): v for k, v in d.items()})
    return decoded_dict

def spreadsheet_to_tuple_dict(string, key_length=2):
    """
    Made so you can copy data from 2+ columns of a Google sheet and convert into a dictionary
    Where the right column text is the value of the dictionary and the values in the remaining
    columns are concatenated to create the key.
    Created originally for CYSIS table mapping project.
    """

    result = string.strip()
    result = re.sub(r'\t', r':\t', result)
    result = re.sub(r' ,', r',', result)
    result = re.sub(r'\n', r',', result)
    # result = re.sub(r' ([^:,\s]+:)', r'_\1', result) # Replace spaces in keys with underscore
    key_regex = r'([^:,]+):\t'
    for i in range(1, key_length):
        key_regex += r'([^:,]+):\t'
    key_regex += r'([^:,]+)(?:, )?'
    print(key_regex)
    key_regex_capture_groups = '"' + r'__'.join([rf'\{int}' for int in range(1, key_length+1)]) + '"'
    
    print(f'key regex capture groups: {key_regex_capture_groups}')
    result = re.sub(key_regex, rf'{key_regex_capture_groups}: "\{key_length+1}"', result).rstrip(',\n')
    result = "\n{" + result + "}\n"

    # print(f'result string: \n{result}')
    result = json.loads(result)
    # print(f'Number of dictionary items: {len(result)}')
    return result

def get_value_counts(df, columns, copy_paste=False, logger=None):
    """
    Prints the unique values and their counts for each column in the given dataframe.

    Parameters:
    - df: The dataframe to explore (pandas.DataFrame).
    - columns: A list of column names to explore (list or string).

    Returns:
        Pandas Series object from `pd.value_counts()` 
    """
    logger = create_function_logger('get_value_counts', logger)
    if type(columns) == str:
        columns = [columns]
    print_data = []
    for column in columns:
        print_data.append(f'Value counts for `{column}` column:')

        result = df[column].value_counts()
        if copy_paste:
            result.reset_index().apply(lambda x: print_data.append(f'- {x[column]}: {int(x["count"])}'), axis=1)
        print_data.append(f'\tNull values: {df[column].isnull().sum()}')
        print_data.append(f'\tData type: {df[column].dtype}')
        print_data.append('\n')
    logger.info('\n'.join(print_data))
    return result

def explore_categorical(df, categorical_columns, show_numbers=True):
    """
    Prints the unique values and their counts for each categorical column in the given dataframe.

    Parameters:
    - df: The dataframe to explore (pandas.DataFrame)
    - categorical_columns: A list of column names to explore (list)

    Returns:
    None
    """
    for column in categorical_columns:
        print(f'\n**{column}** ({len(df[column].unique())} unique values):\n')
        values = df.value_counts(column).sort_values(ascending=False).index
        for value in values:
            if show_numbers:
                print(f'\t{value} ({df[df[column]==value].shape[0]})')
            else:
                print(f'{value},')

def delete_documents(filename, filepath):
    """Function to delete files prior to their generation."""
    if filepath:
        filename = f'{filepath}/{filename}'
    try:
        os.remove(filename)
        print(f'{filename} deleted')
    except Exception as error:
        exc_type, exc_obj, tb = sys.exc_info()
        f = tb.tb_frame
        lineno = tb.tb_lineno
        filename = f.f_code.co_filename
        message = f'{filename} not deleted. An error occurred on line {lineno} in {filename}: {error}.'
        print(message)

def filter_by_period(
        df, column='created_time', period=None, start_date=None, end_date=None,
        verbose=False, **kwargs
        ):
    """
    Filter a DataFrame based on a specified column and period or provided start_date and end_date.
    
    Parameters:
        df (DataFrame): The DataFrame to filter.
        column (str): The column to filter on.
        period (str, optional): The period to filter by. Valid options are 'week', 'past_month', 'past_quarter', 'past_week', or None. Defaults to None.
        start_date (str, optional): The start date to filter by. Should be in the format 'YYYY-MM-DD'. Defaults to None.
        end_date (str, optional): The end date to filter by. Should be in the format 'YYYY-MM-DD'. Defaults to None.
    
    Returns:
        DataFrame: A new DataFrame containing only the rows that meet the specified filtering criteria.
    
    Raises:
        ValueError: If an invalid period is provided.
    """
    today = datetime.today().date()
    try:
        # Set the start and end dates based on the specified period or provided start_date and end_date
        if period == 'week':
            start_date = today - timedelta(days=today.weekday())  # Monday of the current week
            end_date = today + timedelta(days=6 - today.weekday())  # Sunday of the current week
        elif period == 'past_month':
            start_date = today.replace(day=1) - timedelta(days=1)  # Last day of the previous month
            start_date = start_date.replace(day=1)  # First day of the previous month
            end_date = today.replace(day=1) - timedelta(days=1)  # Last day of the previous month
        elif period == 'past_quarter':
            end_date = today.replace(day=1) - timedelta(days=1)  # Last day of the previous month
            start_date = end_date.replace(day=1) - timedelta(days=2 * 30)  # First day of 3 months ago
            start_date = start_date.replace(day=1)
        elif period == 'past_week':
            start_date = today - timedelta(days=today.weekday() + 7)  # Monday of the previous week
            end_date = today - timedelta(days=today.weekday() + 1)  # Sunday of the previous week
        elif period is None:
            if end_date is not None:
                end_date = datetime.strptime(end_date, '%Y-%m-%d').date()
            else:
                end_date = today
            if start_date is not None:
                start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
            else:
                start_date = end_date - timedelta(days=28)
        else:
            raise ValueError("Invalid period. Valid options are 'week', 'past_month', 'past_quarter', 'past_week', or None.")
        
        df = df.copy()
        df[column] = pd.to_datetime(df[column], **kwargs).dt.date    
        if verbose:
            print(f'Filtering based on {column} between {start_date} and {end_date}')
        filtered_df = df[(df[column] >= start_date) & (df[column] <= end_date)]
    except Exception as error:
        exc_type, exc_obj, tb = sys.exc_info()
        f = tb.tb_frame
        lineno = tb.tb_lineno
        filename = f.f_code.co_filename
        message = f'`filter_by_period`: An error occurred on line {lineno} in {filename}: {error}. \n'
        print(message)
    
    return filtered_df

def filter_df_any_condition(df, filters, view_columns=None, verbose=False, show_indices=True):
    """
    Filters a DataFrame based on any of the given conditions in a dictionary.

    Args:
        df (pandas.DataFrame): The DataFrame to filter.
        filters (dict): A dictionary with column names as keys and filter conditions as values.
            The filter condition can be a boolean, a string representing a comparison operation,
            a list of values, or the string "null" or "notnull".
        view_columns (list): A list of column names to include in the resulting DataFrame.
            If None, all columns will be included.        
        Example filters dictionary:
        all_filters1 = {
            'Captured': False,
            'Captured': True,
            'Your Name': ['Rob'], 
            'Class': '< 200',
            'Cardio Friendly': ['y'],
            'test friendly': ['y']
        }
        verbose (bool): If true, prints indices of filtered rows.
    Returns:
        pandas.DataFrame: A filtered DataFrame where at least one condition is met.
    """
    filtered_dfs = []
    filtered_df = df.copy()  # make a copy of the original DataFrame
    for col, condition in filters.items():
        if (isinstance(condition, list)) | (isinstance(condition, pd.Series)):
            if type(condition[0]) == str:
                condition = [str(item).lower() for item in condition]
                filtered_dfs.append(filtered_df[filtered_df[col].str.lower().isin(condition)])
            else:
                filtered_dfs.append(filtered_df[filtered_df[col].isin(condition)])
            if verbose:
                print(f'Filtered on {col} in {[item for item in condition]}: {[index for index in filtered_df.index]}')
        elif isinstance(condition, bool):
            filtered_dfs.append(filtered_df[filtered_df[col] == condition])
            if verbose:
                print(f'Filtered on {col} in {condition}: {[index for index in filtered_df.index]}')
        elif condition == "notnull":
            if filtered_df[col].dtypes== 'datetime64[ns]':
                filtered_dfs.append(filtered_df[filtered_df[col] > datetime(1900, 1, 1)])
            else:
                filtered_dfs.append(filtered_df[filtered_df[col].notnull()])
            if verbose:
                print(f'Filtered on {col} in {condition}: {[index for index in filtered_df.index]}')
        elif condition == "null":
            if filtered_df[col].dtypes== 'datetime64[ns]':
                filtered_dfs.append(filtered_df[filtered_df[col] == datetime(1900, 1, 1)])
            else:
                filtered_dfs.append(filtered_df[filtered_df[col].isnull()])
            if verbose:
                print(f'Filtered on {col} in {condition}: {[index for index in filtered_df.index]}')
        else:
            filtered_dfs.append(filtered_df.query(f'{col}{condition}'))
            if verbose:
                print(f'Filtered on {col} in {condition}: {[index for index in filtered_df.index]}')
    combined_df = pd.concat(filtered_dfs).sort_index()
    deduped_df = combined_df.drop_duplicates(ignore_index=False)
    deduped_df = deduped_df[view_columns] if view_columns != None else deduped_df
    if show_indices:
        print(f'Results where any condition is met:')
        print(f'\tDataFrame indices: {[index for index in deduped_df.index]}')
    print(f'\tDataFrame shape: {deduped_df.shape}')
    return deduped_df


def filter_df_all_conditions(df, filters, view_columns=None, verbose=False, show_indices=True):
    """
    Filters a DataFrame based on all of the given conditions in a dictionary.

    Args:
        df (pandas.DataFrame): The DataFrame to filter.
        filters (dict): A dictionary with column names as keys and filter conditions as values.
            The filter condition can be a boolean, a string representing a comparison operation,
            a list of values, or the string "null" or "notnull".
        view_columns (list): A list of column names to include in the resulting DataFrame.
            If None, all columns will be included.
        
        Example filters dictionary:
        all_filters1 = {
            'Captured': False,
            'Captured': True,
            'Your Name': ['Rob'], 
            'Class': '< 200',
            'Cardio Friendly': ['y'],
            'test friendly': ['y']
        }
        verbose (bool): If true, prints indices of filtered rows.

    Returns:
        pandas.DataFrame: A filtered DataFrame where all conditions are met.
    """
    filters_list = []
    filtered_df = df.copy()  
    for col, condition in filters.items():
        if (isinstance(condition, list)) | (isinstance(condition, pd.Series)):
            if type(condition[0]) == str:
                condition = [str(item).lower() for item in condition]
                filters_list.append(filtered_df[filtered_df[col].str.lower().isin(condition)].index.tolist())
            else:
                filters_list.append(filtered_df[filtered_df[col].isin(condition)].index.tolist())
            if verbose:
                print(f'Filtered on {col} in {[item for item in condition]}')
        elif isinstance(condition, bool):
            filters_list.append(filtered_df[filtered_df[col] == condition].index.tolist())
        elif condition == "notnull":
            print(f'Date column dtype: {filtered_df[col].dtype}')
            if filtered_df[col].dtypes== 'datetime64[ns]':
                filters_list.append(filtered_df[filtered_df[col] > datetime(1900, 1, 1)].index.tolist())
                if verbose:
                    print('Removed rows with null dates')
            else:
                filters_list.append(filtered_df[filtered_df[col].notnull()].index.tolist())
        elif condition == "null":
            if filtered_df[col].dtypes== 'datetime64[ns]':
                filters_list.append(filtered_df[filtered_df[col] == datetime(1900, 1, 1)].index.tolist())
            else:
                filters_list.append(filtered_df[filtered_df[col].isnull()].index.tolist())
        else:
            filters_list.append(filtered_df.query(f'{col}{condition}').index.tolist())
    filtered_rows = sorted(list(set(filters_list[0]).intersection(*filters_list[1:])))
    if show_indices:
        print(f'Results where ALL conditions are met:')
        print(f'\tDataFrame indices: {filtered_rows}')
    filtered_df = df.loc[filtered_rows][view_columns] if view_columns != None else df.loc[filtered_rows]
    print(f'\tDataFrame shape: {filtered_df.shape}')
    return filtered_df

def filter_any_and_all(df, any_filters, all_filters, view_columns=None, verbose=False):
    """
    Filters a pandas DataFrame by applying two types of filters: 'any' and 'all'.
    
    Parameters:
    -----------
    df : pandas.DataFrame
        The DataFrame to filter.
    any_filters : list of dict or None
        The 'any' filters to apply to the DataFrame. A filter is a dictionary with the following keys:
            - 'column': the name of the column to filter by.
            - 'condition': the condition to apply to the column. Must be a string that can be evaluated as a boolean expression.
        If None, no 'any' filters are applied.
    all_filters : list of dict or None
        The 'all' filters to apply to the DataFrame. A filter is a dictionary with the same keys as above.
        If None, no 'all' filters are applied.
    view_columns : list of str or None, optional
        The columns to include in the final filtered DataFrame. If None, all columns are included.
    verbose (bool): If true, prints indices of filtered rows.
        
        Example filters dictionary:
        all_filters1 = {
            'Captured': False,
            'Captured': True,
            'Your Name': ['Rob'], 
            'Class': '< 200',
            'Cardio Friendly': ['y'],
            'test friendly': ['y']
        }
        
    Returns:
    --------
    pandas.DataFrame
        The filtered DataFrame.
    """
    print(f'Original DataFrame shape: {df.shape}')
    if any_filters:
        print(f'** Applying filter_df_any_condition')
        any_filtered_df = filter_df_any_condition(df, any_filters, view_columns, verbose=verbose)
        print()
    else:
        any_filtered_df = pd.DataFrame()
    if all_filters:
        print(f'** Applying filter_df_all_conditions')
        all_filtered_df = filter_df_all_conditions(df, all_filters, view_columns, verbose=verbose)
        print()
    else:
        all_filtered_df = pd.DataFrame()
    combined_df = pd.concat(
        [any_filtered_df, all_filtered_df]
        ).sort_index().drop_duplicates(ignore_index=False)
    combined_df = combined_df[view_columns] if view_columns != None else combined_df
    print(f'Final DataFrame shape: {combined_df.shape}')
    return combined_df

def filter_chain(df, any_filters, all_filters, final_filter, view_columns=None, verbose=False):
    """
    Chains together multiple filtering functions to filter a pandas DataFrame.
    
    Parameters:
    -----------
    df : pandas.DataFrame
        The DataFrame to filter.
    any_filters : list of dict or None
        The 'any' filters to apply to the DataFrame. A filter is a dictionary with the following keys:
            - 'column': the name of the column to filter by.
            - 'condition': the condition to apply to the column. Must be a string that can be evaluated as a boolean expression.
        If None, no 'any' filters are applied.
    all_filters : list of dict or None
        The 'all' filters to apply to the DataFrame. A filter is a dictionary with the same keys as above.
        If None, no 'all' filters are applied.
    final_filter : dict or list of dict or None
        The final filter(s) to apply to the DataFrame. A filter is a dictionary with the same keys as above.
        If None, no final filter is applied.
        If a list of filters is provided, they will be applied sequentially.
    view_columns : list of str or None, optional
        The columns to include in the final filtered DataFrame. If None, all columns are included.
    verbose (bool): If true, prints indices of filtered rows.
        
        Example filters dictionary:
        all_filters1 = {
            'Captured': False,
            'Captured': True,
            'Your Name': ['Rob'], 
            'Class': '< 200',
            'Cardio Friendly': ['y'],
            'test friendly': ['y']
        }
    Returns:
    --------
    pandas.DataFrame
        The filtered DataFrame.
    """
    filtered_df1 = filter_any_and_all(df, any_filters, all_filters)
    if final_filter:
        if type(final_filter) == list:
            for index, filter in enumerate(final_filter):
                print(f'** Applying filter_df_all_conditions: Iteration {index + 1}')
                filtered_df1 = filter_df_all_conditions(filtered_df1, filter, view_columns, verbose=verbose)
                print()
        else:
            print(f'** Applying filter_df_all_conditions')
            filtered_df1 = filter_df_all_conditions(filtered_df1, final_filter, view_columns, verbose=verbose)

    print(f'\nFilter chain: Final DataFrame shape: {filtered_df1.shape}')
    return filtered_df1

def filter_any_and_all_chain(
        df, filters_dict_list, final_filter, view_columns=None,
        rank_sort=True, capture_column='To capture', trainer_column='Your Name', date_column='date added 0',
        captured_column='Captured',
        max_rows=400, final_sort=['Equipment 3', 'Exercise', 'main movement', 'secondary movement'],
        sort_na_position='first', verbose=False):
    """
    Filter a DataFrame by chaining multiple filters, each consisting of "any" and "all" conditions.

    Args:
        - df (pandas.DataFrame): The DataFrame to filter.
        - filters_dict_list (list[dict]): A list of dictionaries, each containing the "any" and "all" conditions for a filter.
        - final_filter (dict or list): The final filter to apply after all other filters, using the same syntax as the "all" condition.
        - view_columns (list[str], optional): The columns to include in the filtered DataFrame. If None, all columns are included. Defaults to None.
        - rank_sort (bool or list[str], optional): Whether to sort the filtered DataFrame by the "trainer" and "date" columns. If True, the default columns are used. If a list of column names, those columns are used instead. Defaults to True.
        - trainer_column (str, optional): The name of the column containing the trainer's name. Used for sorting. Defaults to 'Your Name'.
        - date_column (str, optional): The name of the column containing the date of the exercise. Used for sorting. Defaults to 'date added 0'.
        - captured_column (str, optional): The name of the column containing the "captured" flag. Used for printing value counts. Defaults to 'Captured'.
        - max_rows (int or None, optional): The maximum number of rows to include in the filtered DataFrame. If None, all rows are included. Defaults to 400.
        - final_sort (list[str], optional): The columns to sort the final filtered DataFrame by. Defaults to ['Equipment 3', 'main movement', 'secondary movement'].
        - sort_na_position ('first', 'last'): Where to place NaN values when sorting. Defaults to 'first'.
        - verbose (bool): If true, prints indices of filtered rows.
    Returns:
        pandas.DataFrame: The filtered DataFrame.

    Example usage:
        view_columns = df.columns[:5].tolist() + ['Your Name', 'date added 0']
        date_robs_exercises = df[df['Your Name'].str.lower() == 'rob']['date added 0'].drop_duplicates()
        any_filters1 = {
            'Your Name': ['Rob'],
            'date added 0': date_robs_exercises,
        }
        all_filters1 = {
            'Captured': False,
        }
        any_filters2 ={
            'date added 0': 'notnull',
            'To capture': 'notnull',
        }
        all_filters2 ={
            'Your Name': ['Rob'],
        }
        filters_dict_list = [
            {'any': any_filters1, 'all': all_filters1},
            {'any': any_filters2, 'all': all_filters2},
        ]
        final_filter ={
            'Captured': False,
        }
        mocap = filter_any_and_all_chain(df, filters_dict_list, final_filter, view_columns=view_columns)
    """
    
    filtered_df = df.copy()
    for index, filters_dict in enumerate(filters_dict_list):
        print(f'** Applying filter_any_and_all_conditions: Iteration {index + 1}')
        
        filtered_df = filter_any_and_all(
            filtered_df, filters_dict['any'], filters_dict['all'], view_columns)
        print()
    if final_filter:
        if type(final_filter) == list:
            for index, filter in enumerate(final_filter):
                print(f'** Applying filter_df_all_conditions: Iteration {index + 1}')
                filtered_df = filter_df_all_conditions(filtered_df, filter, view_columns, verbose=verbose)
                print()
        else:
            print(f'** Applying filter_df_all_conditions')
            filtered_df = filter_df_all_conditions(filtered_df, final_filter, view_columns, verbose=verbose)

    print(f'\nFilter chain: Filtered DataFrame shape: {filtered_df.shape}')

    if rank_sort & (type(rank_sort) != list):
        rank_sort = [capture_column, trainer_column, date_column]
    if trainer_column in rank_sort:
        print(f'\tSorting by {rank_sort}...')
        trainer_rank = {'rob': 1, 'silvia': 2}
        filtered_df['trainer_rank'] = filtered_df[trainer_column].str.lower().map(trainer_rank)
        date_robs_exercises = [time for time in filtered_df[filtered_df[trainer_column].str.lower() == 'rob'][date_column].drop_duplicates()][1:]
        print(f'Dates of Robs exercises: {date_robs_exercises}')
        filtered_df['date_rank'] = filtered_df[date_column].apply(lambda x: 1 if x in date_robs_exercises else 2)
        rank_sort = ['trainer_rank', 'date_rank']
        filtered_df = filtered_df.sort_values(rank_sort).drop(columns=rank_sort)
    if max_rows:
        if filtered_df.shape[0] > max_rows:
            print(f'\tLimiting to {max_rows} rows...')
            filtered_df = filtered_df.iloc[:max_rows]

    if final_sort:
        print(f'\tFinal sorting by {final_sort}...')
        filtered_df = filtered_df.sort_values(final_sort, na_position=sort_na_position)

    print(f'Value counts for {trainer_column}: \n{filtered_df[trainer_column].value_counts()}')
    print(f'Value counts for {captured_column}: \n{filtered_df[captured_column].value_counts()}')

    return filtered_df

def return_duplicate_rows(df, subset=None, keep=False, id_column=None, logger=None, logging_level=logging.DEBUG):
    """
    Identify duplicate rows in a dataframe.

    Parameters:
        - df (DataFrame)
        - subset (str or list): Only consider certain columns for identifying duplicates, 
            by default use all of the columns.
        - keep ('first', 'last', or None): Default 'first. Determines which duplicates (if any) to mark.
            first : Mark duplicates as True except for the first occurrence.
            last : Mark duplicates as True except for the last occurrence.
            False : Mark all duplicates as True.
    Returns:
        - DataFrame with the duplicate rows.
    """
    logger = create_function_logger('return_duplicate_rows', logger, level=logging_level)
    messages = []
    messages.append(f'***Running `return_duplicate_rows`***')
    messages.append(f'DataFrame shape: {df.shape}')
    if subset == None:
        subset = df.columns.tolist() 
    if id_column in subset:
        subset.remove(id_column)
    messages.append(f'Subset: {subset}')
    messages.append(f'Number of duplicate rows: {df.duplicated(subset=subset, keep="first").sum()}')
    duplicate_index = df.duplicated(subset=subset, keep=keep)
    duplicate_rows = df.loc[duplicate_index].sort_values(by=subset if subset else df.columns[0])
    if id_column:
        messages.append(f'{id_column} values of duplicate rows: {sorted(list(set(duplicate_rows[id_column])))}')
    messages.append(f'\tReturning {keep if keep else "all"} duplicate rows.')
    logger.debug('\n'.join(messages))
    return duplicate_rows

def remove_duplicates_by_lettercase(df, column='Reference'):
    """
    Removes rows from a pandas DataFrame if the strings in the specified column are identical aside from letter case,
    treating two white space characters the same as one white space character.

    Args:
        df (pandas.DataFrame): the DataFrame to remove duplicates from
        column (str): the name of the column containing the strings to compare (default is 'Reference')

    Returns:
        pandas.DataFrame: a DataFrame with the duplicate rows removed
    """
    print(f'Number of rows before removing duplicates: {len(df)}')
    
    # Remove excess white space characters
    df[column] = df[column].str.replace('\s+', ' ', regex=True)
    
    # Create a new column with lowercased strings
    df['lowercase_column'] = df[column].str.lower()
    
    # Drop the duplicates based on the lowercase column
    df.drop_duplicates(subset='lowercase_column', keep='first', inplace=True)
    
    # Remove the lowercase column
    df.drop('lowercase_column', axis=1, inplace=True)
    
    # Reset the index
    df.reset_index(drop=True, inplace=True)
    
    print(f'Number of rows after removing duplicates: {len(df)}')
    
    return df

def get_duplicates(
        df, subset=None, keep='first', id_column=None, duplicate_column_name='duplicate',
        logger=None, logging_level=logging.INFO, **kwargs
        ):
    """
    Add a column that indicates which rows are duplicate rows given the subset of columns.
            
    Parameters:
        - subset (list or None): Subset of column names to check. If none, all columns will be used except for id_column.
        - id_column (str): Name of the column to exclude from checking.
        - logger: Custom_Logger instance. If None, new instance is created with the logging level
            indicated by the `logging_level` parameter.
        - **kwargs are passed to the pandas `.duplicated` method.
    """
    logger = create_function_logger('get_duplicates', logger, level=logging_level)
    logger.debug('**Creating column with duplicate indicator**')
    if subset == None:
        subset = df.columns.tolist() 
    if id_column != None:
        subset.remove(id_column)
    if duplicate_column_name in subset:
        subset.remove(duplicate_column_name)
    print(f'Checking duplicates')
    df[duplicate_column_name] = df.duplicated(subset=subset, keep=keep, **kwargs)
    messages_list = []
    messages_list.append(f'Checking for duplicate rows based on these columns: {subset}')
    messages_list.append(f'\tNumber of duplicate rows `(keep={keep})`: {df[duplicate_column_name].sum()}')
    logger.log('\n'.join(messages_list))
    return df

def check_for_nulls(
        df, subset=None, id_column=None, how='all', null_column_name='null_values',
        logger=None, logging_level=logging.INFO
        ):
    """
    Add a column that indicates which rows have null values for the subset of columns.
            
    Parameters:
        - subset (list or None): Subset of column names to check. If none, all columns will be used except for id_column.
        - id_column (str): Name of the column to exclude from checking.
        - logger: Custom_Logger instance. If None, new instance is created with the logging level
            indicated by the `logging_level` parameter.
    """
    logger = create_function_logger('check_for_nulls', logger, level=logging_level)
    logger.debug('**Creating column with nulls indicator**')
    if subset == None:
        subset = df.columns.tolist() 
    if id_column != None:
        subset.remove(id_column)
    if null_column_name in subset:
        subset.remove(null_column_name)

    messages_list = []
    messages_list.append(f'Checking for null values in these columns: {subset}')
    if how == 'all':
        df[null_column_name] = df[subset].isnull().all(axis=1)
    else:
        df[null_column_name] = df[subset].isnull().any(axis=1)
    messages_list.append(f'\tNumber of null records: {df[null_column_name].sum()}')
    logger.log('\n'.join(messages_list))
    return df

def convert_dtypes(
        df, date_columns=1, format='%Y-%m-%d',
        int_columns=['index', 'total_cases', 'days_since_last_case', 'cases_when_cluster_confirmed', 'total_cases', 'doc_page_number'], 
        float_columns=None,
        description='pdfs_parsed_2023-04-02', save=False, 
        csv_path=None,
        pickle_path=r'C:\Users\silvh\OneDrive\lighthouse\portfolio-projects\BC-Covid-workplace-closures\data\interim'
        ):
    """
    Converts specified columns in a pandas DataFrame to datetime format and optionally saves the modified DataFrame.
    Originally created for BC Covid workplace closures project.

    Args:
        - df (pandas DataFrame): DataFrame to be modified
        - date_columns (dict or list, optional): Either a dictionary of {column_name: datetime_format} 
            or a list of column names to be converted to datetime format. Defaults to 1.
        - format (str, optional): The format string for the date_columns. Defaults to '%Y-%m-%d'.
        - description (str, optional): The description to be used in the saved output file name. Defaults to 'pdfs_parsed_2023-04-30'.
        - save (bool, optional): Whether or not to save the modified DataFrame. Defaults to False.
        - csv_path (str, optional): The file path for the saved csv file. If None, csv file will not be saved. Defaults to None.
        - pickle_path (str, optional): 

    Returns:
    pandas DataFrame: Modified DataFrame with specified columns converted to datetime format.
    """
    if (type(date_columns) != list) & (type(date_columns) != str):
        date_columns = [
            'date_cluster_confirmed_public_health', 'date_cluster_no_longer_active',
            'earliest_reported_cases', 'latest_reported_cases', 
            'closure_date'
        ]
    print(f'Converting columns to datetime: {[col for col in date_columns]}')
    df[date_columns] = df[date_columns].apply(pd.to_datetime, format=format)
    if (float_columns is None) & (int_columns is None):
        float_columns = list(df.columns)
    if float_columns is not None:
        print(f'Converting columns to float: {[col for col in float_columns]}')
        for column in float_columns:
            print(f'\t{column}')
            df[column] = df[column].apply(pd.to_numeric, errors='coerce')
    if int_columns is not None:
        print(f'Converting columns to integers: {[col for col in int_columns]}')
        for column in int_columns:
            print(f'\t{column}')
            df[column] = df[column].apply(pd.to_numeric, errors='coerce', downcast='integer')
    print(f'dtypes: {df.dtypes}')
    if save:
        try:
            save_output(
                df, description=description+'_dtypes_converted', pickle_path=pickle_path, csv_path=csv_path)
        except:
            print('Unable to save outputs')
    return df

def eda(df):
    """
    Exploratory data analysis for a pandas DataFrame.
    """
    print(f'DataFrame shape: {df.shape}')
    print(f'Dataframe data types:\n{df.dtypes}')
    categorical_columns = df.select_dtypes(include=['object']).columns
    for column in categorical_columns:
        print(f'Unique values in {column} (n={df[column].nunique()}):')
        print(f'\t{[value for value in df[column].sort_values().unique()]}')

def rename_duplicate_columns(df):
    """
    Identifies duplicate columns in a pandas dataframe and appends a number to the end of the column name
    if a duplicate is found.

    Parameters:
    - df: pandas dataframe

    Returns:
    - df: pandas dataframe with unique column names
    """
    # Create a copy of the dataframe to avoid modifying the original
    # print(f'Original columns: {[column for column in df.columns]}')
    df = df.copy()

    # Create a dictionary to store column names and their respective counts
    column_counts = {}
    new_column_names = []

    # Iterate over the columns of the dataframe
    for index, column in enumerate(df.columns):
        # Check if the column name is already present in the dictionary
        if column in column_counts:
            # Increment the count of the column name
            column_counts[column] += 1

            # Append the count to the column name
            new_column = f"{column}{column_counts[column] + 1:1d}"

            new_column_names.append(new_column)
            print(f'Column "{df.iloc[:, index].name}" renamed to "{new_column}"')
        else:
            # Add the column name to the dictionary with a count of 0
            column_counts[column] = 0
            new_column_names.append(column)
    df.columns = new_column_names
    print(f'\nUpdated columns: {[column for column in df.columns]}')

    return df

def text_to_list(string):
    """
    Separate each new line by a comma.
    """
    string = string.strip().replace('\n', "', '")
    return string

def print_dict_values_for_key(results_dict, key, zero_indexed=False):
    """
    Prints the values of a dictionary for a given key.

    Parameters:
    - results_dict (dict): Dictionary to print values for.
    - key (str): Dictionary key to print values for.
    - zero_indexed (bool): If True, prints the index of each value starting from 0. If False, prints the index starting from 1.
    """
    for index, item in enumerate(results_dict):
        print(f"{index+1 if zero_indexed==False else index}: {results_dict[item].get(key, 'None').strip()}", end='\n\n')

def convert_to_pascal_case(text):
    words = text.split()
    words = [w.title() for w in words]
    return ''.join(words)


# convert dates from string to datetime objects
def date_columns(df,date_column='fl_date',format='%Y-%m-%d'):
    """ 
    Take the dates in a dateframes to create new columns:
        _date_standard: Datetime data 
        _year
        _month
    Parmaters:
    - df: Dataframe.
    - date_column: Name of the column containing the date strings.
    - Format: Original date format in the dateframe. Default: '%d.%m.%Y'
    
    Make sure to do the following import: 
    from datetime import datetime
    """

    date_column=str(date_column)
    
    # df[str(date_column+'_year')] = pd.to_datetime(df[date_column],
    #     format='%d.%m.%Y')
    date = pd.to_datetime(df[date_column],
        format=format)
    # df.get(str(date_column+'_standard'),date)
    # df.get(str(date_column+'_year'),date.dt.year)
    # df.get(str(date_column+'_month'),date.dt.month)
    df[str(date_column+'_standard')] = date
    df[str(date_column+'_year')] = date.dt.year
    df[str(date_column+'_month')] = date.dt.month
    print('\tTime completed:', datetime.now())
    return df

def compare_iterables(iterable1, iterable2, print_common=False, print_difference=True, logger=None, logging_level=logging.DEBUG):
    """
    Print the number of common values and unique values between two iterables (e.g. lists, series).
    
    Returns:
        - different_values (list)
        - common_values (list)           
    """
    logger = create_function_logger('compare_iterables', logger, level=logging_level)
    common_values = set(iterable1) & set(iterable2)
    info_message = '***`compare_iterables`***: \n'
    debug_message = ''

    if len(iterable1) > len(iterable2):
        larger_set = set(iterable1)
        smaller_set = set(iterable2)
    else:
        larger_set = set(iterable2)
        smaller_set = set(iterable1)
    different_values = list(larger_set - smaller_set)
    debug_message += f'Proper subset = {smaller_set < larger_set} \n'
    opposite_subtraction = list(smaller_set - larger_set)
    debug_message = f'\tOpposite set subtraction ({len(opposite_subtraction)} values): {opposite_subtraction}\n'
    debug_message += f'Unique values in iterable 1: {len(set(iterable1))}\n'
    debug_message += f'Unique values in iterable 2: {len(set(iterable2))}\n'
    info_message += f'Number of common values between iterables 1 and 2: {len(common_values)}\n'
    info_message += f'Number of different values between iterables 1 and 2: {len(different_values)}\n'
    if (logger.console_handler.level <=10) | (print_common == True):
        info_message += f'Values in common: {common_values} \n'
    else:
        debug_message +=  f'Values in common: {common_values} \n'
    if (logger.console_handler.level <=10) | (print_difference == True):
        info_message += f'Different values: {different_values} \n'
    else:
        debug_message += f'Different values: {different_values} \n'
    logger.info(info_message)
    logger.debug(debug_message)
    return different_values, common_values

def find_unique_df_ids(df1, df1_column, df2, df2_column, **kwargs):
    """
    Print the number of common values and unique values between two DataFrame columns.
    
    Returns:
        - different_values (list)
        - common_values (list)           
    """        
    different_ids, common_ids = compare_iterables(
        df1[df1_column].values, df2[df2_column], **kwargs
    )
    return different_ids, common_ids

def compare_df_columns(
        df1, df1_column, df2, df2_column,print_common=False,print_difference=True, logger=None, logging_level=logging.DEBUG
        ):
    """
    Print the number of common values and unique values between two dataframe columns.
    Return the unique rows of the dataframe with more records.
    
    """
    logger = create_function_logger('compare_iterables', logger, level=logging_level)
    df1_values = df1[df1_column].values
    df2_values = df2[df2_column].values
    different_values, common_values = compare_iterables(
        df1[df1_column].values, df2[df2_column], 
        print_common=print_common, print_difference=print_difference,
        logger=logger, logging_level=logging_level
    )
    if df1.equals(df2):
        logger.info(f'Returning rows in DataFrame where {df1_column} != {df2_column}')
        return df1[df1[df1_column] != df1[df2_column]].dropna(subset=[df1_column, df2_column], how='all')
    else:
        logger.info(f'Returning different rows of the larger DataFrame.')
        if len(df1_values) > len(df2_values):
            parent_df = df1
            parent_df_column = df1_column
        else:
            parent_df = df2
            parent_df_column = df2_column
        return parent_df[parent_df[parent_df_column].isin(different_values)]

    
def drop_na(df, subset=None, logger=None, logging_level=logging.INFO, **kwargs):
    logger = create_function_logger('drop_na', logger, level=logging_level)
    messages = []
    before_length = len(df)
    messages.append(f'***Running `drop_na`***')
    messages.append(f'Shape before dropping nulls: {df.shape}')
    df = df.dropna(subset=subset, how='all')
    messages.append(f'\tShape after dropping nulls: {df.shape}')
    messages.append(f'\t{before_length - len(df)} rows dropped')
    logger.info('\n'.join(messages))
    return df

# function that prints null values
def explore(df,id=0,print_n_unique=False, printValues=False, axis=0):
    """
    Explore dataframe data and print missing values.
    Parameters:
    - df: Dataframe.
    - id: Column number or name with the primary IDs. Default is zero.
    - print_n_unique (bool): If the number of unique values in the first column doesn't match 
        the number of rows in the df, print the number of unique values in each column to see if 
        there's another column that might serve as a unique id.
    """

    if (id==False) & (id !=0):
        pass
    elif isinstance(id,int):
    # if type(id)==int:
        print(f'Unique IDs: {len(set(df.iloc[:,0]))}. # of rows: {df.shape[0]}. Match: {len(set(df.iloc[:,0]))==df.shape[0]}')
    else:
        print(f'Unique IDs: {len(set(df[id]))}. # of rows: {df.shape[0]}. Match: {len(set(df[id]))==df.shape[0]}')
    
    # if the number of unique values in the first column doesn't match the number of rows in the df,
    # print the number of unique values in each column to see if there's another column that migh
    # serve as a unique id.
    if (print_n_unique==True):
        if len(set(df.iloc[:,0])) !=df.shape[0]: 
            for column in df.columns:
                print(len(df[column].value_counts()),'\t', column)
    
    # count amount of missing values in each column
    total = df.isnull().sum(axis=axis).sort_values(ascending=False) 
    # % of rows with missing data from each column
    percent = (df.isnull().sum(axis=axis)/df.isnull().count(axis=axis)).sort_values(ascending=False)
    # return percent

    # create a table that lists total and % of missing values starting with the highest
    missing_data = pd.concat([total, percent], axis=1, keys=['Total', 'Percent']) 

    if (printValues == True):
        # extract the names of columns with missing values
        cols_with_missing = missing_data[missing_data.Percent > 0].index.tolist()
        print(df.dtypes[cols_with_missing])

    print(f'')
    return missing_data

def drop_features(df,threshold=100, show_update=True):
    """
    Drop columns in a dataframe with null values above the specified threshold.
    Parameters:
    - df: Dataframe.
    - threshold (float): Float between 0 and 100. 
        Threshold of % null values over which columns will be dropped.
    - show_update: If true, show missing values for the updated dataframe
        (calls the custom function explore)
    """ 
    
    # count amount of missing values in each column
    total = df.isnull().sum().sort_values(ascending=False) 
    # % of rows with missing data from each column
    percent = (df.isnull().sum()/df.isnull().count()).sort_values(ascending=False) 

    # create a table that lists total and % of missing values starting with the highest
    missing_data = pd.concat([total, percent], axis=1, keys=['Total', 'Percent']) 

    filter = missing_data['Percent'] > threshold
    to_drop = missing_data[filter].index.tolist()
    df.drop(to_drop, axis=1, inplace=True)
    print(f'Threshold of percentage values for dropping columns: {threshold}')
    print(f'Columns dropped: {to_drop}')
    if show_update == True:
        return explore(df,id=0,print_n_unique=False, printValues=False)