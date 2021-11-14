import numpy as np
from ipywidgets import interact, fixed
from PIL import Image
import matplotlib.pyplot as plt


def imshow(X, resize=None):
    """
    You should create a way to resize an image from an array X.
    The use of widgets is optional but you can take a look to interact.
    We should be able to install this package in Google Colab from your Git repo.
    """
    number_rows = len(X)  # source number of rows
    number_columns = len(X[0])  # source number of columns
    res = [[X[int(number_rows * r / resize[0])][int(number_columns * c / resize[1])]
            for c in range(resize[1])] for r in range(resize[0])]
    plt.imshow(res)

    pass
