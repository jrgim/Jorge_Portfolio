import reflex as rx

def skill_progress(skill: str, value: int, logo: str) -> rx.Component:
    return rx.card(
        rx.hstack(
            rx.image(src = logo, height="3em"),
            rx.spacer(),
            rx.vstack(
                rx.text(skill),
            ),
            rx.progress(value=value, width="300px"),
        ),
    )