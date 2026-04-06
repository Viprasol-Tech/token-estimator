"""
token-estimator - Estimate tokens across programming languages

Part of Viprasol Utilities: https://viprasol.com
"""

__version__ = "0.1.0"
__author__ = "Viprasol"
__email__ = "hello@viprasol.com"

from .core import TokenEstimator, estimate, process, main

__all__ = ["TokenEstimator", "estimate", "process", "main"]
