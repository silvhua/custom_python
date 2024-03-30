import sys
sys.path.append(r"C:\Users\silvh\OneDrive\lighthouse\custom_python")
from silvhua import *
from wrangling import *
import numpy as np
from Custom_Logger import *

def load_and_describe_csv(
        filename, path, subset=None, id_column=0, 
        logger=None, logging_level=logging.INFO, file_level=logging.DEBUG, **kwargs
    ):
    """
    Load a CSV as a dataframe and list the dataframe's columns and data types.

    Parameters:
    - filename (str)
    - path (raw string): Use the format r'<path>'. If None, file is saved in the same directory.
    - kwargs: Additional arguments to pass to pd.read_csv
    """
    messages_list = []
    logger = create_function_logger(
        'load_and_describe_csv', logger, level=logging_level, file_level=file_level
    )
    df = load_csv(filename, path, **kwargs)
    logger.info(f'\n***Running `load_and_describe_csv`***\n\tfilename: {filename}; subset: {subset}; id_column: {id_column}; kwargs: {kwargs}')
    messages_list.append(f'Dataframe shape: {df.shape}')
    messages_list.append(f'DataFrame columns: {[col for col in df.columns]}')
    messages_list.append(f'\tTime completed: {datetime.now()}')
    if type (id_column) == int:
        id_column = df.columns[id_column]
    if subset == None:
        subset = df.columns.tolist() 
    if id_column != None:
        subset.remove(id_column)
    duplicate_rows = return_duplicate_rows(
        df, subset=subset, id_column=id_column, logger=logger, logging_level=logging_level
        )
    messages_list.append(f'\tNumber of null records: {df[subset].isnull().all(axis=1).sum()}')
    logger.debug('\n'.join(messages_list))
    logger.debug(df.dtypes)
    return df

def drop_rows_with_value(
    df, column, value=True, drop_column=True,
    logger=None, logging_level=logging.INFO, 
    ):
    logger = create_function_logger('drop_rows_with_value', logger, level=logging_level)
    messages = []
    before_length = len(df)
    messages.append(f'\n***Running `drop_rows_with_value` using column "{column}" with value `{value}`***')
    messages.append(f'\tShape before: {df.shape}')
    df = df.drop(df[df[column] == value].index)
    if drop_column:
        messages.append(f'\t\tDropping column "{column}"')
        df.drop(columns=[column], inplace=True)
    messages.append(f'\tShape after: {df.shape}')
    messages.append(f'\t{before_length - len(df)} rows dropped')
    logger.info('\n'.join(messages))
    return df

def table_check(
        result_df, final_columns, drop_na=False,
        logger=None, logging_level=logging.DEBUG,
        **kwargs
        ):
    logger = create_function_logger('table_check', logger, level=logging_level)
    logger.info(f'\n***Running `table_check`***\n\t**kwargs: {kwargs}')
    result_df = result_df.replace({-1: None}).replace({np.nan: None})[final_columns]
    result_df = check_for_nulls(
        result_df, **kwargs, logger=logger
    )
    duplicate_column_name = 'table_check_duplicate' if 'duplicate' in result_df.columns else 'duplicate'
    result_df = get_duplicates(
        result_df, logger=logger, duplicate_column_name=duplicate_column_name
    )
    result_df = drop_rows_with_value(
        result_df, column=duplicate_column_name, value=True, drop_column=True, logger=logger
    )
    id_column = kwargs.get('id_column', None)
    subset = kwargs.get('subset', None)
    if (id_column == None) & (subset == None):
        drop_na = True
    null_column_name = kwargs.get('null_column_name', 'null_values')
    if drop_na:
        result_df = drop_rows_with_value(
            result_df, column=null_column_name, value=True, drop_column=True, logger=logger
        )
    else:
        result_df.drop(columns=[null_column_name], inplace=True)
    return result_df 

