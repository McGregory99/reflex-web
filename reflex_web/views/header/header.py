import reflex as rx

from reflex_web.views.links.links import links

def header() -> rx.Component:
    return rx.vstack(
        rx.avatar(
            name="Goyo Cancio",
            size="xl"
        ),
        rx.text("@McGregory99"),
        rx.text("Hola! MI NOMBRE ES GOYO CANCIO"),
        rx.text("""Soyingeniero en telecomunicaciones, con ms in fintech
                actualmente trabaoj en GRASP on unos satelites
                Leo muchos libros y me gusta el emprendimiento
                """)
        
    )