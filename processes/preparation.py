# DATA PREPARATION
# ----------------------------------------------------------------------------------------------------------------


# INITIATION ------------

from processes.tools.modify_cls import add_method
import pandas as pd
import warnings
import re
warnings.simplefilter(action='ignore', category=UserWarning)


# EXECUTION -------------a

# General-purpose method to import dataset as dataframe
@add_method(pd)
def read(fileName: str, default=True, **kwargs):
    extension = fileName[fileName.rfind('.')+1:]
    funcs = {
        'csv': pd.read_csv,
        'xlsx': pd.read_excel,
        'sav': pd.read_spss,
        'dta': pd.read_stata,
        'XPT': pd.read_sas, 'sas7bdat': pd.read_sas,
        'xml': pd.read_xml,
        'pkl': pd.read_pickle,
        'json': pd.read_json
    }
    
    if extension not in funcs or not default:
        data = pd.read_table(fileName, **kwargs)
    
    else:
        data = funcs[extension](fileName, **kwargs)
        
    # Flag to indicate dataset has not been processed
    data.isRaw = True
    
    data.update_cols()
    
    return data
    

# Format indices & rearrange the rows
@add_method(pd.DataFrame)
def reorder_rows(self):
    self.index.name = 'ID'
    self.sort_index(inplace=True)
    
    return


# Format columns' titles
@add_method(pd.DataFrame)
def format_titles(self, columns=None):
    if columns is None:
        columns = {}
        
    self.columns = self.columns.map(lambda name: ' '.join(
        map(lambda word: word.title(), name.split('_'))))
    self.rename(columns=columns, inplace=True)
    
    self.update_cols()
    
    return


@add_method(pd.DataFrame)
def recap(self, n_rows=10, show_title=True, title=None):
    # Update types of columns
    self.update_cols()
    
    # Show title
    # if show_title:
    #     if title is None:
    #         title = f"{self=}".split('=')[0]
    #         print(title)
    #         print(separate_underscores(title))
    #         title = ' '.join(separate_camel_case(w) for w in separate_underscores(title))
    #         print(title)
    #     print(title.upper())
    
    # Number of observations and features
    print(f"Number of Observations: {self.shape[0]}; \n"
          f"Number of Features: {self.shape[1]}.")
    
    print(f"- Categorical features: {', '.join(map(str, self.cols_name))}; \n"
          f"- Numerical features: {', '.join(map(str, self.cols_numb))}.")
    
    return self.head(n_rows)


@add_method(pd.DataFrame)
def update_cols(self):
    # List of the names of columns with qualitative data
    self.cols_name = self.select_dtypes(include='object').columns.tolist()
    # List of the names of columns with quantitative data
    self.cols_numb = self.select_dtypes(include='number').columns.tolist()
    
    return


# Function that separates CamelCase words
def separate_camel_case(word):
    return ' '.join(re.findall(r'[A-Z]?(?:[a-z]+|[A-Z]*(?=[A-Z]|$))', word))


# Function that separates underscore words
def separate_underscores(word):
    word = word.split('_')
    word.reverse()
    
    return word


# END -------------------

if __name__ == '__main__':
    pass


# DRAFT -----------------

"""



"""