def save_tables(
    result, table_name, 
    exceptions_filter={'null_values': [True]}, exceptions_any_filters=None,
    columns_to_drop=[], excel=False, append_version=False,
    path = r'C:\Users\silvh\Documents\Cascadia local', excel_filename='CYSIS Data Mapping local',
    logger=None,
    **review_filter_kwargs
    ):
    """
    Remove extra columns to save a version of the table that is ready for load.
    Filter rows to be excluded (`exceptions_filter`) and save them separately.
    Filter rows to be reviewed by the client (`**review_filter_kwargs`) and save them separately as an Excel file.
    """
    rows_to_remove = None
    logger = create_function_logger('save_tables', logger, level=10)
    logger.info(f'*****Running `save_tables`*****')
    if exceptions_filter:
        exceptions = filter_any_and_all(
            result, all_filters=exceptions_filter, any_filters=exceptions_any_filters
            )
        save_csv(
            exceptions, filename=f'{table_name} exceptions', path=path,  
            append_version=append_version
        )
    if review_filter_kwargs:
        for_review = filter_df_any_condition(result, **review_filter_kwargs)
        col_width = {col: 20 for col in for_review.columns}
        save_excel(
            for_review, filename=f'{table_name} for review', path=path, col_width=col_width, 
            append_version=append_version, overwrite=True
        )
    if type(columns_to_drop) == str:
        columns_to_drop = [columns_to_drop]
    merge_columns = result.columns[result.columns.str.contains('_merge')].tolist()
    columns_to_drop += merge_columns
    if 'duplicate' in result.columns:
        columns_to_drop += ['duplicate']
    result = result.drop(columns=columns_to_drop)
    if exceptions_filter:
        rows_to_remove = exceptions.index
        result.loc[rows_to_remove, 'exception'] = True
        result = drop_rows_with_value(
            result, column='exception', value=True, drop_column=True,
            logger=logger
        )
    save_csv(
        result,
        filename = table_name,
        path = path
    )
    if excel:
        save_excel(
            result,
            filename = excel_filename,
            path = r'C:\Users\silvh\Documents\Cascadia local',
            sheet_name = table_name,
            wrapping=False,
            col_width = None,
            overwrite=True
        )

def concat_columns(df, columns, new_column, sep='; ', drop_columns=False,
    logger=None
    ):
    logger = create_function_logger('merge_and_validate', logger)
    try:
        df[columns] = df[columns].replace({np.nan: ''}).replace({-1: ''}).astype(str)
        df[new_column] = df[columns[0]]
        for column in columns[1:]:
            df[new_column] = df[new_column].str.cat(df[column], sep=sep)
        df[new_column] = df[new_column].replace({sep * (len(columns) - 1): None}).str.strip(sep)
        if drop_columns:
            df = df.drop(columns=columns)
    except Exception as error:
        exc_type, exc_obj, tb = sys.exc_info()
        f = tb.tb_frame
        lineno = tb.tb_lineno
        filename = f.f_code.co_filename
        message = f'An error occurred on line {lineno} in {filename}: {error}.'
        print(message)
    return df

