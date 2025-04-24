import flet as ft
from flet import AppBar, Text, View
from flet.core.colors import Colors


def main(page: ft.Page):
    # Configurações
    page.title = "Exemplo de Rotas"
    page.theme_mode = ft.ThemeMode.DARK  # ou ft.ThemeMode.DARK
    page.window.width = 375
    page.window.height = 667

    # Funções
    lista = []

    def salvar_nome(e):
        if inputname.value == '':
            page.overlay.append(msg_error)
            msg_error.open = True
            page.update()
        elif inputname.value in lista:
            page.overlay.append(msg_error_repetido)
            msg_error_repetido.open = True
            page.update()
        else:
            lista.append(inputname.value)
            inputname.value = ""
            page.overlay.append(msg_sucesso)
            msg_sucesso.open = True
            page.update()

    def exibir_lista(e):
        lv_nome.controls.clear()
        for nome in lista:

            lv_nome.controls.append(
                ft.Text(value='nome: ' + nome)
            )
        page.update()
    def gerencia_rotas(e):
        page.views.clear()
        page.views.append(
            View(
                "/",
                [
                    AppBar(title=Text("Home"), bgcolor=Colors.PRIMARY_CONTAINER),
                    inputname,
                    ft.Button(
                        text='Salvar',
                        on_click=lambda _: salvar_nome(e),

                    ),
                    ft.Button(
                        text='Exibir',
                        on_click=lambda _: page.go('/segunda'),
                    )



                ],
            )
        )
        if page.route == "/segunda":
            exibir_lista(e)
            page.views.append(
                View(
                    "/segunda",
                    [
                        AppBar(title=Text("Segunda tela"), bgcolor=Colors.SECONDARY_CONTAINER),
                        lv_nome,
                        ft.FloatingActionButton('+', on_click=lambda _: page.go('/'),)

                    ],
                )
            )
        page.update()

    def voltar(e):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)


    # Componentes
    msg_sucesso = ft.SnackBar(
        content=ft.Text(value='nome salvado com sucesso'),
        bgcolor=Colors.GREEN,
        duration=1000,
                              )
    msg_error = ft.SnackBar(
        content=ft.Text(value='nome está vazio'),
        bgcolor=Colors.RED,
        duration=2000,
    )
    msg_error_repetido = ft.SnackBar(
        content=ft.Text(value='nome repetido'),
        bgcolor=Colors.RED,
        duration=2000,
    )
    lv_nome = ft.ListView(
        height=500,

    )
    inputname = ft.TextField(label='digite seu nome')



    # Eventos
    page.on_route_change = gerencia_rotas
    page.on_view_pop = voltar

    page.go(page.route)

# Comando que executa o aplicativo
# Deve estar sempre colado na linha
ft.app(main)