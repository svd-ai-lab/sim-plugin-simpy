# sim-plugin-simpy

Simpy driver for [sim-cli](https://github.com/svd-ai-lab/sim-cli),
distributed as an out-of-tree plugin.

SimPy driver for sim.

## Install

```bash
sim plugin install simpy
```

Other paths:

```bash
pip install git+https://github.com/svd-ai-lab/sim-plugin-simpy@v0.1.0
pip install https://github.com/svd-ai-lab/sim-plugin-simpy/releases/download/v0.1.0/sim_plugin_simpy-0.1.0-py3-none-any.whl
pip install -e .
```

After install:

```bash
sim plugin doctor simpy
sim plugin sync-skills
```

## Development

```bash
git clone https://github.com/svd-ai-lab/sim-plugin-simpy
cd sim-plugin-simpy
uv sync
uv run pytest
```

## License

Apache-2.0.
