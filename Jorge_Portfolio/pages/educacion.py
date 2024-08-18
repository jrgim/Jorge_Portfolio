import reflex as rx
from Jorge_Portfolio.templates import template
from Jorge_Portfolio.components.skill_progress import skill_progress
from Jorge_Portfolio.components.cursoscard import cursoscard


@template(route="/educacion", title="Educación")
def educacion() -> rx.Component:
    return rx.vstack(
        rx.heading("Formación", value="1"),
        rx.flex(
            rx.card(
                rx.heading("ESO y Bachillerato de ciencias", size="5"),
                rx.blockquote("El Pilar Maristas", size="4"),
                rx.text.em("2016 - 2022", size="5"),
            ),
            rx.card(
                rx.heading("Ingeniería Informática", size="5"),
                rx.blockquote("Universidad San Jorge", size="4"),
                rx.text.em("2022 - Actualidad", size="5"),
            ),
            spacing="2",
        ),
        rx.heading("Skills", value="1"),
        rx.flex(
            skill_progress("Java", 70, "/java.svg"),
            skill_progress("Docker", 60, "/docker.svg"),
            skill_progress("C", 50, "/c.png"),
            skill_progress("C++", 70, "/cpp.png"),
            skill_progress("SQL", 70, "/sql.png"),
            skill_progress("Photoshop", 80, "/photoshop.png"),
            skill_progress("Final Cut Pro", 80, "/finalcutpro.png"),
            flex_wrap="wrap",
            spacing="2",
        ),
        rx.heading("Aprendiendo", value="1"),
        rx.flex(
            skill_progress("HTML", 0, "/html.svg"),
            skill_progress("Blender", 0, "/blender.png"),
            skill_progress("Python", 0, "/python.svg"),
            #skill_progress("Swift", 10, "/swift.png"),
            flex_wrap="wrap",
            spacing="2",
        ),
        rx.heading("Cursos - Meritos", value="1"),
        rx.flex(
            cursoscard(
                "2022  -  3º premio en la Olimpiada Informática de Aragón",
                "Escuela de ingenieros",
            ),
            cursoscard(
                "2024 - Curso de Docker y seguridad - 3h", "Universidad San Jorge"
            ),
            cursoscard(
                "2024 - Curso de introduccion a la Inteligencia Artificial y casos prácticos - 10h",
                "Universidad San Jorge",
            ),
            cursoscard("2024 - Participación Hackathon", "Code_Labs"),
            cursoscard(
                "2024 - 1º Premio Hackathon Pentesting", "Universidad San Jorge"
            ),
            spacing="2",
            wrap="wrap",
        ),
        width="100%",
    )
