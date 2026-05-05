import asyncio

import content
import flet
from flet import ThemeMode, View, Colors, Button, FloatingActionButton, Icons, TextField, ListView, Text, Card, Column, \
    Row, Icon, ListTile, PopupMenuButton, PopupMenuItem, Dropdown, DropdownOption, FontWeight, CrossAxisAlignment, \
    Container
from flet.controls.core import list_view
from flet.controls.material import floating_action_button


class Tamagotchi:
    def __init__(self, nome, cor, preco, idade):
        self.nome = nome
        self.cor = cor
        self.preco = preco
        self.idade = idade


def main(page: flet.Page):
    # Configurações
    page.title = "Primeiro APP"
    page.theme_mode = ThemeMode.DARK
    page.window.width = 400
    page.window.height = 700

    lista_dados = []

    # Navegar
    def navegar(route):
        asyncio.create_task(
            page.push_route(route)
        )

    # Funções
    def montar_lista_padrao():
        list_view.controls.clear()

        for item in lista_dados:
            list_view.controls.append(
                ListTile(
                    leading=Icon(Icons.TOYS),
                    title=item.nome,
                    subtitle=f"R$ {item.preco}",
                    trailing=PopupMenuButton(
                        icon=Icons.MORE_VERT,
                        items=[
                            PopupMenuItem(
                                "Ver Detalhes",
                                icon=Icons.REMOVE_RED_EYE,
                                on_click = lambda _, pessoa=item: ver_detalhes(pessoa)
                            ),
                            PopupMenuItem("Excluir", icon=Icons.DELETE, on_click=lambda: excluir(item)),
                        ]
                    ),
                )
            )


    def ver_detalhes(pessoa):
        text_nome.value = pessoa.nome
        text_preco.value = f"R$ {pessoa.preco}"
        text_cor.value = pessoa.cor
        if pessoa.idade == "De 1 a 7 dias":
            text_idade.value = f"Criança: {pessoa.idade}"
        elif pessoa.idade == "De 8 a 14 dias":
            text_idade.value = f"Jovem: {pessoa.idade}"
        elif pessoa.idade == "De 15 a 21 dias":
            text_idade.value = f"Adulto: {pessoa.idade}"
        elif pessoa.idade == "De 22 a 28 dias":
            text_idade.value = f"Idoso: {pessoa.idade}"

        navegar("/detalhes")


    def excluir(item):
        lista_dados.remove(item)
        montar_lista_padrao()

    tem_erro = False

    def salvar_dados():
        nome = input_nome.value
        preco = input_preco.value
        cor = input_cor.value
        idade = input_idade.value

        tem_erro = False
        if nome:
            input_nome.error = None
        else:
            tem_erro = True
            input_nome.error = "Campo obrigatorio"

        if preco:
            input_preco.error = None
        else:
            tem_erro = True
            input_preco.error = "Campo obrigatorio"

        if cor:
            input_cor.error = None
        else:
            tem_erro = True
            input_cor.error = "Campo obrigatorio"

        if idade:
            input_idade.error = None
        else:
            tem_erro = True
            input_cor.error = "Campo obrigatorio"

        if not tem_erro:
            # montar objeto
            tamagotchi = Tamagotchi(
                nome=nome,
                preco=preco,
                cor=cor,
                idade=idade
            )
            lista_dados.append(tamagotchi)

            input_nome.value = ""
            input_preco.value = ""
            input_cor.value = ""
            input_idade.value = ""

        montar_lista_padrao()


    # Gerenciar as telas(routes)
    def route_change():
        page.views.clear()
        montar_lista_padrao()
        page.views.append(
            View(
                route="/",
                controls=[
                    flet.AppBar(
                        title="Lista de Tamagotchi",
                    ),
                    list_view
                ],
                floating_action_button=FloatingActionButton(
                    icon=Icons.ADD,
                    on_click=lambda: navegar("/form_cadastro"),
                )
            )
        )
        if page.route == "/form_cadastro":
            page.views.append(
                View(
                    route="/form_cadastro",
                    controls=[
                        flet.AppBar(
                            title="Cadastro",
                        ),
                        input_nome,
                        input_preco,
                        input_cor,
                        input_idade,
                        btn_salvar
                    ]
                )
            )
        elif page.route == "/detalhes":
            page.views.append(
                View(
                    route="/detalhes",
                    controls=[
                        flet.AppBar(
                            title="Detalhes do Tamagotchi",
                        ),
                        Container(
                            Column([
                                text_nome,
                                Row([
                                    Icon(Icons.MONEY, color=Colors.PRIMARY, size=20),
                                    text_preco
                                ]),
                                Row([
                                    Icon(Icons.COLOR_LENS, color=Colors.PRIMARY, size=20),
                                    text_cor
                                ]),
                                Row([
                                    Icon(Icons.TIMER, color=Colors.PRIMARY, size=20),
                                    text_idade
                                ]),
                            ],
                                horizontal_alignment=CrossAxisAlignment.CENTER,
                            ),
                            bgcolor=Colors.BLUE_500,
                            padding=15,
                            border_radius=10,
                            width=400,
                        )
                    ]
                )
            )


    # Voltar
    async def view_pop(e):
        if e.view is not None:
            page.views.remove(e.view)
            top_view = page.views[-1]
            await page.push_route(top_view.route)


    # Componentes
    text_nome = Text(weight=FontWeight.BOLD, size=24)
    text_preco = Text()
    text_cor = Text()
    text_idade = Text()
    input_nome = TextField(label="Nome", hint_text="Digite o nome do seu Tamagotchi")
    input_preco = TextField(label="Preço", hint_text="Digite o preço do seu Tamagotchi")
    input_cor = TextField(label="Cor", hint_text="Digite a cor do seu Tamagotchi")
    input_idade = Dropdown(
        label="Idade",
        editable=True,
        options=[
            DropdownOption("De 1 a 7 dias"),
            DropdownOption("De 8 a 14 dias"),
            DropdownOption("De 15 a 21 dias"),
            DropdownOption("De 22 a 28 dias"),

        ],
    )
    btn_salvar = Button("Salvar", width=400, on_click=lambda: salvar_dados())
    list_view = ListView(height=500)

    # Eventos
    page.on_route_change = route_change
    page.on_view_pop = view_pop

    route_change()

flet.run(main)