def merge_and_validate(
        left_df, right_df, left_on, right_on, how='outer', indicator=True, drop_duplicates=False,
        nan_fill=None, left_df_name='left', right_df_name='right', drop_indictor_column=False, id_column='RID',
        logger=None
        ):
    merged_df = pd.DataFrame()
    try:
        logger = create_function_logger('merge_and_validate', logger)
        if nan_fill:
            left_df[left_on] = left_df[left_on].replace({np.nan: nan_fill})
        indicator_root = '_merge' if indicator == True else indicator
        indicator = indicator_root
        merge_integer = 1
        info_messages = []
        debug_messages = []
        while indicator in left_df.columns:
            merge_integer +=1
            indicator = f'{indicator}{merge_integer}'
        info_messages.append(f'****`merge_and_validate`****: Total rows: {left_df.shape[0] + right_df.shape[0]}')
        common_columns = list(set(left_df.columns.tolist()).intersection(
            set(right_df.columns.tolist())) - set([left_on] if type(left_on)==str else left_on))
        info_messages.append(f'Performing {how} merge: {left_df_name} on `{left_on}` and \n\t{right_df_name} on `{right_on}`.')
        info_messages.append(f'`Using `{indicator}` as indicator column')
        logger.info('\n'.join(info_messages))
        debug_messages.append(f'\tLeft DF shape: {left_df.shape}\n\tRight DF shape: {right_df.shape}\n\tCommon columns: {common_columns}')
        
        merged_df = left_df.merge(
            right_df, how=how, indicator=indicator, suffixes=(None, '_y'),
            left_on=left_on, right_on=right_on
        )
        merge_info_message = ''
        merge_info_message += f'Shape after initial merge: {merged_df.shape}\n'
        debug_messages.append(f'Columns after merge: {[column for column in merged_df.columns]}')

        merge_info_message += f"Merge indicator value counts: {merged_df[indicator].value_counts()}\n"
        
        merged_df[indicator] = merged_df[indicator].replace({
            'left_only': left_df_name, 'right_only': right_df_name, 
            'both': f'{left_df_name}, {right_df_name}'
        })
        
        merge_info_message += f"\tSum: {merged_df[indicator].value_counts().sum()}\n"
        
        duplicate_rows = return_duplicate_rows(merged_df, logger=logger)
        if drop_duplicates:
            merged_df = merged_df.drop_duplicates(subset=[left_on, right_on], keep='first')
            merge_info_message += f'\tShape after dropping duplicates: {merged_df.shape}\n'
        else:
            merge_info_message += f'\tDrop duplicates = {str(drop_duplicates)}\n'
        
        for column in common_columns:
            if column != id_column:
                merged_df[column] = merged_df[column].fillna(merged_df[f'{column}_y'])
        if (right_on != left_on) & (right_on in common_columns):
            merged_df[left_on] = merged_df[left_on].fillna(merged_df[right_on])
        logger.debug('\n'.join(debug_messages))
        logger.info(merge_info_message)
        columns_to_drop = [column for column in merged_df.columns if column.endswith('_y')]
        if drop_indictor_column:
            columns_to_drop.append(indicator)
        
        merged_df = merged_df.drop(columns=columns_to_drop)
    except Exception as error:
        exc_type, exc_obj, tb = sys.exc_info()
        f = tb.tb_frame
        lineno = tb.tb_lineno
        filename = f.f_code.co_filename
        message = f'An error occurred on line {lineno} in {filename}: {error}.'
        logger.error(message)
    
    return merged_df

def concatenate_df(dfs_list, axis=0, renaming_dict={}, logger=None):
    """
    A function to concatenate a list of DataFrames along a specified axis with optional renaming of columns.
    
    Parameters:
    - dfs_list: list of pandas DataFrames to concatenate.
        Each item in the list can be a pandas DataFrame or a tuple of (df_name, df) 
        where df_name is the name of the DataFrame and df is the DataFrame itself.
    - axis: axis along which to concatenate the DataFrames (default is 0)
    - renaming_dict: dictionary to rename columns (default is an empty dictionary)
    - logger: optional Custom_Logger object for logging messages
    
    Returns:
    - concatenated_df: the concatenated pandas DataFrame
    """
    concatenated_df = pd.DataFrame()
    try:
        logger = create_function_logger('concatenate_df', logger)
        logger.info(f'Concatenating {len(dfs_list)} DataFrames...')
        logger.debug(f'\tRenaming dict: {renaming_dict}')
        info_message = []
        parsed_dfs_list = []
        for index, df_tuple in enumerate(dfs_list):
            if isinstance(df_tuple, pd.DataFrame):
                df_name = f'df_{index}'
                df = df_tuple
            else: # if df_tuple is a tuple or list
                df_name = df_tuple[0]
                df = df_tuple[1]
            info_message.append(f'\t`{df_name}` DataFrame shape: {df.shape}')
            df['source_table'] = df_name
            if (len(renaming_dict) > 0) & (axis == 0):  
                df = df.rename(columns=renaming_dict) 
            parsed_dfs_list.append(df)
        if len(parsed_dfs_list) > 1:
            different_columns = compare_iterables(
                parsed_dfs_list[0].columns, parsed_dfs_list[1].columns, print_common=0,
                print_difference=0, logger=logger
                )    
        concatenated_df = pd.concat(parsed_dfs_list, axis=axis)  
        logger.info(f'\tShape after concatenation: {concatenated_df.shape}')
    except Exception as error:
        exc_type, exc_obj, tb = sys.exc_info()
        f = tb.tb_frame
        lineno = tb.tb_lineno
        filename = f.f_code.co_filename
        message = f'An error occurred on line {lineno} in {filename}: {error}.'
        logger.error(message)
    return concatenated_df.reset_index(drop=True)

