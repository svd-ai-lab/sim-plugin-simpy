"""Simpy driver plugin for sim-cli.

Distributed as an out-of-tree plugin; discovered by sim-cli via the
``sim.drivers`` entry-point group. Bundled skill files (under
``_skills/``) are exposed via the ``sim.skills`` entry-point group, and
lightweight metadata via ``sim.plugins``.
"""
from importlib.resources import files

from .driver import SimpyDriver

skills_dir = files(__name__) / "_skills"

plugin_info = {
    "name": "simpy",
    "summary": "SimPy driver for sim.",
    "homepage": "https://github.com/svd-ai-lab/sim-plugin-simpy",
    "license_class": "oss",
    "solver_name": "Simpy",
}

__all__ = ["SimpyDriver", "skills_dir", "plugin_info"]
