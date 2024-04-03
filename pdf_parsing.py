from tabula import read_pdf
import sys
import re

def parse_pdf_tolist(
    pdf_filenames, 
    filepath=r'C:\Users\silvh\OneDrive\Ginkgo\references', 
    pages='all',**kwargs
    # last_id_column='Major Heading', value_to_ignore=None,
    # blank_columns=None,
    ):
    """
    Create dataframe from a PDF file using tabula-py.

    Returns:
        A list of lists of dataframes, one item for each file. Within each nested list
        are a dataframe for each parsed pdf page.

    Created in 2024-03-12 notebook.

    Example usage:
        pdf_filenames = ['1_2024-adult-compendium_1_2024.pdf']

        dfs_list = parse_pdf_tolist(
            pdf_filenames, 
            filepath=r'C:\Users\silvh\OneDrive\Ginkgo\references', 
            pages='all',
            )
    """
    print(f'Extracting the following files:')
    if type(pdf_filenames) != list:
        pdf_filenames = [pdf_filenames]
    dfs_list = []
    reference_dict = dict()
    corrected_pages = dict()
    for index, file in enumerate(pdf_filenames):
        print(file)
        filepath = f'{filepath}/'.replace('\\','/') if filepath else ''
        path_and_file = filepath+file
        try:
            df_list = read_pdf(path_and_file, pages=pages, **kwargs)
            dfs_list.append(df_list)
        except Exception as error:
            exc_type, exc_obj, tb = sys.exc_info()
            f = tb.tb_frame
            lineno = tb.tb_lineno
            filename = f.f_code.co_filename
            message = f'An error occurred on line {lineno} in {filename}: {error}.'
            print(message)
    return dfs_list


def concat_parsed_pdfs(dfs_list):
    """
    A function that concatenates a list of DataFrames into a single DataFrame. 
    It unpacks nested lists, concatenates the DataFrames, and handles columns that do not match. 
    Returns the final concatenated DataFrame.
    """
    # Unpack the lists into a single unnested list
    if type(dfs_list[0]) != list:
        dfs_list = [dfs_list]
    unpacked_dfs_list = [item for sublist in dfs_list for item in sublist]
    print(f'Concatenating {len(unpacked_dfs_list)} dataframes...')
    page1_columns = unpacked_dfs_list[0].columns
    dfs_list = [unpacked_dfs_list[0]]
    n_rows = len(unpacked_dfs_list[0])
    print(f'\tDataframe 1 (shape: {unpacked_dfs_list[0].shape})...')
    for index, df in enumerate(unpacked_dfs_list[1:]):
        print(f'\tDataframe {index+2} (shape: {df.shape})...')
        df_columns = df.columns
        print(f'Dataframe {index+2} columns: {df_columns}')
        if page1_columns.equals(df_columns):
            pass
        elif len(page1_columns) == len(df_columns): 
            # If columns do not match, assume that the pages do not have headers and turn the dataframe into a row
            row_1_dict = {}
            for column, value in zip(page1_columns, df_columns):
                row_1_dict[column] = value
            df.columns = page1_columns
            dfs_list.append(pd.DataFrame(row_1_dict, index=[0]))
            n_rows += 1
        dfs_list.append(df)
        n_rows += len(df) 
    print(f'Total number of rows: {n_rows}')
    result_df = pd.concat(dfs_list, ignore_index=True)
    print(f'\tFinal dataframe shape: {result_df.shape}')
    return result_df

def join_2_cells_below(
        df, column_to_concat, columns_to_fill=['Major Heading', 'Activity Code', 'MET Value'], 
        fill_method='bfill'
        ):
    """
    Generate a new DataFrame by joining the values of two cells below each row in the input DataFrame.
    
    Parameters:
    df (DataFrame): The input DataFrame to process.
    column_to_concat (str): The column name to concatenate with the shifted values.
    columns_to_fill (list, optional): List of column names to fill missing values. Defaults to ['Major Heading', 'Activity Code', 'MET Value'].
    fill_method (str, optional): The method to use for filling missing values. Defaults to 'bfill'.
    
    Returns:
    DataFrame: A new DataFrame with the specified transformations applied.
    """
    df = df.copy()
    df['shifted'] = df[column_to_concat].shift(-2)
    rows_to_fix_filter = df['Major Heading'].isna()
    df.loc[rows_to_fix_filter, f'{column_to_concat} fixed'] = df[rows_to_fix_filter]['Activity Description'] + ' ' + df[rows_to_fix_filter]['shifted']
    df['Check Parsing'] = df[f'{column_to_concat} fixed'].notna()
    df[f'{column_to_concat} fixed'].fillna(df[column_to_concat], inplace=True)
    df[f'{column_to_concat} fixed'].fillna(method=fill_method, inplace=True)
    df.drop_duplicates(
        subset=f'{column_to_concat} fixed', keep='first', inplace=True
        )
    df.drop(columns=[column_to_concat, 'shifted'], inplace=True)
    df.rename(columns={f'{column_to_concat} fixed': column_to_concat}, inplace=True)
    df[columns_to_fill] = df[columns_to_fill].fillna(method=fill_method)
    df.drop_duplicates(
        subset=columns_to_fill, keep='first', inplace=True
        )
    return df

def convert_dict_keys_to_regex(dictionary):
    new_dict = {}
    for key, value in dictionary.items():
        new_key = re.compile(rf'(?i)^.*?{key}.*?$')
        new_dict[new_key] = value
    return new_dict

def simplify_strings(
        df, mapping_dict, original_column='Activity Description', new_column='Simplified Name', regex=True):
    if regex == True:
        mapping_dict = convert_dict_keys_to_regex(mapping_dict)
    df[new_column] = df[original_column].replace(
        mapping_dict, regex=regex,
        )
    return df
