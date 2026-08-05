import logging
from Custom_Logger import *

class CompareIterables:
    def __init__(self, iterable1, iterable2, print_common=False, print_difference=True, logger=None, logging_level=logging.DEBUG):
        """
        Initialize with two iterables and optional logging/printing options.
        Calculates and stores different_values and common_values.
        """
        self.iterable1 = iterable1
        self.iterable2 = iterable2
        self.print_common = print_common
        self.print_difference = print_difference
        self.logger = create_function_logger('compare_iterables', logger, level=logging_level)
        self.logging_level = logging_level
        self.common_values = set(iterable1) & set(iterable2)
        
        self.difference_1_2 = list(set(iterable1) - set(iterable2))
        self.difference_2_1 = list(set(iterable2) - set(iterable1))
        self._log_results()

    def _log_results(self):
        info_message = '***`compare_iterables`***: \n'
        debug_message = ''
        debug_message += f'Proper subset = {self.iterable1 < self.iterable2} \n'
        debug_message = f'\tOpposite set subtraction ({len(self.difference_2_1)} values): {self.difference_2_1}\n'
        debug_message += f'Unique values in iterable 1: {len(set(self.iterable1))}\n'
        debug_message += f'Unique values in iterable 2: {len(set(self.iterable2))}\n'
        info_message += f'Number of common values between iterables 1 and 2: {len(self.common_values)}\n'
        info_message += f'Number of different values between iterables 1 and 2: {len(self.difference_1_2)}\n'
        info_message += f'Number of different values between iterables 2 and 1: {len(self.difference_2_1)}\n'
        if (self.logger.console_handler.level <=10) | (self.print_common == True):
            info_message += f'Values in common: {self.common_values} \n'
        else:
            debug_message +=  f'Values in common: {self.common_values} \n'
        if (self.logger.console_handler.level <=10) | (self.print_difference == True):
            info_message += f'Different values: {self.difference_1_2} \n'
        else:
            debug_message += f'Different values: {self.difference_1_2} \n'
        self.logger.info(info_message)
        self.logger.debug(debug_message)

    def get_results(self):
        """
        Return different_values and common_values.
        """
        return self.difference_1_2, self.common_values

    def find_unique_df_ids(self, df1, df1_column, df2, df2_column, **kwargs):
        """
        Print the number of common values and unique values between two DataFrame columns.
        Returns:
            - different_values (list)
            - common_values (list)
        """
        comp = CompareIterables(df1[df1_column].values, df2[df2_column], **kwargs)
        return comp.different_values, comp.common_values

    def compare_df_columns(self, df1, df1_column, df2, df2_column, print_common=False, print_difference=True, logger=None, logging_level=logging.DEBUG):
        """
        Print the number of common values and unique values between two dataframe columns.
        Return the unique rows of the dataframe with more records.
        """
        logger = create_function_logger('compare_iterables', logger, level=logging_level)
        df1_values = df1[df1_column].values
        df2_values = df2[df2_column].values
        comp = CompareIterables(
            df1[df1_column].values, df2[df2_column],
            print_common=print_common, print_difference=print_difference,
            logger=logger, logging_level=logging_level
        )
        different_values = comp.different_values
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