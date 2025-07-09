"""
Routes package for AWS Simulados API.

This package contains all route blueprints and related functionality.
"""

from .user import user_bp
from .simulation import simulation_bp

__all__ = ['user_bp', 'simulation_bp']
