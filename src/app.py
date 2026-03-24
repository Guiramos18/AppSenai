import flet
from flet import ThemeMode, Text, TextField, OutlinedButton, Column, CrossAxisAlignment
from flet.controls import page
from flet.controls.border_radius import horizontal


def main(page: flet.Page):
    # Configurações
    page.title = "Primeiro APP"
    page.theme_mode = ThemeMode.DARK
    page.window.width = 400
    page.window.height = 700

    # Funções

    def salvar_nome(nome):
        text.value = f"Bom dia {input_nome.value} {input_nome2.value}"
        page.update()


    def impar_par():

        num_convertido = int(numero1.value)


        if num_convertido % 2 == 0:
            texto = 'Par'

        else:
            texto = 'Impar'


        text.value = f"Seu numero é {texto}"
        page.update()

    def verificar_idade():
        idade_convertida = int(data_nasc.value)
        sua_idade= 2026 - idade_convertida
        if sua_idade >= 18:
            texto = 'maior de idade'

        else:
            texto = 'menor de idade'

        text.value = f"Você é {texto}"
        page.update()




    # Componentes
    text = Text("Ola mundo")

    input_nome = TextField(label="Nome")
    input_nome2 = TextField(label="Sobrenome")
    numero1 = TextField(label="Digite o numero")
    data_nasc = TextField(label="Data de nascimento")
    btn_salvar = OutlinedButton("Salvar", on_click=salvar_nome)
    btn_impar_par = OutlinedButton("Impar ou par", on_click=impar_par)
    btn_idade = OutlinedButton("Verificar idade", on_click=verificar_idade)


    # Construção da tela
    page.add(
        Column(
            [
            input_nome,
            input_nome2,
            numero1,
            data_nasc,
            btn_salvar,
            btn_impar_par,
            btn_idade,
            text,
            ],
            width=400,
            horizontal_alignment=CrossAxisAlignment.CENTER
        )
    )



flet.app(main)