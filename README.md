# claude-arboreto-skill

A Claude Code skill for inferring gene regulatory networks from gene-expression data with Arboreto.

## Overview

Arboreto provides scalable algorithms for inferring relationships between transcription factors and potential target genes. This skill guides the preparation of expression matrices, selection of an inference algorithm, execution of network inference, and interpretation of the resulting regulatory links.

It is intended for bulk or single-cell transcriptomics workflows where expression patterns are used to prioritize candidate regulatory relationships.

## Main Capabilities

- Prepare expression matrices for network inference.
- Select between GRNBoost2 and GENIE3 workflows.
- Supply transcription factor lists when available.
- Configure random seeds and execution parameters.
- Run inference on a local machine or distributed environment.
- Export inferred regulatory links for downstream analysis.
- Review outputs and identify limitations before drawing biological conclusions.

## Installation

Install Arboreto and its core Python dependencies:

```bash
python -m pip install arboreto pandas
```

Install the skill:

```bash
git clone https://github.com/Brajesh31/claude-arboreto-skill.git ~/.claude/skills/arboreto
```

## Input Expectations

The typical input is an expression matrix in which rows represent observations or samples and columns represent genes. Confirm the orientation and gene identifiers before running inference.

A transcription factor list can be supplied to constrain the candidate regulators. Ensure that the identifiers in the list match the expression matrix columns.

## Basic Example

```python
import pandas as pd
from arboreto.algo import grnboost2

expression = pd.read_csv("expression_data.tsv", sep="\t", index_col=0)

network = grnboost2(
    expression_data=expression,
    tf_names=list(expression.columns),
    seed=42,
)

network.to_csv("regulatory_network.tsv", sep="\t", index=False)
```

This is an illustrative starting point. Confirm the installed Arboreto version and adjust the input orientation, transcription factor list, and execution settings to match the dataset.

## Workflow

1. Inspect the expression matrix dimensions and identifiers.
2. Remove or handle unsuitable observations and genes.
3. Confirm that candidate transcription factors are represented in the matrix.
4. Choose GRNBoost2 or GENIE3 based on the analysis requirements.
5. Run inference with documented parameters.
6. Inspect the output columns and score distribution.
7. Save the network and analysis configuration.
8. Validate candidate relationships using independent biological evidence.

## Repository Contents

- `SKILL.md`: Main skill instructions and inference workflow.
- `references/`: Algorithm, inference, and distributed-computing guidance.
- `scripts/basic_grn_inference.py`: Example command-line inference workflow.

## Interpretation and Limitations

An inferred edge is a computationally prioritized relationship, not proof of direct regulation or causality. Results depend on sample size, expression quality, regulator selection, preprocessing, and algorithm settings. Treat the network as a hypothesis-generating result and validate important findings independently.

## Reproducibility Checklist

- Record the input dataset and preprocessing steps.
- Record the Arboreto and dependency versions.
- Save the regulator list and random seed.
- Keep the full output and filtering criteria.
- Document compute settings for distributed runs.
- Validate important edges before biological interpretation.
