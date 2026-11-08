# Basic GRN Inference

## Input contract
Arboreto expects a numeric expression matrix with observations in rows and genes in columns. Column names must be unique gene identifiers. Remove metadata columns before inference, handle missing values explicitly, and avoid mixing identifier columns with measurements.

## Minimal workflow
```python
import pandas as pd
from arboreto.algo import grnboost2

if __name__ == "__main__":
    expression = pd.read_csv("expression_data.tsv", sep="\t", index_col=0)
    expression = expression.apply(pd.to_numeric, errors="raise")
    network = grnboost2(expression_data=expression, seed=777)
    network.to_csv("network.tsv", sep="\t", index=False)
```

## Quality checks
- Confirm rows are samples/cells and columns are genes.
- Remove genes with all-zero or near-constant expression.
- Check duplicate gene symbols and missing values.
- Restrict candidate regulators with a validated TF list when appropriate.
- Record input dimensions, filtering rules, algorithm, seed, and package versions.

## Output
The result contains regulator, target, and importance information. Treat importance as a ranking score, not a causal effect size or p-value. Use independent biological evidence and downstream validation before interpreting an edge as regulation.

## Troubleshooting
- Empty output: inspect matrix orientation, TF identifiers, and filtering.
- Memory pressure: reduce low-information genes or process a justified subset.
- Dask multiprocessing errors: protect entry-point code with `if __name__ == "__main__":`.
