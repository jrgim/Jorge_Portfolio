import reflex as rx
import reflex_motion as rxm


def home_card(title: str, body: str) -> rx.Component:
    return rxm.motion(
        rx.card(
            rx.vstack(
                rx.heading(
                    title,
                    level=2,
                    color_scheme="mint",
                    align="center",
                ),
                rx.spacer(spacing="5"),
                rxm.motion(
                    rx.text(
                        body,
                    ),
                    initial={"scale": 1.0},
                    transition={"type": "tween", "stiffness": 400, "damping": 17},
                ),
            ),
            width="100%",
        ),
        while_hover={"scale": 1.0},
        while_tap={"scale": 0.9},
        transition={"type": "spring", "stiffness": 400, "damping": 17},
    )
