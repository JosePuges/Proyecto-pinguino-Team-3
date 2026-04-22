from palmerpenguins import load_penguins
import seaborn as sns
import matplotlib.pyplot as plt


def cargar_dataset_penguins():
    sns.set_theme(style="whitegrid")
    plt.rcParams["figure.figsize"] = (10, 5)
    return load_penguins()
