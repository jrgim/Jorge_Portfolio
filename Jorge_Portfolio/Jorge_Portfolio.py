"""Welcome to Reflex!."""

# Import all the pages.
from Jorge_Portfolio.pages import *
from Jorge_Portfolio.pages.contact import contact
import reflex as rx


class State(rx.State):
    """Define empty state to allow access to rx.State.router."""


# Create the app.
app = rx.App()