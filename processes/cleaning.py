# DATA CLEANING
# ----------------------------------------------------------------------------------------------------------------


# INITIATION ------------

from processes.tools.modify_cls import add_method
import pandas as pd


# EXECUTION -------------

@add_method(pd.DataFrame)
def has_nan(self, verbose=True):
    # Analyze possible invalid self
    rows_NaN = self.isnull().any(axis=1)
    
    if rows_NaN.any():  # check if any observations have unrepresentable values
        if verbose:
            print('Invalid observations:\n', self[rows_NaN])
        return True
    
    else:
        if verbose:
            print('Invalid values not found.')
        return False


@add_method(pd.DataFrame)
def has_na(self, verbose=True):
    # Analyze possible missing data
    rows_NA = self.isna().any(axis=1)
    
    if rows_NA.any():  # check if any observations have missing values
        if verbose:
            print('Observations with missing values:\n', self[rows_NA])
    
    else:
        if verbose:
            print('Missing values not found.')
        return False


# Investigate duplicated values
@add_method(pd.DataFrame)
def has_duplicates(self, colName, rm=False, verbose=True):
    col = self.index if colName == 'index' else self[colName]
    vals_unique = col.unique()
    vals_duplicated = col[col.duplicated()]

    if vals_unique.size != self.shape[0]:
        if verbose:
            print(f'Duplicates in {colName.capitalize()} found.')
            print(f'- No. Unique Values:', vals_unique.size)
            print(f'- Duplicated Values:', ', '.join(vals_duplicated))
        if rm:
            if colName == 'index':
                self.drop_duplicates(inplace=True)
            else:
                self.drop_duplicates(subset=colName, inplace=True)
            if verbose:
                print('\n# Column no longer contains duplicated values.')
        return True

    else:
        if verbose:
            print('Duplicated IDs not found.')
        return False
    

# END -------------------

if __name__ == '__main__':
    pass


# DRAFT -----------------

"""



"""
