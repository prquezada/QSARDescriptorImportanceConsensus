from pathlib import Path

import pandas as pd

from src.consensus import build_consensus_table

# ----------------------------
# Paths
# ----------------------------

DATA = Path("data/descriptor_importance.csv")
OUTPUT = Path("outputs/tables")

OUTPUT.mkdir(parents=True, exist_ok=True)

# ----------------------------
# Load data
# ----------------------------

df = pd.read_csv(DATA)

# ----------------------------
# Build consensus
# ----------------------------

consensus = build_consensus_table(
    df=df,
    descriptor_col="Descriptor",
    importance_col="Importance"
)

# ----------------------------
# Save
# ----------------------------

consensus.to_csv(
    OUTPUT / "descriptor_consensus.csv",
    index=False
)

print(consensus.head(20))