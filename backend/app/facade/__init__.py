"""
Facade Layer

This layer contains the application's business logic facades.
Each facade represents a single business operation and orchestrates
the necessary services and repositories to complete it.
"""

from app.facade.auth import AuthFacade

__all__ = ["AuthFacade"]

