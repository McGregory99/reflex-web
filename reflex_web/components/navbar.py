import reflex as rx

def navbar() -> rx.Component:
    return rx.hstack(
        rx.text(
            "GOYO CANCIO",
            as_="i",
            height="40px"
        ),
        position="sticky",
        bg="blue",
        padding_x="16px",
        padding_y="8px",
        z_index="999" #Total prioridad en el eje de la Z (profundidad), para que no sea tapada por nada
    )