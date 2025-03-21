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
        txt_resultado.value = input_name.value + ' ' + input_sobrenome.value
        page.update()
    def parOuImpar(e):
        num = number1.value
        if int(num) % 2 == 0:
            resul_par_impar.value = "é par"
            page.update()
        else:
            resul_par_impar.value = "é impar"
            page.update()
    #
    # Criação de componentes
    input_name = ft.TextField(label="digite seu nome", hint_text="digite seu nome; Exemplo: Luis Fernando")
    input_sobrenome = ft.TextField(label="digite seu sobrenome", hint_text="digite seu sobrenome")
    btn_enviar = ft.FilledButton(text="Enviar", width=page.window.width, on_click=mostrar_nome)
    txt_resultado = ft.Text(value="")

    # Par ou Impar
    txt_explicao = ft.Text(value="Insira um numero a baixo e descubra se é par ou impar")
    number1 = ft.TextField(label="Insira um numero", hint_text="digite um numero")
    btn_par = ft.FilledButton(text="Descobrir", width=page.window.width, on_click=parOuImpar)
    resul_par_impar = ft.Text(value="")
    #
    # contruir o layout
    page.add(
        ft.Column(
            [

                input_name,
                input_sobrenome,
                btn_enviar,
                txt_resultado,


                txt_explicao,
                number1,
                btn_par,
                resul_par_impar,


            ]

        )

    )


ft.app(main)