import reflex as rx
import reflex_motion as rxm


def cursoscard(title: str, lugar: str) -> rx.Component:
    return rxm.motion(
        rx.card(
            rx.heading(title, size="4"),
            rx.blockquote(lugar, size="4"),
            # width="100%",
            # height="100%",
        ),
        initial={"scale": 1},
        while_hover={"scale": 1.2, "skew": 10},
        while_tap={"scale": 0.9},
        transition={"type": "spring", "stiffness": 260, "damping": 20},
    )
