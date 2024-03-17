import sys
sys.path.append(r"C:\Users\silvh\OneDrive\lighthouse\custom_python")
from silvhua import *
from wrangling import *
import numpy as np

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
        logger, left_df, right_df, left_on, right_on, how='outer', indicator=True, drop_duplicates=False,
        nan_fill=None, left_df_name='left', right_df_name='right', drop_indictor_column=False
        ):
    if nan_fill:
        left_df[left_on] = left_df[left_on].replace({np.nan: nan_fill})
    indicator = '_merge' if indicator == True else indicator
    logger.debug(f'\n****`merge_and_validate`****: Total rows: {left_df.shape[0] + right_df.shape[0]}')
    logger.debug(f'\tLeft DF shape: {left_df.shape}')
    logger.debug(f'\tRight DF shape: {right_df.shape}')
    common_columns = list(set(left_df.columns.tolist()).intersection(set(right_df.columns.tolist())) - set([left_on]) - set([right_on])
    logger.debug(f'\tCommon columns: {common_columns}')
    logger.debug(f'Performing {how} merge: left on `{left_on}` and right on `{right_on}.')
    
    merged_df = left_df.merge(
        right_df, how=how, indicator=indicator, suffixes=(None, '_y'),
        left_on=left_on, right_on=right_on
    )
    logger.debug(f'Shape after initial merge: {merged_df.shape}')
    logger.debug(f'Columns after merge: {[column for column in merged_df.columns]}')
    logger.debug(f"Merge indicator value counts: {merged_df[indicator].value_counts()}")
    
    merged_df[indicator] = merged_df[indicator].replace({
        'left_only': left_df_name, 'right_only': right_df_name, 
        'both': f'{left_df_name}, {right_df_name}'
    })
    
    logger.debug(f"\tSum: {merged_df[indicator].value_counts().sum()}")
    
    duplicate_rows = return_duplicate_rows(merged_df)
    if drop_duplicates:
        merged_df = merged_df.drop_duplicates(subset=[left_on, right_on], keep='first')
        logger.debug(f'\tShape after dropping duplicates: {merged_df.shape}\n')
    else:
        logger.debug(f'\tDrop duplicates = {str(drop_duplicates)}')
    
    for column in common_columns:
        merged_df[column] = merged_df[column].fillna(merged_df[f'{column}_y'])
    
    columns_to_drop = [column for column in merged_df.columns if column.endswith('_y')]
    if drop_indictor_column:
        columns_to_drop.append(indicator)
    
    merged_df = merged_df.drop(columns=columns_to_drop)
    
    return merged_df

def merge_to_replace(left_df, right_df, left_on, right_index_column, value_column, nan_fill=None):
    if nan_fill:
        left_df[left_on] = left_df[left_on].replace({np.nan: nan_fill})
    print(f'\n****`merge_to_replace`****: \nright index length: {len(right_df.index)}')
    print(f'right index unique values : {len(right_df.index.unique())}')
    print(f'left_df[left_on] shape {left_df[left_on].shape}')
    try:
        if value_column in left_df.columns:
            new_value_column = f'{value_column}_y'
            right_df = right_df.rename(columns={value_column: new_value_column})
            value_column = new_value_column
        else:
            new_value_column = value_column 
        print(f'right_df[value_column] shape {right_df[new_value_column].shape}')
        print(f'\nBefore `merge_to_replace`: \n\tColumns:{[col for col in left_df.columns]}')
        print(f'\tLeft DataFrame shape: {left_df.shape}')
        right_df = right_df.copy().set_index(right_index_column)
        column_to_fill = left_on if type(left_on) == str else left_on[-1] 
        print(f'column_to_fill: {column_to_fill}')
        # In case there are duplicate values in any of the merge columns, merge the dataframes, then 
        # drop the extra column.
        left_df = left_df.merge(
                right_df[value_column], how='left', left_on=left_on, right_index=True,
                indicator=True
            )
        left_df[column_to_fill] = left_df[value_column]
        print(f"Merge indicator value counts: {left_df['_merge'].value_counts()}\n")
        left_df = left_df.drop(columns=[value_column, '_merge'])
        print(f'After `merge_to_replace`: \n\tColumns: {[col for col in left_df.columns]}')
        print(f'\tLeft DataFrame shape: {left_df.shape}')
        duplicate_rows = return_duplicate_rows(left_df)
    except Exception as error:
        exc_type, exc_obj, tb = sys.exc_info()
        f = tb.tb_frame
        lineno = tb.tb_lineno
        filename = f.f_code.co_filename
        message = f'An error occurred on line {lineno} in {filename}: {error}.'
        print(message)
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

def concatenate_df(dfs_list, axis=0, renaming_dict={}):
    print(f'Concatenating {len(dfs_list)} DataFrames...')
    print(f'\tRenaming dict: {renaming_dict}')
    print(f'\tDataFrame shapes: {dfs_list[0].shape}, {dfs_list[1].shape}')
    if (len(renaming_dict) > 0) & (axis==0):
        for df in dfs_list:
            df = df.rename(columns=renaming_dict)
    different_columns  = compare_iterables(dfs_list[0].columns,dfs_list[1].columns, print_common=1)
    concatenated_df = pd.concat(dfs_list, axis=axis)
    print(f'\tShape after concatenation: {concatenated_df.shape}')
    return concatenated_df

def melt_dfs(dfs_list, id_vars, value_vars, var_name, value_name, date_columns, renaming_dict=None, **kwargs):
    concatenated_df = concatenate_df(dfs_list, axis=0, renaming_dict=renaming_dict)
    for column in date_columns:
        concatenated_df[column] = concatenated_df[column].apply(lambda x: remove_time_from_date_string(x))
    melted_df = pd.melt(
        concatenated_df, 
        id_vars=id_vars, value_vars=value_vars, var_name=var_name, value_name=value_name, 
        **kwargs)
    print(f'Shape of melted dataframe: {melted_df.shape}')
    return melted_df

# def concatenate_columns(row, columns, new_column_name, delimiter='; '):
#     row[new_column_name] = delimiter.join([row[column] for column in columns if row[column] != -1])
#     if len(row[new_column_name]) == 0:
#         row[new_column_name] = None
#     return row