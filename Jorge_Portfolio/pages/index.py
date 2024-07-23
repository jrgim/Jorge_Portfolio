"""The home page of the app."""

from Jorge_Portfolio import styles
from Jorge_Portfolio.templates import template
from Jorge_Portfolio.components.spline import spline
import Jorge_Portfolio.style.styles as styles
import reflex as rx


@template(route="/", title="Home", description="descriip")
def index() -> rx.Component:
    return rx.vstack(
        rx.heading("Bienvenido a mi portfolio", level=1),
        spline(scene="https://prod.spline.design/CYgmTGMJ95Sj5Jmh/scene.splinecode"),
        rx.heading("Sobre mi", level=2),
        rx.text(
            "Soy Jorge Giménez, estudiante de ingeniería informática en la Universidad San Jorge. "
            "Me apasiona la programación, la tecnología y el diseño 3D. Estoy en constante aprendizaje para mejorar mis habilidades."
        ),
        rx.flex(
            rx.card(
                rx.heading("Trabajo en equipo", level=2, color_scheme="mint"),
                rx.text(
                    "Soy una persona proactiva, disfruto colaborando y aportando ideas innovadoras en equipo, adaptándome a diversos roles y responsabilidades "
                    "para alcanzar metas comunes de manera eficiente. Me gusta trabajar en equipo, aportando mis conocimientos y aprendiendo de los demás."
                ),
            ),
            rx.card(
                rx.heading("Organización", level=2, color_scheme="mint"),
                rx.text(
                    "Soy una persona organizada y metódica, cualidades que se reflejan en mi capacidad para gestionar proyectos de manera eficiente. "
                    "Valoro el orden como una herramienta clave para mantener la claridad y el progreso. Utilizo herramientas digitales como Notion para "
                    "optimizar la organización y maximizar la productividad en mi día a día. Me gusta establecer objetivos y trabajar para alcanzarlos."
                ),
            ),
            rx.card(
                rx.heading("Creatividad", level=2, color_scheme="mint"),
                rx.text(
                    "La fotografía, la edición de vídeo y la impresión 3D son mis pasiones, a través de las cuales expreso mis ideas de forma visual. "
                    "Mi enfoque creativo se traduce en la capacidad para transformar conceptos en proyectos visualmente atractivos, siempre buscando "
                    "la innovación y el impacto visual."
                ),
            ),
            rx.card(
                rx.heading("Autodidacta", level=2, color_scheme="mint"),
                rx.text(
                    "Estoy continuamente en búsqueda de nuevos conocimientos y habilidades, especialmente en el campo de la tecnología. "
                    "Mi capacidad para aprender de manera autónoma me permite adaptarme rápidamente a nuevas herramientas y tendencias, manteniéndome al día en un campo "
                    "tan dinámico como la informática."
                ),
            ),
            rx.card(
                rx.heading("Habilidades", level=2, color_scheme="mint"),
                rx.text(
                    "Mis habilidades técnicas incluyen programación en Python, Java, C, C++ y SQL, así como conocimientos en desarrollo web y diseño de bases de datos. "
                    "Actualmente estoy aprendiendo sobre desarrollo de aplicaciones móviles con Swift y diseño 3D. Además, tengo experiencia en el uso de herramientas como Git, Docker y Visual Studio Code."
                    "Tengo un enfoque analítico y proactivo para la resolución de problemas, y he desarrollado habilidades de liderazgo a lo largo de mi carrera, guiando equipos hacia el logro de objetivos comunes."
                ),
            ),
            rx.card(
                rx.heading("Idiomas", level=2, color_scheme="mint"),
                rx.text("Español: Nativo\nInglés: Avanzado (B2)\nFrancés: Básico"),
                width="100%",
            ),
            flex_wrap="wrap",
            align="stretch",
            justify="center",
            spacing="0.1em",
        ),
        width="100%",
        height="100%",
    )

    # = Para poner todo el texto de un README.md en una pagina
    """The home page.

    Returns:
        The UI for the home page.
    
    with open("README.md", encoding="utf-8") as readme:
        content = readme.read()
    return rx.markdown(content, component_map=styles.markdown_style)"""
