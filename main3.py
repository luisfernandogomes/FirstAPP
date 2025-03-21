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
    def soma(e):
        number1 = int(num1.value)
        number2 = int(num2.value)
        resultado = number1 + number2
        resultado_ope.value = resultado
        page.update()

    def subtracao(e):
        number1 = int(num1.value)
        number2 = int(num2.value)
        resultado = number1 - number2
        resultado_ope.value = resultado
        page.update()

    def divisao(e):
        number1 = int(num1.value)
        number2 = int(num2.value)
        resultado = number1 / number2
        resultado_ope.value = resultado

        page.update()

    def multiplicao(e):
        number1 = int(num1.value)
        number2 = int(num2.value)
        resultado = number1 * number2
        resultado_ope.value = resultado
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


    # operações basicas
    # inputs
    txt_operacoes_basicas = ft.Text(value="insira numero nos campos e selecione a operacao")
    num1 = ft.TextField(label="insira o primeiro numero", hint_text="valor numerico")
    num2 = ft.TextField(label="insira o segundo numero", hint_text="valor numerico")
    # botoes
    btn_soma = ft.FilledButton(text="soma", width=page.window.width, on_click=soma)
    btn_subtracao = ft.FilledButton(text="subtracao", width=page.window.width, on_click=subtracao)
    btn_divisao = ft.FilledButton(text="divisao", width=page.window.width,on_click=divisao)
    btn_multiplicacao = ft.FilledButton(text="multiplicacao", width=page.window.width, on_click=multiplicao)

    # exibir resultado
    resultado_ope = ft.Text(value="")


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

                txt_operacoes_basicas,
                num1,
                num2,
                btn_soma,
                btn_subtracao,
                btn_divisao,
                btn_multiplicacao,
                resultado_ope,


            ]

        )

    )


ft.app(main)