def melt_dfs(dfs_list, id_vars, value_vars, var_name, value_name, date_columns, renaming_dict={}, logger=None, **kwargs):
    melted_df = pd.DataFrame()
    try:
        logger = create_function_logger('melt_dfs', logger)
        logger.info(f'Melting {len(dfs_list)} DataFrames...')    
        concatenated_df = concatenate_df(dfs_list, axis=0, renaming_dict=renaming_dict, logger=logger)    
        for column in date_columns:
            concatenated_df[column] = concatenated_df[column].apply(lambda x: remove_time_from_date_string(x))
        melted_df = pd.melt(
            concatenated_df, 
            id_vars=id_vars+['source_table'], value_vars=value_vars, var_name=var_name, value_name=value_name, 
            **kwargs
        )    
        logger.info(f'\tShape after melting: {melted_df.shape}')
    except Exception as error:
        exc_type, exc_obj, tb = sys.exc_info()
        f = tb.tb_frame
        lineno = tb.tb_lineno
        filename = f.f_code.co_filename
        message = f'An error occurred on line {lineno} in {filename}: {error}.'
        logger.error(message)
    return melted_df

def merge_to_replace(
        left_df, right_df, left_on, right_index_column, value_column, nan_fill=None, 
        left_df_name='left', right_df_name='right', drop_indictor_column=False, logger=None
        ):
    logger = create_function_logger('merge_to_replace', logger)
    if nan_fill:
        left_df[left_on] = left_df[left_on].replace({np.nan: nan_fill})
    initiate_messages = []
    info_messages = []
    debug_messages = []
    initiate_messages.append(f'\n****`merge_to_replace`****: \nright index length: {len(right_df.index)}')
    initiate_messages.append(f'Merging on: \n\tLeft: {left_on}\n\tRight: {right_index_column}')
    debug_messages.append(f'right index unique values : {len(right_df.index.unique())}')
    
    debug_messages.append(f'left_df[left_on] shape {left_df[left_on].shape}')
    indicator_root = '_merge'
    indicator = indicator_root
    merge_integer = 1
    while indicator in left_df.columns:
        merge_integer +=1
        indicator = f'{indicator_root}{merge_integer}'
    initiate_messages.append(f'`Using `{indicator}` as indicator column')
    logger.info('\n'.join(initiate_messages))
        
    try:
        if value_column in left_df.columns:
            new_value_column = f'{value_column}_y'
            right_df = right_df.rename(columns={value_column: new_value_column})
            value_column = new_value_column
        else:
            new_value_column = value_column 
        debug_messages.append(f'Before `merge_to_replace`: ')
        debug_messages.append(f'\tLeft DataFrame shape: {left_df.shape}')
        debug_messages.append(f'\t\tColumns:{[col for col in left_df.columns]}')
        debug_messages.append(f'\tright_df[value_column] shape {right_df[new_value_column].shape}')
        debug_messages.append(f'\t\tColumns:{[col for col in right_df.columns]}')
        right_df = right_df.copy().set_index(right_index_column)
        column_to_fill = left_on if type(left_on) == str else left_on[-1] 
        info_messages.append(f'column_to_fill: {column_to_fill}')
        info_messages.append(f'Value column: {value_column}')
        # In case there are duplicate values in any of the merge columns, merge the dataframes, then 
        # drop the extra column.
        debug_messages.append(f'Null values in right DF {value_column}: {right_df[value_column].isna().sum()}')
        left_df = left_df.merge(
                right_df[value_column], how='left', left_on=left_on, right_index=True,
                indicator=indicator
            )
        left_df[column_to_fill] = left_df[value_column]
        info_messages.append(f"Merge indicator value counts: {left_df[indicator].value_counts()}\n")
        left_df[indicator] = left_df[indicator].replace({
            'left_only': left_df_name, 'right_only': right_df_name, 
            'both': f'{left_df_name}, {right_df_name}'
        })
        if column_to_fill in value_column:
            left_df[column_to_fill] = left_df[column_to_fill].fillna(left_df[value_column])
        columns_to_drop = [value_column]
        if drop_indictor_column:
            columns_to_drop.append(indicator)
        left_df = left_df.drop(columns=columns_to_drop)
        debug_messages.append(f'After `merge_to_replace`: \n\tColumns: {[col for col in left_df.columns]}')
        logger.debug('\n'.join(debug_messages))
        info_messages.append(f'\tLeft DataFrame shape: {left_df.shape}')
        logger.info('\n'.join(info_messages))
        duplicate_rows = return_duplicate_rows(left_df, logger=logger)
    except Exception as error:
        exc_type, exc_obj, tb = sys.exc_info()
        f = tb.tb_frame
        lineno = tb.tb_lineno
        filename = f.f_code.co_filename
        message = f'An error occurred on line {lineno} in {filename}: {error}.'
        logger.error(message)
    return left_df

