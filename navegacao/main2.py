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

    input_titulo = ft.TextField(label="digite titulo do livro", hint_text="digite titulo do livro")
    input_descricao = ft.TextField(label="digite descricao do livro", hint_text="digite descricao do livro")
    input_categoria = ft.TextField(label="digite da categoria", hint_text="digite da categoria")
    input_autor = ft.TextField(label="digite nome do autor", hint_text="digite nome do autor")

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

                    input_titulo,
                    input_descricao,
                    input_categoria,
                    input_autor,
                    ElevatedButton(text="Navegar", on_click=lambda _: page.go("/segunda"))

                ]
            )
        )
        if page.route == "/segunda":
            page.views.append(
                View(
                    "/segunda", [
                        AppBar(title=Text("segunda tela"), bgcolor=Colors.SECONDARY_CONTAINER),

                        ft.TextField(f'{input_titulo.value}'),
                        ft.TextField(f'{input_descricao.value}'),
                        ft.TextField(f'{input_categoria.value}'),
                        ft.TextField(f'{input_autor.value}')
                    ]
                )
            )
        page.update()

    page.on_route_change = gerenciar_rotas
    page.on_view_pop = voltar
    page.on_route_change = gerenciar_rotas
    page.go(page.route)


ft.app(main)
