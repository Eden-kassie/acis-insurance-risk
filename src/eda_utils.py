import seaborn as sns
import matplotlib.pyplot as plt

def correlation_heatmap(df, save_path=None):
    corr = df.corr(numeric_only=True)
    plt.figure(figsize=(10,8))
    sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
    plt.title("Correlation Heatmap")

    if save_path:
        plt.savefig(save_path, dpi=200)
    plt.show()
