import reflex as rx


def link_button(title: str, logo: str, url: str) -> rx.Component:
    return rx.link(
        rx.button(rx.icon(logo),title),
        href=url,
        color="primary",
        size="large",
        is_external = True,
    )
