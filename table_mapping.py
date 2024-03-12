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
        df[new_column] = df[new_column].replace({sep * (len(columns) - 1): None})
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

def merge_and_validate(left_df, right_df, left_on, right_on, how='outer', indicator=True, drop_duplicates=False):
    indicator = '_merge' if indicator == True else indicator
    print(f'\nTotal rows: {left_df.shape[0] + right_df.shape[0]}')
    print(f'\tLeft DF shape: {left_df.shape}')
    print(f'\tRight DF shape: {right_df.shape}')
    common_columns = list(set(left_df.columns.tolist()).intersection(set(right_df.columns.tolist())) - set([left_on]) - set([right_on]))
    print(f'\tCommon columns: {common_columns}')
    print(f'Performing {how} merge: left on `{left_on}` and right on `{right_on}.`')
    # print(f'\tLeft DF columns: {left_df.columns}')
    merged_df = left_df.merge(
        right_df, how=how, indicator=indicator, suffixes=(None, '_y'),
        left_on=left_on, right_on=right_on
    )
    print(f'Shape after initial merge: {merged_df.shape}')
    print(f'Columns after merge: {[column for column in merged_df.columns]}')
    print(f"Merge indicator value counts: {merged_df[indicator].value_counts()}")
    print(f"\tSum: {merged_df[indicator].value_counts().sum()}")
    duplicate_rows = return_duplicate_rows(merged_df)
    if drop_duplicates:
        merged_df = merged_df.drop_duplicates(subset=[left_on, right_on], keep='first')
        # drop columns containing the '_y' indicator
        print(f'\tShape after dropping duplicates: {merged_df.shape}\n')
    else:
        print(f'\tDrop duplicates = {str(drop_duplicates)}')
    for column in common_columns:
        merged_df[column] = merged_df[column].fillna(merged_df[f'{column}_y'])
    merged_df = merged_df.drop(columns=[indicator] + [column for column in merged_df.columns if column.endswith('_y')])
    return merged_df

def one_row_per_id(
    df, id_column='kIntakeID', sep='_'
    ):
    """
    Reshape a DataFrame that has multiple rows for a given ID value so that every ID value only
    has 1 row in the DataFrame. Value columns are added based on the maximum number of 
    rows per ID in the original dataframe. 
    """
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
    sorted_columns = []
    # for group in range(1, n_groups + 1):
    for group in range(n_groups):
        for original_column in original_columns:
            sorted_columns.append(f'{original_column}{sep}{group}')
    reshaped_df = reshaped_df.reset_index()
    reshaped_df = reshaped_df[[id_column] + sorted_columns]
    print(f'Final shape: {reshaped_df.shape}')
    print(f'final columns: {[column for column in reshaped_df.columns]}')        
    return reshaped_df

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

def merge_to_replace(left_df, right_df, left_on, right_index_column, value_column):
    print(f'right index length: {len(right_df.index)}')
    print(f'right index unique values : {len(right_df.index.unique())}')
    print(f'left_df[left_on] shape {left_df[left_on].shape}')
    print(f'left_df[value_column] shape {left_df[value_column].shape}')
    try:
        if value_column in left_df.columns:
            new_value_column = f'{value_column}_y'
            right_df = right_df.rename(columns={value_column: new_value_column})
            value_column = new_value_column
        else:
            new_value_column = value_column 
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

def remove_time_from_date_string(date_string, delimiter=' '):
    if type(date_string) == str:
        date = date_string.split(delimiter)[0] if delimiter in date_string else date_string
    else:
        date = None
    return date

def map_many_to_one(row, columns, new_column, mapping_dict):
    key = '__'.join([row[col] for col in columns])
    row[new_column] = mapping_dict.get(key, None)
    # if row[new_column] == None:
    #     print(f'index {row.name} key {key} has no value')
    return row

# def concatenate_columns(row, columns, new_column_name, delimiter='; '):
#     row[new_column_name] = delimiter.join([row[column] for column in columns if row[column] != -1])
#     if len(row[new_column_name]) == 0:
#         row[new_column_name] = None
#     return row