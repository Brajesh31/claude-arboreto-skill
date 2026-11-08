# Algorithm Selection: GRNBoost2 and GENIE3

## GRNBoost2
GRNBoost2 uses gradient-boosted regression trees to estimate how candidate transcription factors predict each target gene. It is generally the faster default for larger expression matrices.

Choose it when throughput matters and you need a ranked candidate network for downstream analysis.

## GENIE3
GENIE3 uses tree-based ensemble regression and is useful as a comparison method or when reproducing workflows built around the original GENIE3 approach. It can be slower and resource-intensive on large matrices.

## Shared design decisions
1. Define the candidate TF set from a curated source appropriate to the organism.
2. Decide whether self-regulation should be retained or filtered.
3. Set and record a random seed.
4. Compare stability across seeds or resampled observations.
5. Filter edges using a documented strategy, such as top-k regulators per target or a score threshold selected for the dataset.

## Interpretation cautions
Importance scores are model-derived feature rankings. They do not establish directionality, direct binding, statistical significance, or causality. Validate candidate edges with perturbation, motif, ChIP, or other independent evidence.

## Reporting checklist
- Organism and gene identifier namespace
- Expression preprocessing and normalization
- Number of observations, genes, and candidate TFs
- Algorithm and parameters
- Random seed and software versions
- Edge filtering and validation method
