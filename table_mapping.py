import sys
sys.path.append(r"C:\Users\silvh\OneDrive\lighthouse\custom_python")
from silvhua import *
from wrangling import *
import numpy as np

def merge_and_validate(left_df, right_df, left_on, right_on, how='outer', indicator=True, drop_duplicates=False):
    indicator = '_merge' if indicator == True else indicator
    print(f'Total rows: {left_df.shape[0] + right_df.shape[0]}')
    print(f'\tLeft DF shape: {left_df.shape}')
    print(f'\tRight DF shape: {right_df.shape}')
    common_columns = list(set(left_df.columns.tolist()).intersection(set(right_df.columns.tolist())) - set([left_on]) - set([right_on]))
    print(f'\tCommon columns: {common_columns}')
    # print(f'\tLeft DF columns: {left_df.columns}')
    merged_df = left_df.merge(
        right_df, how=how, indicator=indicator, suffixes=(None, '_y'),
        left_on=left_on, right_on=right_on
    )
    print(f'Shape after initial merge: {merged_df.shape}')
    print(f'Columns after merge: {[column for column in merged_df.columns]}')
    print(f"Merge indicator value counts: {merged_df[indicator].value_counts()}")
    print(f"\tSum: {merged_df[indicator].value_counts().sum()}")
    if drop_duplicates:
        merged_df = merged_df.drop_duplicates(subset=[left_on, right_on], keep='first')
        # drop columns containing the '_y' indicator
        print(f'Shape after dropping duplicates: {merged_df.shape}\n')
    else:
        print(f'Drop duplicates = {str(drop_duplicates)}')
    for column in common_columns:
        merged_df[column] = merged_df[column].fillna(merged_df[f'{column}_y'])
    merged_df = merged_df.drop(columns=[indicator] + [column for column in merged_df.columns if column.endswith('_y')])
    return merged_df

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
    try:
        if value_column in left_df.columns:
            new_value_column = f'{value_column}_y'
            right_df = right_df.rename(columns={value_column: new_value_column})
            value_column = new_value_column
        else:
            new_value_column = value_column 
        print(f'Before `merge_to_replace`: \n\tColumns:{[col for col in left_df.columns]}')
        print(f'\tLeft DataFrame shape: {left_df.shape}')
        right_df = right_df.copy().set_index(right_index_column)
        col_to_fill = left_on if type(left_on) == str else left_on[0] 
        print(f'col_to_fill: {col_to_fill}')
        # In case there are duplicate values in any of the merge columns, merge the dataframes, then 
        # drop the extra column.
        left_df = left_df.merge(
                right_df[value_column], how='left', left_on=left_on, right_index=True
            )
        left_df[left_on] = left_df[value_column]
        left_df = left_df.drop(columns=[value_column])
        print(f'After `merge_to_replace`: \n\tColumns: {[col for col in left_df.columns]}')
        print(f'\tLeft DataFrame shape: {left_df.shape}')
    except Exception as error:
        print(f'right index length: {len(right_df.index)}')
        print(f'right index unique values : {len(right_df.index.unique())}')
        print(f'left_df[left_on] shape {left_df[left_on].shape}')
        print(f'left_df[value_column] shape {left_df[value_column].shape}')
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

def concatenate_columns(row, columns, new_column_name, delimiter='; '):
    row[new_column_name] = delimiter.join([row[column] for column in columns if row[column] != -1])
    if len(row[new_column_name]) == 0:
        row[new_column_name] = None
    return row

def map_many_to_one(row, columns, new_column, mapping_dict):
    key = '__'.join([row[col] for col in columns])
    row[new_column] = mapping_dict.get(key, None)
    # if row[new_column] == None:
    #     print(f'index {row.name} key {key} has no value')
    return row