def one_row_per_id(
    df, id_column='kIntakeID', sep='_'
    ):
    """
    Reshape a DataFrame that has multiple rows for a given ID value so that every ID value only
    has 1 row in the DataFrame. Value columns are added based on the maximum number of 
    rows per ID in the original dataframe. 
    """
    reshaped_df, group_value_columns_dict = pd.DataFrame(), {}
    print(f'\n***Reshaping DataFrame with `one_row_per_id`***\n')
    try:
        def number_rows_in_group(groupby):
            groupby = groupby.reset_index(drop=True)
            return groupby

        print(f'Initial shape: {df.shape}')
        original_columns = df.columns.tolist()
        original_columns.remove(id_column)
        reshaped_df = pd.DataFrame()
        print(f'Original columns without id_column: {original_columns}')
        reshaped_df = df.groupby(id_column).apply(lambda x: number_rows_in_group(x))
        reshaped_df = reshaped_df.unstack()
        reshaped_df = reshaped_df.sort_index(axis=1, level=-1)
        new_columns = []
        for column_tuple in reshaped_df.columns:
            new_columns.append(f'{column_tuple[0]}{sep}{column_tuple[1]}')
        reshaped_df.columns = new_columns
        n_groups = reshaped_df.columns.str.contains(original_columns[0]).sum()
        print(f'Number of groups: {n_groups}')
        final_columns = [id_column]
        group_value_columns_dict = {}
        # for group in range(1, n_groups + 1):
        for group in range(n_groups):        
            group_value_columns = []
            for original_column in original_columns:
                group_value_columns.append(f'{original_column}{sep}{group}')
            final_columns += group_value_columns
            group_value_columns_dict[group] = group_value_columns
        reshaped_df = reshaped_df.reset_index()
        reshaped_df = reshaped_df[final_columns]
        print(f'Final shape: {reshaped_df.shape}')
        print(f'final columns: {[column for column in reshaped_df.columns]}')    
    except Exception as error:
        exc_type, exc_obj, tb = sys.exc_info()
        f = tb.tb_frame
        lineno = tb.tb_lineno
        filename = f.f_code.co_filename
        message = f'An error occurred on line {lineno} in {filename}: {error}.'
        print(message)
    return reshaped_df, group_value_columns_dict
    
