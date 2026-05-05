import asyncio

import content
import flet
from flet import ThemeMode, View, Colors, Button, FloatingActionButton, Icons, TextField, ListView, Text, Card, Column, \
    Row, Icon, ListTile, PopupMenuButton, PopupMenuItem, Dropdown, DropdownOption, FontWeight
from flet.controls.material import floating_action_button

class Pessoa:
    def __init__(self, nome, profissao, sexo):
        self.nome = nome
        self.profissao = profissao
        self.sexo = sexo

def main(page: flet.Page):
    # Configurações
    page.title = "Primeiro APP"
    page.theme_mode = ThemeMode.DARK
    page.window.width = 400
    page.window.height = 700

    lista_dados = []

    # Funções
    # Navegar
    def navegar(route):
        asyncio.create_task(
            page.push_route(route)
        )

    def montar_lista_texto():
        list_view.controls.clear()

        for item in lista_dados:
            list_view.controls.append(
                Text(item)
            )

    def montar_lista_card():
        list_view.controls.clear()

        for item in lista_dados:
            list_view.controls.append(
                Card(
                    height=50,
                    content=Row([
                        Icon(Icons.PERSON),
                        Text(item.nome),
                        Text(item.profissao)
                    ],
                        margin=8
                    ),
                )
            )

    def montar_lista_padrao():
        list_view.controls.clear()

        for item in lista_dados:
            list_view.controls.append(
                ListTile(
                    leading=Icon(Icons.MAN) if item.sexo == "Masculino" else Icon(Icons.WOMAN),
                    title=item.nome,
                    subtitle=item.profissao,
                    trailing=PopupMenuButton(
                        icon=Icons.MORE_VERT,
                        items=[
                            PopupMenuItem("Ver Detalhes", icon=Icons.REMOVE_RED_EYE, on_click = lambda _, pessoa=item: ver_detalhes(pessoa)),
                            PopupMenuItem("Excluir", icon=Icons.DELETE, on_click=lambda: excluir(item)),
                        ]
                    ),
                )
            )

    def ver_detalhes(pessoa):
        text_nome.value = pessoa.nome
        text_profissao.value = pessoa.profissao
        text_sexo.value = pessoa.sexo

        navegar("/detalhes")

    def excluir(item):
        lista_dados.remove(item)
        montar_lista_padrao()

    tem_erro = False
    def salvar_dados():
        nome= input_nome.value
        profissao= input_profissao.value
        sexo = input_sexo.value

        tem_erro = False
        if nome:
            input_nome.error = None
        else:
            tem_erro = True
            input_nome.error = "Campo obrigatorio"

        if profissao:
            input_profissao.error = None
        else:
            tem_erro = True
            input_profissao.error = "Campo obrigatorio"

        if sexo:
            input_sexo.error = None
        else:
            tem_erro = True
            input_sexo.error = "Campo obrigatorio"

        if not tem_erro:
            # montar objeto
            pessoa = Pessoa(
                nome=nome,
                profissao=profissao,
                sexo=sexo,
            )
            lista_dados.append(pessoa)

            input_nome.value = ""
            input_profissao.value = ""
            input_sexo.value = ""

        montar_lista_texto()
        montar_lista_card()
        montar_lista_padrao()


    # Gerenciar as telas(routes)
    def route_change():
        page.views.clear()
        page.views.append(
            View(
                route="/",
                controls=[
                    flet.AppBar(
                        title="Exemplos de Listas",
                        bgcolor=Colors.AMBER_600
                    ),
                    Button("Lista de texto", on_click=lambda: navegar("/lista_texto")),
                    Button("Lista de Card", on_click=lambda: navegar("/lista_card")),
                    Button("Lista padrão Android", on_click=lambda: navegar("/lista_padrao"))
                ]
            )
        )
        if page.route == "/lista_texto":
            montar_lista_texto()
            page.views.append(
                View(
                    route="/lista_texto",
                    controls=[
                        flet.AppBar(
                            title="Lista de Texto",
                        ),
                        input_nome,
                        btn_salvar,
                        list_view
                    ]
                )
            )

        elif page.route == "/lista_card":
            montar_lista_card()
            page.views.append(
                View(
                    route="/lista_card",
                    controls=[
                        flet.AppBar(
                            title="Lista de Card",
                        ),
                        input_nome,
                        input_profissao,
                        input_sexo,
                        btn_salvar,
                        list_view
                    ]
                )
            )

        elif page.route == "/lista_padrao":
            montar_lista_padrao()
            page.views.append(
                View(
                    route="/lista_padrao",
                    controls=[
                        flet.AppBar(
                            title="Lista de padrão Android",
                        ),
                        list_view
                    ],
                    floating_action_button=FloatingActionButton(
                        icon=Icons.ADD,
                        on_click=lambda: navegar("/form_cadastro"),
                    )
                )
            )
        elif page.route == "/form_cadastro":
            page.views.append(
                View(
                    route="/form_cadastro",
                    controls=[
                        flet.AppBar(
                            title="Cadastro",
                        ),
                        input_nome,
                        input_profissao,
                        input_sexo,
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
                            title="Detalhes",
                        ),
                        text_nome,
                        text_profissao,
                        text_sexo
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
    text_profissao = Text()
    text_sexo = Text()
    input_nome = TextField(label="Nome", hint_text="Digite seu nome")
    input_profissao = TextField(label="Profissão", hint_text="Digite sua profissao")
    input_sexo = Dropdown(
        label="Sexo",
        editable=True,
        options=[
            DropdownOption("Masculino"),
            DropdownOption("Feminino"),

        ],
    )
    btn_salvar = Button("Salvar", width=400, on_click=lambda: salvar_dados())
    list_view = ListView(height=500)

    # Eventos
    page.on_route_change = route_change
    page.on_view_pop = view_pop

    route_change()

flet.run(main)
