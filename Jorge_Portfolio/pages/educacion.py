import reflex as rx
from Jorge_Portfolio.templates import template
from Jorge_Portfolio.components.skill_progress import skill_progress


@template(route="/educacion", title="Educación")
def educacion() -> rx.Component:
    return rx.vstack(
        rx.heading("Formación", value="1"),
        rx.vstack(
            rx.card(
                rx.heading("ESO y Bachillerato de ciencias", size="4"),
                rx.heading("El Pilar Maristas", size="4"),
                rx.heading("2016 - 2022", size="4"),
            ),
            rx.card(
                rx.heading("Ingeniería Informática", size="4"),
                rx.heading("Universidad San Jorge", size="4"),
                rx.heading("2022 - Actualidad", size="4"),
            ),
            width="100%",
        ),
        rx.heading("Skills", value="1"),
        rx.flex(
            skill_progress("HTML", 50, "/html.svg"),
            skill_progress("Java", 50, "/java.svg"),
            skill_progress("Python", 50, "/python.svg"),
            skill_progress("Docker", 50, "/docker.svg"),
            skill_progress("C", 50, "/c.png"),
            skill_progress("C++", 50, "/cpp.png"),
            skill_progress("SQL", 50, "/sql.png"),
            flex_wrap="wrap",
        ),
        rx.heading("Cursos - Meritos", value="1"),
        rx.flex(
            rx.card(
                rx.heading("2022  -  3º premio en la Olimpiada Informática de Aragón", size="4"),
            ),
        ),
        # Añade más habilidades según sea necesario
        width="100%",
    )
