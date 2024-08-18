import reflex as rx

def skill_progress(skill: str, value: int, logo: str) -> rx.Component:
    return rx.card(
        rx.hstack(
            rx.image(src = logo, height="3em", alt="logo de "+skill),
            
            rx.vstack(
                rx.text(skill),
                rx.progress(value=value),
                width="100%",
            ),
        ),
        width = "350px",
        
    )