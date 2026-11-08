# Distributed Computing

Arboreto uses Dask to parallelize inference. Start with the local default and introduce explicit cluster configuration only when profiling shows it is needed.

## Local cluster
```python
from distributed import Client, LocalCluster
from arboreto.algo import grnboost2

if __name__ == "__main__":
    cluster = LocalCluster(n_workers=4, threads_per_worker=1, memory_limit="4GB")
    client = Client(cluster)
    try:
        network = grnboost2(expression_data=expression, client_or_address=client, seed=777)
    finally:
        client.close()
        cluster.close()
```

Tune worker count and memory limits to the actual host. More workers can increase memory use and contention rather than improve throughput.

## Remote scheduler
Connect with a configured scheduler address using Dask's Client. Protect credentials and network access; do not expose scheduler ports publicly.

## Operational guidance
- Monitor worker memory and task failures.
- Keep input data accessible to all workers.
- Avoid creating multiple competing clusters in one process.
- Close clients and clusters in a finally block.
- Record worker count, memory limits, scheduler configuration, and runtime.

## Failure modes
Worker restarts commonly indicate memory pressure or environment mismatch. Validate package versions across workers and reduce concurrency or dataset size before increasing infrastructure.
