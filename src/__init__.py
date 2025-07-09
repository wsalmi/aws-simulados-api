"""
AWS Simulados API - Main Package

This package contains the main application for the AWS practice exam simulator.
It includes models, routes, and database configuration.
"""

from .models import Question, SimulationSession, db
from .routes import user_bp, simulation_bp

__version__ = '1.0.0'
__author__ = 'AWS Simulados Team'

__all__ = [
    'Question', 
    'SimulationSession', 
    'db',
    'user_bp', 
    'simulation_bp'
]