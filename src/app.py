import flet
from flet import ThemeMode, Text, TextField, OutlinedButton, Column, CrossAxisAlignment, ElevatedButton, TextButton, \
    Container, Colors
from datetime import datetime
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


        text2.value = f"Seu numero é {texto}"
        page.update()

    def verificar_idade():
        idade_convertida = int(data_nasc.value)
        sua_idade= datetime.now().year - idade_convertida
        if sua_idade >= 18:
            texto = 'maior de idade'

        else:
            texto = 'menor de idade'

        text3.value = f"Você é {texto}"
        page.update()




    # Componentes
    text = Text("")
    text2 = Text("")
    text3 = Text("")

    input_nome = TextField(label="Nome")
    input_nome2 = TextField(label="Sobrenome")
    numero1 = TextField(label="Digite o numero")
    data_nasc = TextField(label="Ano de nascimento")
    btn_salvar = OutlinedButton("Salvar", on_click=salvar_nome)
    btn_impar_par = ElevatedButton("Impar ou par", on_click=impar_par)
    btn_idade = TextButton("Verificar idade", on_click=verificar_idade)


    # Construção da tela
    page.add(
        Column(
            [
                Container(
                    Column(
                        [
                            Text("Atividade 1", weight="bold"),
                            input_nome,
                            input_nome2,
                            btn_salvar,
                            text,
                        ],
                        horizontal_alignment=CrossAxisAlignment.CENTER,
                    ),
                    bgcolor=Colors.BLUE_500,
                    padding=15,
                    border_radius=10,
                    width=400,
                ),

                Container(
                    Column(
                        [
                            Text("Atividade 2", weight="bold"),
                            numero1,
                            btn_impar_par,
                            text2,
                        ],
                        horizontal_alignment=CrossAxisAlignment.CENTER,
                    ),
                    bgcolor=Colors.AMBER_600,
                    padding=15,
                    border_radius=10,
                    width=400,
                ),

                Container(
                    Column(
                        [
                            Text("Atividade 3", weight="bold"),
                            data_nasc,
                            btn_idade,
                            text3,
                        ],
                        horizontal_alignment=CrossAxisAlignment.CENTER,
                    ),
                    bgcolor=Colors.GREEN_800,
                    padding=15,
                    border_radius=10,
                    width=400,
                ),
            ],
            width=400,
            horizontal_alignment=CrossAxisAlignment.CENTER
        )
    )



flet.run(main)