# DATA VISUALIZATION
# ----------------------------------------------------------------------------------------------------------------


# INITIATION ------------

from processes.tools.modify_cls import add_method
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import skimage as ski
import seaborn as sns
import numpy as np
import math


# EXECUTION -------------

def setup_figure(self: pd.DataFrame):
    cols_numb = self.select_dtypes(include='number')
    n_cols = math.ceil(math.sqrt(cols_numb.shape[1]))
    n_rows = math.ceil(cols_numb.shape[1]/n_cols)
    
    figure, axes = plt.subplots(
        ncols=n_cols,
        nrows=n_rows,
        dpi=100,
        figsize=(min(16, 4 * n_cols), min(16, 4 * n_rows))
    )
    axes = np.array(axes).flatten()
    
    return cols_numb, figure, axes


# Boxplots of quantitative data
@add_method(pd.DataFrame)
def boxplots(self, **kwargs):
    # Create a figure with subplots
    cols_numb, figure, axes = setup_figure(self)
    
    # Plot a boxplot for each column
    for i, col in enumerate(cols_numb):
        axes[i].boxplot(self[col], **kwargs)
        axes[i].set_title(col, fontsize=12)
        axes[i].set_xticklabels([])
        axes[i].grid(visible=True)
    
    # Remove the last empty subplot, adjust layout and title
    figure.suptitle(
        'Boxplots | Characteristics\n',
        fontsize=20,
        fontweight='bold'
    )
    figure.subplots_adjust(hspace=0.2, wspace=0.2)
    figure.tight_layout()
    
    for i in range(cols_numb.shape[1], len(axes)):
        figure.delaxes(axes[i])
    
    # Display the plot
    plt.show()


# Letter-value plots of quantitative data
@add_method(pd.DataFrame)
def boxenplots(self, color='white', color_points='black', **kwargs):
    # Create a figure with subplots
    cols_numb, figure, axes = setup_figure(self)

    # Plot a boxen plot for each column
    for i, col in enumerate(cols_numb):
        sns.boxenplot(self[col], ax=axes[i], color=color, **kwargs)
        sns.stripplot(data=self[col], size=4, pallete=f'dark:{color_points}', alpha=0.2, ax=axes[i])
        axes[i].set_title(col, fontsize=12)
        axes[i].set_ylabel('')
        axes[i].set_xticklabels([])
        axes[i].grid(visible=True)
    
    # Remove the last empty subplot, adjust layout and title
    figure.suptitle(
        'Letter-Value Plots | Courses\' Characteristics\n',
        fontsize=20,
        fontweight='bold'
    )
    figure.subplots_adjust(hspace=0.2, wspace=0.2)
    figure.tight_layout()
    
    for i in range(cols_numb.shape[1], len(axes)):
        figure.delaxes(axes[i])
    
    # Display the plot
    plt.show()


# Heatmap that represents the correlation matrix of the numeric data
@add_method(pd.DataFrame)
def corr_heatmap(self):
    # Create a square figure
    plt.figure(figsize=(8, 8))
    
    # Correlations of numerical features
    Correlations = self.corr(numeric_only=True)
    
    # Create heatmap
    sns.heatmap(
        Correlations,
        vmax=.8,
        square=True,
        annot=True,
        fmt='.2f',
        annot_kws={'size': 8 + round(24/len(self.cols_numb))}
    )
    
    # Format plot's details (title)
    plt.title('Correlation Matrix of Features Heatmap', fontdict={'fontsize': 20, 'fontweight': 'bold'})
    
    # Display the plot
    plt.show()
    

# END -------------------

if __name__ == '__main__':
    pass


# DRAFT -----------------

"""



"""
