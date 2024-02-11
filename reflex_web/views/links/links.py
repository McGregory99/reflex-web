import reflex as rx

from reflex_web.components.link_button import link_button

def links() -> rx.Component:
    return rx.vstack(
        link_button("PERFIL DE LINKEDIN", "https://linkedin.com/in/goyocancio"),
        link_button("CUENTA DE GITHUB", "https://github.com/McGregory99"),
        link_button("INSTAGRAM", "https://www.instagram.com/mcgregory__/"),
        link_button("WEB GOYOCANCIO.COM", "https://goyocancio.com")    
    )