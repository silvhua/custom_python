from tabula import read_pdf
import sys

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