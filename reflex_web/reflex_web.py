from rxconfig import config
import reflex as rx

from reflex_web.components.navbar import navbar
from reflex_web.components.footer import footer

from reflex_web.views.header.header import header

filename = f"{config.app_name}/{config.app_name}.py"


class State(rx.State):
    """The app state."""
    pass


def index() -> rx.Component:
    return rx.vstack(
        navbar(),
        header(),
        footer()
    )


# Create app instance and add index page.
app = rx.App()
app.add_page(index)