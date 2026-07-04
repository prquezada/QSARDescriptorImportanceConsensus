"""
consensus.py

Builds a consensus table from descriptor importance scores
obtained across multiple machine learning models.
"""

import pandas as pd


def build_consensus_table(
    df: pd.DataFrame,
    descriptor_col: str,
    importance_col: str
) -> pd.DataFrame:
    """
    Compute mean importance and frequency for each descriptor.

    Parameters
    ----------
    df : pd.DataFrame
        Input dataframe containing descriptor importance values.

    descriptor_col : str
        Name of descriptor column.

    importance_col : str
        Name of importance column.

    Returns
    -------
    pd.DataFrame
        Consensus table sorted by MeanImportance.
    """

    consensus = (
        df.groupby(descriptor_col)
          .agg(
              MeanImportance=(importance_col, "mean"),
              Frequency=(importance_col, "count")
          )
          .reset_index()
          .rename(columns={
              descriptor_col: "Descriptor"
          })
          .sort_values(
              by="MeanImportance",
              ascending=False
          )
    )

    return consensus