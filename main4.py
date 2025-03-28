import flet as ft
import datetime
from dateutil import parser, relativedelta
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


    # maior de idade

    def maiorDeIdade(e):

        try:
            idade_recebida = input_data_nas.value
            data_recebida = parser.parse(idade_recebida)
            tempo_atual = datetime.date.today()
            idade = tempo_atual - data_recebida
            ano_subtraido = tempo_atual.year -data_recebida.year
            meses_subtraido = tempo_atual.month -data_recebida.month
            dias_subtraido = tempo_atual.day -data_recebida.day

            if ano_subtraido > 112:
                maior_de_idade.value = 'data de nascimento invalido, não tem como ter mais de 120 anos'
                page.update()

            elif ano_subtraido >= 18 and meses_subtraido >= 0 and dias_subtraido >= 0:
                maior_de_idade.value = 'voce é maior de idade'
                page.update()

            else:
                maior_de_idade.value = 'voce é menor de idade'
                page.update()
        except ValueError:
            maior_de_idade.value = "data de nascimento invalido"
            page.update()




        # maior_de_idade.value = data.date()



        # if idade_atual < 18:
        #     maior_de_idade.value = 'Voce é menor de idade'
        #     page.update()
        # else:
        #     maior_de_idade.value = 'Voce é maior de idade'
        #     page.update()

    #
    # Criação de componentes
    input_name = ft.TextField(label="digite seu nome", hint_text="digite seu nome; Exemplo: Luis Fernando")
    btn_enviar = ft.FilledButton(text="Enviar", width=page.window.width, on_click=mostrar_nome )
    txt_resultado = ft.Text(value="")



    input_data_nas = ft.TextField(label="insira sua data de nascimento", hint_text="digite seu ano de nascimento")
    btn_calcular = ft.FilledButton(text="calcular idade", width=page.window.width, on_click=maiorDeIdade)
    maior_de_idade = ft.Text(value="")

    #
    # contruir o layout
    page.add(
        ft.Column(
            [
                input_name,
                btn_enviar,
                txt_resultado,

                input_data_nas,
                btn_calcular,
                maior_de_idade,
            ]
        )
    )


ft.app(main)