def map_to_new_column(
        df, mapping, map_from_column, map_to_column, normalize_casing=True, logger=None
        ):
    """
    A function to map values from one column to another based on a provided mapping.
    
    Parameters:
    - df: The DataFrame to operate on
    - mapping: A dictionary containing the mapping of values
    - map_from_column: The column in df to map values from
    - map_to_column: The column in df to map values to
    - normalize_casing: A boolean indicating whether to normalize the casing of keys
    - logger: An optional Custom_Logger object for logging information
    
    Returns:
    - The DataFrame with the values mapped to the new column
    """
    final_mapping = {}
    logger = create_function_logger('map_to_new_column', logger)
    if normalize_casing:
        for key, value in mapping.items():
            final_mapping[key.lower()] = value
    else:
        final_mapping = mapping
    df[map_to_column] = df[map_from_column].str.lower().map(final_mapping)
    logger.debug(f'Final mapping in `map_to_new_column`: {final_mapping}\nColumns after `map_to_new_column`: {df.columns}')
    return df

def remove_time_from_date_string(date_string, delimiter=' '):
    if type(date_string) == str:
        date = date_string.split(delimiter)[0] if delimiter in date_string else date_string
    elif type(date_string) == pd.Series:
        date = date_string.replace(rf'^(.*){delimiter}.*', r'\1', regex=True)
    else:
        date = None
    return date

def spreadsheet_to_dict(string):
    """
    Made so you can copy data from 2 columns of a Google sheet and convert into a dictionary
    Where the left column text is the key and the right column text is the value of the dictionary.
    Created originally for CYSIS table mapping project.
    """
    result = string.strip()
    result = re.sub(r'\n', r', ', result)
    result = re.sub(r'\t', r': ', result)
    result = re.sub(r'([a-zA-Z0-9_]+)', r'"\1"', result)
    result = "{" + result + "}"
    print(f'result string: \n{result}')
    result = json.loads(result)
    print(f'Number of dictionary items: {len(result)}')
    return result

def map_many_to_one(row, columns, new_column, mapping_dict):
    key = '__'.join([row[col] for col in columns])
    row[new_column] = mapping_dict.get(key, None)
    # if row[new_column] == None:
    #     print(f'index {row.name} key {key} has no value')
    return row

def get_dropdown_values(
        df, dropdown_columns, 
        dropdown_values_df, right_index_column='RID', value_column='cValues',         
        ):
    """[not needed if table is to be reshaped]
    Use this if needing to replace values using `merge_to_replace` on multiple columns using the
    same values table.
    """
    print(f'Getting dropdown values for {len(dropdown_columns)} columns...')
    for column in dropdown_columns:
        print(f'\t{column} Unique values: {[value for value in df[column].unique()]}')
        df = merge_to_replace(
            df, dropdown_values_df,
            left_on=column, 
            right_index_column=right_index_column, 
            value_column=value_column, nan_fill=-1
        )  
    return df

