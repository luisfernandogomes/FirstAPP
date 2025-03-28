import flet as ft
from flet.core.app_bar import AppBar
from flet import AppBar, ElevatedButton, Page, Text, View
from flet.core.colors import Colors
from flet.core.textfield import TextField


def main(page: Page):
    page.title = "exemplo de rotas"
    page.theme_mode = ft.ThemeMode.DARK
    page.window_width = 375
    page.window_height = 667

    input_sobrenome = ft.TextField(label="digite seu sobrenome", hint_text="digite seu sobrenome")

    print_nome = ft.Text(value="dadada")



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
                    AppBar(title=Text("home"), bgcolor=Colors.PRIMARY_CONTAINER),
                    ElevatedButton(text="Navegar", on_click=lambda _: page.go("/segunda")),
                    input_sobrenome


                ]
            )
        )
        if page.route == "/segunda":
            page.views.append(
                View(
                    "/segunda",[
                        AppBar(title=Text("segunda tela"), bgcolor=Colors.SECONDARY_CONTAINER),
                        ft.TextField(f'Bem vindo {input_sobrenome.value}')
                        ]
                )
            )
        page.update()
    page.on_route_change = gerenciar_rotas
    page.on_view_pop = voltar
    page.on_route_change = gerenciar_rotas
    page.go(page.route)


ft.app(main)
