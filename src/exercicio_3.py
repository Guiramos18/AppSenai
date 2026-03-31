import asyncio
from os import remove

import flet
from flet import ThemeMode, View, control, AppBar, Colors, Button, TextField, Text
from rich.color import Color


def main(page: flet.Page):
    # Configurações
    page.title = "Primeiro APP"
    page.theme_mode = ThemeMode.LIGHT  # ou Dark
    page.window.width = 400
    page.window.height = 700


    tem_erro = False
    # Funções
    def tamagotchi():
        text_nome.value = f"Nome: {input_nome.value}"
        text_cor.value = f"Cor: {input_cor.value}"
        text_cor.value = f"Preço: R${input_preco.value}"

        tem_erro = False
        if input_nome.value:
            input_nome.error = None
        else:
            tem_erro = True
            input_nome.error = "Campo obrigatorio"

        if input_cor.value:
            input_cor.error = None
        else:
            tem_erro = True
            input_cor.error = "Campo obrigatorio"

        if input_preco.value:
            input_cor.error = None
        else:
            tem_erro = True
            input_preco.error = "Campo obrigatorio"

        if not tem_erro:
            input_nome.value = ""
            input_cor.value = ""
            input_preco.value = ""
            navegar("/tela_msg")


    # Navegar
    def navegar(route):
        asyncio.create_task(
            page.push_route(route)
        )
    # Gerenciar as telas(routes)
    def route_change():
        page.views.clear()
        page.views.append(
            View(
                route="/",
                controls=[
                    AppBar(
                        title="Cadastro Tamagotchi",
                        bgcolor=Colors.AMBER_200

                    ),
                    Text("Digite seus Dados!"),
                    input_nome,
                    input_cor,
                    input_preco,
                    btn_salvar,
                ]

            )
        )
        if page.route == "/tela_msg":
            page.views.append(
                View(
                    route="/tela_msg",
                    controls=[
                        AppBar(
                            title="Seus Dados",
                            bgcolor=Colors.AMBER_200

                        ),
                        text_nome,
                        text_cor,
                        text_preco
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
    input_nome = TextField(label="Nome:")
    input_cor = TextField(label="Cor:")
    input_preco = TextField(label="Preço:")
    text_nome = Text()
    text_cor = Text()
    text_preco = Text()
    btn_salvar = Button("Salvar", on_click= tamagotchi)



    # Eventos
    page.on_route_change = route_change
    page.on_view_pop = view_pop

    route_change()

flet.run(main)