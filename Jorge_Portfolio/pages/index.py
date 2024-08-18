"""The home page of the app."""

from Jorge_Portfolio import styles
from Jorge_Portfolio.templates import template
from Jorge_Portfolio.components.spline import spline
import Jorge_Portfolio.style.styles as styles
from Jorge_Portfolio.components.home_card import home_card
from reflex_animated_cursor import animated_cursor
import reflex as rx


@template(route="/", title="Home", description="description")
def index() -> rx.Component:
    return rx.vstack(
        # rx.desktop_only(animated_cursor(),inner_scale=0.5,outer_scale=1.0, show_system_cursor=True),
        rx.heading("Bienvenido a mi portfolio", level=1),
        spline(scene="https://prod.spline.design/CYgmTGMJ95Sj5Jmh/scene.splinecode"),
        rx.flex(
            home_card(
                "Trabajo en equipo",
                "Soy una persona proactiva, disfruto colaborando y aportando ideas innovadoras en equipo, adaptándome a diversos roles y responsabilidades para alcanzar metas comunes de manera eficiente.",
            ),
            home_card(
                "Organización",
                "Soy una persona organizada y metódica, cualidades que se reflejan en mi capacidad para gestionar proyectos de manera eficiente. "
                "Valoro el orden como una herramienta clave para mantener la claridad y el progreso. Utilizo herramientas digitales como Notion para "
                "optimizar la organización y maximizar la productividad en mi día a día. Me gusta establecer objetivos y trabajar para alcanzarlos.",
            ),
            home_card(
                "Creatividad",
                "La fotografía, la edición de vídeo y la impresión 3D son mis pasiones, a través de las cuales expreso mis ideas de forma visual. "
                "Mi enfoque creativo se traduce en la capacidad para transformar conceptos en proyectos visualmente atractivos, siempre buscando "
                "la innovación y el impacto visual.",
            ),
            home_card(
                "Autodidacta",
                "Estoy continuamente en búsqueda de nuevos conocimientos y habilidades, especialmente en el campo de la tecnología. "
                "Mi capacidad para aprender de manera autónoma me permite adaptarme rápidamente a nuevas herramientas y tendencias, manteniéndome al día en un campo "
                "tan dinámico como la informática.",
            ),
            home_card(
                "Habilidades",
                "Mis habilidades técnicas incluyen programación en Python, Java, C, C++ y SQL, así como conocimientos en desarrollo web y diseño de bases de datos. "
                "Actualmente estoy aprendiendo sobre desarrollo de aplicaciones móviles con Swift y diseño 3D. Además, tengo experiencia en el uso de herramientas como Git, Docker y Visual Studio Code."
                "Tengo un enfoque analítico y proactivo para la resolución de problemas, y he desarrollado habilidades de liderazgo a lo largo de mi carrera, guiando equipos hacia el logro de objetivos comunes.",
            ),
            home_card(
                "Idiomas",
                "Español: Nativo\nInglés: Avanzado (B2), certficado Cambridge B1\n",
            ),
            flex_wrap="wrap",
            align="start",
            justify="center",
            spacing="0.8em",
        ),
        width="100%",
        height="100%",
    )
