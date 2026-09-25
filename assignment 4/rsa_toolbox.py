import numpy as np
from scipy.stats import spearmanr


def compute_rdm(patterns, metric="euclidean"):
    n_classes = patterns.shape[0]
    rdm = np.zeros((n_classes, n_classes))

    if metric == "euclidean":
        for i in range(n_classes):
            differences = patterns - patterns[i]
            rdm[i] = np.sqrt(np.sum(differences ** 2, axis=1))

    elif metric == "correlation":
        rdm = 1 - np.corrcoef(patterns)

    np.fill_diagonal(rdm, 0)
    return rdm


def upper_triangle(rdm):
    indices = np.triu_indices(rdm.shape[0], k=1)
    return rdm[indices]


def compare_rdms(rdm_a, rdm_b, method="pearson"):
    distances_a = upper_triangle(rdm_a)
    distances_b = upper_triangle(rdm_b)

    if method == "pearson":
        return np.corrcoef(distances_a, distances_b)[0, 1]

    elif method == "spearman":
        return spearmanr(distances_a, distances_b)[0]


def compare_to_many(reference_rdm, candidate_rdms, method="pearson"):
    scores = []

    for index, candidate in enumerate(candidate_rdms):
        score = compare_rdms(reference_rdm, candidate, method=method)
        scores.append((index, score))

    return sorted(scores, key=lambda item: item[1], reverse=True)

    
def plot_rdm(rdm, ax, title="", labels=None, vmax=None, annotate=False):
    """Plot an RDM on the supplied axes."""
    image = ax.imshow(rdm, cmap="viridis", vmin=0, vmax=vmax)

    if labels is not None:
        ax.set_xticks(range(len(labels)), labels=labels)
        ax.set_yticks(range(len(labels)), labels=labels)

    ax.set_title(title)
    ax.set_xlabel("Stimulus")
    ax.set_ylabel("Stimulus")

    if annotate:
        upper_limit = image.get_clim()[1]

        for i in range(rdm.shape[0]):
            for j in range(rdm.shape[1]):
                ax.text(
                    j, i, f"{rdm[i, j]:.2f}",
                    ha="center",
                    va="center",
                    color="white" if rdm[i, j] < upper_limit / 2 else "black",
                )

    return image