import flet as ft
def main(page: ft.Page):

    # configutação da página
    page.title = "minha aplicação flet"
    page.theme_mode = ft.ThemeMode.DARK
    page.window.width = 375
    page.window.height = 667
    #
    # defiição de funções
    def mostrar_nome(e):
        txt_resultado.value = input_name.value + 'da o cu todo dia'
        page.update()
    #
    # Criação de componentes
    input_name = ft.TextField(label="digite seu nome", hint_text="digite seu nome; Exemplo: Luis Fernando")
    btn_enviar = ft.FilledButton(text="Enviar", width=page.window.width, on_click=mostrar_nome )
    txt_resultado = ft.Text(value="")
    #
    # contruir o layout
    page.add(
        ft.Column(
            [
                input_name,
                btn_enviar,
                txt_resultado,
            ]
        )
    )


ft.app(main)