# config.py

from pathlib import Path

# =============================
# PROJECT
# =============================

PROJECT_NAME = "Descriptor Importance Analysis"

# =============================
# MODEL
# =============================

# config.py

REGRESSION = "regression"
CLASSIFICATION = "classification"

MODELING_TYPE = REGRESSION

# =============================
# PATHS
# =============================

DATA_DIR = Path("data")

OUTPUT_DIR = Path("outputs")

FIGURES_DIR = OUTPUT_DIR / "figures"

TABLES_DIR = OUTPUT_DIR / "tables"

# =============================
# COLUMNS
# =============================

DESCRIPTOR_COLUMN = "Descriptor"

IMPORTANCE_COLUMN = "Importance"

SOURCE_COLUMN = "Source"

MODEL_COLUMN = "Model"

# =============================
# PLOTS
# =============================

TOP_N = 20