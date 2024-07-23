import reflex as rx
from Jorge_Portfolio.templates import template
import Jorge_Portfolio.components.link_button as lb


@template(route="/contact", title="Contacto")
def contact() -> rx.Component:
    return rx.vstack(
        rx.heading("Puedes contactar conmigo", size="8"),
        lb.link_button(
            "Linkedin", "linkedin", "https://www.linkedin.com/in/jorge-gimenez-lopez"
        ),
        lb.link_button("Github", "github", "https://github.com/jrgim"),
        # lb.link_button("Email", "mail", "mailto:jorge.gimenezlopez@gmail.com"),
        lb.link_button("Email", "mail", "mailto:alu.139992@usj.es"),
    )
