from rxconfig import config
import reflex as rx

from reflex_web.components.navbar import navbar
from reflex_web.components.footer import footer

from reflex_web.views.header.header import header
from reflex_web.views.links.links import links


filename = f"{config.app_name}/{config.app_name}.py"


class State(rx.State):
    """The app state."""
    pass


def index() -> rx.Component:
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                links(),
                max_width="600px",
                width="100%"
            ),
        ),
        footer(),
    )
        


# Create app instance and add index page.
app = rx.App()
app.add_page(index)