def to_iso8601(
        series, from_tz=None, to_tz='UTC', iso=True, logger=None, logging_level=logging.DEBUG, 
        **kwargs
        ):
    """
    Converts a given series of datetime values to ISO 8601 format.

    Parameters:
        -series (pandas.Series): The series of datetime values to be converted.
        - from_tz (str, optional): The timezone of the input series. Defaults to None.
        - to_tz (str, optional): The timezone to convert the series to. Defaults to 'UTC'.
        - iso (bool, optional): Whether to use the alpha_tz function to put the timezone in
        ISO 8601 format (True)or human-readable format (False), e.g. 'EST'. 
        Defaults to True to preserve ISO 8601 format.
        - **kwargs: Additional keyword arguments to pass to `pd.to_datetime()`.

    Returns:
        pandas.Series: The series of datetime values converted to ISO 8601 format, or None if the input can't be converted.

    Raises:
        ValueError: If `from_tz` is not a valid timezone.

    Note:
        The output series will have the format '%Y-%m-%dT%H:%M:%S.%fZ' if `to_tz` is 'UTC',
        and '%Y-%m-%dT%H:%M:%S.%f%z' otherwise.
    """
    logger = create_function_logger('to_iso8601', logger, level=logging_level)
    logger.info(f'***Running `to_iso8601` on column {series.name}***')
    try:
        if not isinstance(series, pd.Series):
            raise TypeError("`series` must be a pandas.Series, not {}".format(type(series)))

        datetime_series = pd.to_datetime(series, **kwargs)
        if from_tz:
            datetime_series = datetime_series.dt.tz_localize(from_tz).dt.tz_convert(to_tz)

        # return datetime_series
        formatted_series_no_tz = datetime_series.dt.strftime('%Y-%m-%dT%H:%M:%S.') + datetime_series.dt.strftime('%f').str[:3]
        if to_tz == 'UTC':
            formatted_series = formatted_series_no_tz + 'Z'
        elif iso == True:
            formatted_series = formatted_series_no_tz + datetime_series.dt.strftime('%z')
        else:
            logger.debug(f'Using human-readable format for column {series.name}')
            formatted_series = formatted_series_no_tz + datetime_series.dt.strftime('%Z')
    except Exception as e: # Use regex to convert the timestamp to ISO 8601 format
        logger.debug(f'Using regex to convert to ISO 8601 format for column {series.name}: \n{e}')        
        replacement_dict = {
            r'(\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}:\d{2})$': r'\1T\2.000Z',
            r'(\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}:\d{2})(\.\d)$': r'\1T\2\300Z',
            r'(\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}:\d{2})(\.\d{2})$': r'\1T\2\30Z',
            r'(\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}:\d{2})(\.\d{3})': r'\1T\2\3Z',
            }
        series_str = series.astype(str)
        formatted_series = series_str.replace(replacement_dict, regex=True)
    return formatted_series
    
def columns_to_function(
        df, columns, function, suffix=None, logger=None, logging_level=logging.DEBUG, drop=True, **kwargs
        ):
    """
    Apply a function to specified columns of a DataFrame.

    Parameters:
    - df (pandas.DataFrame): The input DataFrame.
    - columns (list): The list of columns to apply the function to.
    - function (function): The function to apply to the columns.
    - suffix (str): The suffix to append to the new column names.
    - logger (logging.Logger): The logger to use for logging.
    - logging_level (int): The logging level to use.
    - drop (bool): Whether to drop the original columns after creating the new ones.
    - **kwargs: Additional keyword arguments to pass to the function.

    Returns:
    - pandas.DataFrame: A new DataFrame with the new columns.

    """
    def validate_regex(row):
        if row.str.contains('\[invalid\]').any():
            row = row.replace({None: ''})
            invalid_values = ', '.join(row[row.str.contains(f'{kwargs["tag"]}')].values)
            return invalid_values
        else:
            return None
        
    debug_messages = []
    if suffix==None:
        suffix = function.__name__
    logger = create_function_logger('columns_to_function', logger, level=logging_level)
    debug_messages.append(f'`columns_to_function` function: {function.__name__}')
    debug_messages.append(f'`columns_to_function` input columns: {columns}')
    new_columns = [f'{column}_{suffix}' for column in columns] if drop == False else columns
    debug_messages.append(f'`columns_to_function` output columns: {new_columns}')
    df[new_columns] = df[columns].apply(lambda x: function(
        x, logger=logger, logging_level=logging_level, **kwargs
        ), axis=0)
    if function == verify_regex:
        # Determine if the passed `regex` kwarg is a regex ; regex_name is 'email' if `regex='email'`
        regex_special_chars = r'^$.*+?{}[]\|()' 
        regex_name = 'regex' if any(char in regex_special_chars for char in kwargs["regex"]) else kwargs["regex"] 
        df[f'invalid_{regex_name}'] = df[new_columns].apply(lambda x: validate_regex(x), axis=1)
        
        # Replace invalid values with None
        df[new_columns] = df[new_columns].fillna('').replace({np.nan: ''}).replace({
            rf'.* \[{kwargs["tag"]}\]': None
        }, regex=True)
        if df[f'invalid_{regex_name}'].notna().any():
            df[f'invalid_{regex_name}'] = df[f'invalid_{regex_name}'].replace({
                rf' \[{kwargs["tag"]}\]': r''}, regex=True)
        else:
            debug_messages.append(f'No invalid {regex_name} values found in the DataFrame.')
        df[new_columns] = df[new_columns].replace({'': None})
    logger.debug('\n'.join(debug_messages))
    return df

