import sys
sys.path.append(r"C:\Users\silvh\OneDrive\lighthouse\custom_python")
from silvhua import *
from wrangling import *
import numpy as np
from Custom_Logger import *

def concat_columns(df, columns, new_column, sep='; ', drop_columns=False):
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
        nan_fill=None, left_df_name='left', right_df_name='right', drop_indictor_column=False,
        logger=None
        ):
    logger = create_function_logger('merge_and_validate', logger)
    if nan_fill:
        left_df[left_on] = left_df[left_on].replace({np.nan: nan_fill})
    indicator = '_merge' if indicator == True else indicator
    merge_integer = 1
    while indicator in left_df.columns:
        merge_integer +=1
        indicator = f'{indicator}{merge_integer}'
        logger.info(f'`Using `{indicator}` as indicator column')
    logger.info(f'\n****`merge_and_validate`****: Total rows: {left_df.shape[0] + right_df.shape[0]}')
    common_columns = list(set(left_df.columns.tolist()).intersection(set(right_df.columns.tolist())) - set([left_on]) - set([right_on]))
    logger.debug(f'\tLeft DF shape: {left_df.shape}\n\tRight DF shape: {right_df.shape}\n\tCommon columns: {common_columns}')
    logger.info(f'Performing {how} merge: left on `{left_on}` and right on `{right_on}.')
    
    merged_df = left_df.merge(
        right_df, how=how, indicator=indicator, suffixes=(None, '_y'),
        left_on=left_on, right_on=right_on
    )
    merge_info_message = ''
    merge_info_message += f'Shape after initial merge: {merged_df.shape}\n'
    logger.debug(f'Columns after merge: {[column for column in merged_df.columns]}')

    merge_info_message += f"Merge indicator value counts: {merged_df[indicator].value_counts()}\n"
    
    merged_df[indicator] = merged_df[indicator].replace({
        'left_only': left_df_name, 'right_only': right_df_name, 
        'both': f'{left_df_name}, {right_df_name}'
    })
    
    merge_info_message += f"\tSum: {merged_df[indicator].value_counts().sum()}\n"
    
    duplicate_rows = return_duplicate_rows(merged_df)
    if drop_duplicates:
        merged_df = merged_df.drop_duplicates(subset=[left_on, right_on], keep='first')
        merge_info_message += f'\tShape after dropping duplicates: {merged_df.shape}\n'
    else:
        merge_info_message += f'\tDrop duplicates = {str(drop_duplicates)}\n'
    
    for column in common_columns:
        merged_df[column] = merged_df[column].fillna(merged_df[f'{column}_y'])
    logger.info(merge_info_message)
    
    columns_to_drop = [column for column in merged_df.columns if column.endswith('_y')]
    if drop_indictor_column:
        columns_to_drop.append(indicator)
    
    merged_df = merged_df.drop(columns=columns_to_drop)
    
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
    return concatenated_df

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
            **kwargs)    
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
    info_messages = []
    debug_messages = []
    logger.info(f'\n****`merge_to_replace`****: \nright index length: {len(right_df.index)}')
    logger.info(f'Merging on: \n\tLeft: {left_on}\n\tRight: {right_index_column}')
    debug_messages.append(f'right index unique values : {len(right_df.index.unique())}')
    
    debug_messages.append(f'left_df[left_on] shape {left_df[left_on].shape}')
    indicator = '_merge'
    merge_integer = 1
    while indicator in left_df.columns:
        merge_integer +=1
        indicator = f'{indicator}{merge_integer}'
        logger.info(f'`Using `{indicator}` as indicator column')
        
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
        logger.debug('\n'.join(debug_messages))
        right_df = right_df.copy().set_index(right_index_column)
        column_to_fill = left_on if type(left_on) == str else left_on[-1] 
        logger.info(f'column_to_fill: {column_to_fill}')
        logger.info(f'Value column: {value_column}')
        # In case there are duplicate values in any of the merge columns, merge the dataframes, then 
        # drop the extra column.
        logger.debug(f'Null values in right DF {value_column}: {right_df[value_column].isna().sum()}')
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
        logger.debug(f'After `merge_to_replace`: \n\tColumns: {[col for col in left_df.columns]}')
        info_messages.append(f'\tLeft DataFrame shape: {left_df.shape}')
        logger.info('\n'.join(info_messages))
        duplicate_rows = return_duplicate_rows(left_df)
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