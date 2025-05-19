from sqlmodel import Session

"""
Provide a SQLModel session for database operations.

This function yields a session connected to the database using the
configured engine. It ensures that the session is properly closed
after use.

Yields:
    Session: A SQLModel session object for executing database queries.
"""
def get_session():
    from ..utils import engine
    with Session(engine) as session:
        yield session