def verify_regex(series, regex='email', tag='invalid', logger=None, logging_level=logging.DEBUG):
    """
    Verify and extract email addresses from a pandas series.

    Parameters:
    - series (pandas.Series): The input series containing email addresses.

    Returns:
    - pandas.Series: A new series with the extracted email addresses. If an email address is invalid, it will be marked as '[invalid]'. If an email address is empty or None, it will be marked as None.

    Example:
    >>> series = pd.Series(['john@example.com', 'invalid_email', '', None])
    >>> verify_email(series)
    0        john@example.com
    1            [invalid]
    2                   None
    3                   None
    dtype: object
    """
    logger = create_function_logger('verify_email', logger, level=logging_level)
    log_messages = []
    if regex == 'email':
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
    
    def extract_regex(string):
        if pd.isnull(string):
            return None
        match = re.search(regex, str(string))
        if match:
            return match.group()
        else:
            if len(str(string)) > 0:
                index = series[series == string].index[0]
                log_messages.append(f"Invalid email at index: {index}")
                return f'{string} [{tag}]'
            else:
                return None
    
    series = series.apply(extract_regex)
    if len(log_messages) > 0:
        logger.debug('\n'.join(log_messages))
    return series

def lookup_value(id, df, id_column, value_column):
    result = []
    if type(id) == str:
        id_list = id.split(',')
    else:
        id_list = [id]
    for id in id_list:
        value_series = df.loc[df[id_column] == int(id), value_column]
        if len(value_series) > 0:
            result.append(value_series.values[0])
    result = '; '.join(result)
    if result == '':
        result = None
    return result

# def concatenate_columns(row, columns, new_column_name, delimiter='; '):
#     row[new_column_name] = delimiter.join([row[column] for column in columns if row[column] != -1])
#     if len(row[new_column_name]) == 0:
#         row[new_column_name] = None
#     return row

def verify_email(series):
    """[use `verify_regex` instead]
    Verify and extract email addresses from a pandas series.

    Parameters:
    - series (pandas.Series): The input series containing email addresses.

    Returns:
    - pandas.Series: A new series with the extracted email addresses. If an email address is invalid, it will be marked as '[invalid]'. If an email address is empty or None, it will be marked as None.

    Example:
    >>> series = pd.Series(['john@example.com', 'invalid_email', '', None])
    >>> verify_email(series)
    0        john@example.com
    1            [invalid]
    2                   None
    3                   None
    dtype: object
    """
    email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
    
    def extract_email(email_str, logger=None, logging_level=logging.DEBUG):
        if pd.isnull(email_str):
            return None
        match = re.search(email_regex, str(email_str))
        if match:
            return match.group()
        else:
            if len(str(email_str)) > 0:
                return '[invalid]'
            else:
                return None
    
    series = series.apply(extract_email)
    return series

def clean_text(text):
    # Remove non-alphanumeric characters (except punctuation) and replace them with a space
    cleaned_text = re.sub(r'[^a-zA-Z0-9\s' + re.escape(string.punctuation) + ']', ' ', text)
    return cleaned_text