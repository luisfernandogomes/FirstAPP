import flet as ft
from time import sleep
from flet.core.app_bar import AppBar
from flet import AppBar, ElevatedButton, Page, Text, View
from flet.core.colors import Colors
from flet.core.textfield import TextField


def main(page: Page):
    page.title = "exemplo de rotas"
    page.theme_mode = ft.ThemeMode.DARK
    page.window_width = 375
    page.window_height = 667
    pb = ft.ProgressBar(width=400)
    def voltar(e):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)



    def gerenciar_rotas(e):
        page.views.clear()
        page.views.append(
            View(
                "/",
                [
                    AppBar(title=Text("home"), bgcolor=Colors.TERTIARY_CONTAINER),
                    ft.Icon(name=ft.Icons.FAVORITE, color=ft.Colors.TERTIARY_CONTAINER),
                    ft.Text("Linear progress indicator", style="headlineSmall"),
                    ft.Column([ft.Text("Doing something..."), pb]),
                    ft.Text("Indeterminate progress bar", style="headlineSmall"),
                    ft.ProgressBar(width=400, color="amber", bgcolor="#eeeeee"),
                    ElevatedButton(text="Regras", on_click=lambda _: page.go("/regras")),
                    ElevatedButton(text="Simulação", on_click=lambda _: page.go("/simulacao")),


                ]
            )


        )
        for i in range(0, 101):
            pb.value = i * 0.01
            sleep(0.1)
            page.update()
        if page.route == "/regras":
            page.views.append(
                View(
                    "/regras", [
                        AppBar(title=Text("regras"), bgcolor=Colors.SECONDARY_CONTAINER),
                        ElevatedButton(text="Inicio", on_click=lambda _: page.go("/")),
                        ElevatedButton(text="Simulação", on_click=lambda _: page.go("/simulacao"))
                    ]
                )
            )

        if page.route == "/resultado":
            page.views.append(
                View(
                    "/resultado", [
                        AppBar(title=Text("resultado"), bgcolor=Colors.SECONDARY_CONTAINER),
                        ElevatedButton(text="Inicio", on_click=lambda _: page.go("/")),
                        ElevatedButton(text="Regras", on_click=lambda _: page.go("/regras"))



                    ]
                )
            )

        if page.route == "/simulacao":
            page.views.append(
                View(
                    "/simulacao", [
                        AppBar(title=Text("simulacao"), bgcolor=Colors.SECONDARY_CONTAINER),
                        ElevatedButton(text="resultado", on_click=lambda _: page.go("/resultado")),
                        ElevatedButton(text="Inicio", on_click=lambda _: page.go("/inicio"))

                    ]
                )
            )

        page.update()

    page.on_route_change = gerenciar_rotas
    page.on_view_pop = voltar
    page.on_route_change = gerenciar_rotas
    page.go(page.route)


ft.app(main)
