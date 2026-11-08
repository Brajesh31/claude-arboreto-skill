#!/usr/bin/env python3
"""Run reproducible Arboreto GRN inference from a TSV expression matrix."""

import argparse
from pathlib import Path

import pandas as pd
from arboreto.algo import grnboost2, genie3


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="TSV expression matrix; rows are samples/cells, columns are genes")
    parser.add_argument("output", type=Path, help="Output TSV path")
    parser.add_argument("--tf-file", type=Path, help="Optional newline-delimited transcription-factor names")
    parser.add_argument("--algorithm", choices=("grnboost2", "genie3"), default="grnboost2")
    parser.add_argument("--seed", type=int, default=777)
    return parser.parse_args()


def main():
    args = parse_args()
    if not args.input.is_file():
        raise SystemExit(f"Input file not found: {args.input}")

    expression = pd.read_csv(args.input, sep="\t", index_col=0)
    if expression.empty or expression.shape[1] < 2:
        raise SystemExit("Expression matrix is empty or has fewer than two gene columns.")
    expression = expression.apply(pd.to_numeric, errors="raise")
    if expression.isna().any().any():
        raise SystemExit("Expression matrix contains missing values. Clean them before inference.")

    tf_names = None
    if args.tf_file:
        if not args.tf_file.is_file():
            raise SystemExit(f"TF file not found: {args.tf_file}")
        tf_names = [line.strip() for line in args.tf_file.read_text().splitlines() if line.strip()]
        if not tf_names:
            raise SystemExit("TF file contains no names.")

    algorithm = grnboost2 if args.algorithm == "grnboost2" else genie3
    network = algorithm(expression_data=expression, tf_names=tf_names, seed=args.seed)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    network.to_csv(args.output, sep="\t", index=False)
    print(f"Wrote {len(network)} regulatory links to {args.output}")


if __name__ == "__main__":
    main()
