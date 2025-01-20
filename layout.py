import flet as ft
#criando uma classe para meus produtos
#irei criar uns atributos dentro da classe
class Produto(self, nome, preco, descricao):
    self.nome = nome
    self.preco = preco
    self.descricao = descricao

#definindo carrinho como um dicionario
carrinho []

carrinho = criar_carrinho(page)
    page.title = "Cardápio"
    page.horizontal_alignment = "center"
    page.bgcolor = "#f0f0f0"
    page.vertical_alignment = "center"

    tabs = ft.Tabs(
        tabs=[
            ft.Tab(text="Doces"),
            ft.Tab(text="Lanches"),
            ft.Tab(text="Combos"),
            ft.Tab(text="Porções"),
            ft.Tab(text="Bebidas"),
            ft.Tab(text="Carrinho"),
        ],
        on_change=lambda e: mudar_aba(page, e),
    )

    conteudo_inicial = criar_conteudo(tabs.tabs[0].text)

    page.controls = [
        ft.Container(
            content=ft.Column(
                horizontal_alignment="center",
                controls=[
                    ft.Text("Cardápio KiDeli", text_align="center"),
                    tabs,
                    conteudo_inicial,
                ],
            ),
            bgcolor="transparent",
            border_radius=10,
            padding=ft.padding.all(20),
            width=page.width,
            height=page.height,
            expand=True,
        )
    ]
    page.update()



#logo abaixo estara o conteudo dos produtos do restaurante
def criar_conteudo(aba:str):
    if aba == "Doces":
        return ft.Column(
            scroll=True,
            expand=True,
            controls=[
                ft.Row(
                    wrap=True,
                    controls=[
                        ft.Container(
                            width=200,
                            height=450,
                            padding=ft.padding.all(20),
                            border_radius=10,
                            bgcolor="white",
                            content=ft.Column(
                                controls=[
                                    ft.Image(
                                        "lan.jpg",
                                        width=150,
                                        height=180,
                                        fit="cover",
                                    ),
                                    ft.Text("Brownie", weight="bold"),
                                    ft.Text("R$ 15,00"),
                                    ft.ElevatedButton("Adicionar ao carrinho", on_click=lambda e: adicionar_ao_carrinho(e.control.page, Produto("Brownie", 15.00, "Descrição"))),
                                ]
                            ),
                        ),
                        ft.Container(
                            width=200,
                            height=450,
                            padding=ft.padding.all(20),
                            border_radius=10,
                            bgcolor="white",
                            content=ft.Column(
                                controls=[
                                    ft.Image(
                                        "lan.jpg",
                                        width=150,
                                        height=180,
                                        fit="cover",
                                    ),
                                    ft.Text("Dadinho de Brownie", weight="bold"),
                                    ft.Text("R$ 20,00"),
                                    ft.ElevatedButton("Adicionar ao carrinho", on_click=lambda e: adicionar_ao_carrinho(e.control.page, Produto("Dadinho de Brownie", 20.00, "Descrição"))),
                                ]
                            ),
                        ),
                        ft.Container(
                            width=200,
                            height=450,
                            padding=ft.padding.all(20),
                            border_radius=10,
                            bgcolor="white",
                            content=ft.Column(
                                controls=[
                                    ft.Image(
                                        "lan.jpg",
                                        width=150,
                                        height=180,
                                        fit="cover",
                                    ),
                                    ft.Text("Slice Cake", weight="bold"),
                                    ft.Text("R$ 20,00"),
                                    ft.ElevatedButton("Adicionar ao carrinho", on_click=lambda e: adicionar_ao_carrinho(e.control.page, Produto("Slice Cake", 20.00, "Descrição"))),
                                ]
                            ),
                        ),
                        ft.Container(
                            width=200,
                            height=450,
                            padding=ft.padding.all(20),
                            border_radius=10,
                            bgcolor="white",
                            content=ft.Column(
                                controls=[
                                    ft.Image(
                                        "lan.jpg",
                                        width=150,
                                        height=180,
                                        fit="cover",
                                    ),
                                    ft.Text("Fatias KiDeli", weight="bold"),
                                    ft.Text("R$ 20,00"),
                                    ft.ElevatedButton("Adicionar ao carrinho", on_click=lambda e: adicionar_ao_carrinho(e.control.page, Produto("Fatias KiDeli", 20.00, "Descrição"))),
                                ]
                            ),
                        ),
                        ft.Container(
                            width=200,
                            height=450,
                            padding=ft.padding.all(20),
                            border_radius=10,
                            bgcolor="white",
                            content=ft.Column(
                                controls=[
                                    ft.Image(
                                        "lan.jpg",
                                        width=150,
                                        height=180,
                                        fit="cover",
                                    ),
                                    ft.Text("Canole", weight="bold"),
                                    ft.Text("R$ 20,00"),
                                    ft.ElevatedButton("Adicionar ao carrinho", on_click=lambda e: adicionar_ao_carrinho(e.control.page, Produto("Canole", 20.00, "Descrição"))),
                                ]
                            ),
                        ),
                    ]
                )
            ]
        )
    elif aba == "Lanches":
        return ft.Column(
            scroll=True,
            expand=True,
            controls=[
                ft.Row(
                    wrap=True,
                    controls=[
                        ft.Container(
                            width=200,
                            height=450,
                            padding=ft.padding.all(20),
                            border_radius=10,
                            bgcolor="white",
                            content=ft.Column(
                                controls=[
                                    ft.Image(
                                        "lan.jpg",
                                        width=150,
                                        height=180,
                                        fit="cover",
                                    ),
                                    ft.Text("Smash Cheddar", weight="bold"),
                                    ft.Text("R$ 19,99", style="bodyMedium"),
                                    ft.Text("Hambúrguer acompanhado de Queijo cheddar especial", color="grey"),
                                    ft.ElevatedButton("Adicionar ao carrinho", on_click=lambda e: adicionar_ao_carrinho(e.control.page, Produto("Smash Burguer", 19.99, "Descrição"))),
                                ]
                            ),
                        ),
                        ft.Container(
                            width=200,
                            height=450,
                            padding=ft.padding.all(20),
                            border_radius=10,
                            bgcolor="white",
                            content=ft.Column(
                                controls=[
                                    ft.Image(
                                        "lan.jpg",
                                        width=150,
                                        height=180,
                                        fit="cover",
                                    ),
                                    ft.Text("Duplo Smash Cheddar", weight="bold"),
                                    ft.Text("R$ 29,99", style="bodyMedium"),
                                    ft.Text("2 hambúrgueres, Queijo cheddar especial em dobro", color="grey"),
                                    ft.ElevatedButton("Adicionar ao carrinho", on_click=lambda e: adicionar_ao_carrinho(e.control.page, Produto("Duplo Smash Burguer", 29.99, "Descrição"))),
                                ]
                            ),
                        ),
                        ft.Container(
                            width=200,
                            height=450,
                            padding=ft.padding.all(20),
                            border_radius=10,
                            bgcolor="white",
                            content=ft.Column(
                                controls=[
                                    ft.Image(
                                        "lan.jpg",
                                        width=150,
                                        height=180,
                                        fit="cover",
                                    ),
                                    ft.Text("X-Burguer KiDeli", weight="bold"),
                                    ft.Text("R$ 29,99", style="bodyMedium"),
                                    ft.Text("Hambúrguer de 100g, Queijo cheddar especial", color="grey"),
                                    ft.ElevatedButton("Adicionar ao carrinho", on_click=lambda e: adicionar_ao_carrinho(e.control.page, Produto("X-Burguer KiDeli", 29.99, "Descrição"))),
                                ]
                            ),
                        ),
                        ft.Container(
                            width=200,
                            height=450,
                            padding=ft.padding.all(20),
                            border_radius=10,
                            bgcolor="white",
                            content=ft.Column(
                                controls=[
                                    ft.Image(
                                        "lan.jpg",
                                        width=150,
                                        height=180,
                                        fit="cover",
                                    ),
                                    ft.Text("X-Salada KiDeli", weight="bold"),
                                    ft.Text("R$ 25,00", style="bodyMedium"),
                                    ft.Text("Hambúrguer de 100g, 2 fatias de queijo mussarela, 2 rodelas de tomate, alface e maionese verde da casa", color="grey"),
                                    ft.ElevatedButton("Adicionar ao carrinho", on_click=lambda e: adicionar_ao_carrinho(e.control.page, Produto("X-Salada KiDeli", 25.00, "Descrição"))),
                                ]
                            ),
                        ),
                        ft.Container(
                            width=200,
                            height=450,
                            padding=ft.padding.all(20),
                            border_radius=10,
                            bgcolor="white",
                            content=ft.Column(
                                controls=[
                                    ft.Image(
                                        "lan.jpg",
                                        width=150,
                                        height=180,
                                        fit="cover",
                                    ),
                                    ft.Text("Cheddar Classic Bacon", weight="bold"),
                                    ft.Text("R$ 34,99", style="bodyMedium"),
                                    ft.Text("Hambúrguer de 100g, Molho cheddar especial, cebola caramelizada e bacon crocante", color="grey"),
                                    ft.ElevatedButton("Adicionar ao carrinho", on_click=lambda e: adicionar_ao_carrinho(e.control.page, Produto("Cheddar Classic Bacon", 34.99, "Descrição"))),
                                ]
                            ),
                        ),
                        ft.Container(
                            width=200,
                            height=450,
                            padding=ft.padding.all(20),
                            border_radius=10,
                            bgcolor="white",
                            content=ft.Column(
                                controls=[
                                    ft.Image(
                                        "lan.jpg",
                                        width=150,
                                        height=180,
                                        fit="cover",
                                    ),
                                    ft.Text("Cheddar Supremo KiDeli", weight="bold"),
                                    ft.Text("R$ 45,00", style="bodyMedium"),
                                    ft.Text("Hambúrguer de 150g, Muito molho cheddar especial, farofa de bacon, geléia de alho caramelizado", color="Grey"),
                                    ft.ElevatedButton("Adicionar ao carrinho", on_click=lambda e: adicionar_ao_carrinho(e.control.page, Produto("Cheddar Supremo KiDeli", 45.00, "Descrição"))),
                                ]
                            ),
                        ),
                        ft.Container(
                            width=200,
                            height=450,
                            padding=ft.padding.all(20),
                            border_radius=10,
                            bgcolor="white",
                            content=ft.Column(
                                controls=[
                                    ft.Image(
                                        "lan.jpg",
                                        width=150,
                                        height=180,
                                        fit="cover",
                                    ),
                                    ft.Text("Catupiry Supremo KiDeli", weight="bold"),
                                    ft.Text("R$ 40,00", style="bodyMedium"),
                                    ft.Text("Hambúrguer de 150g, Catupiry empanado 80g, geléia de pimentão, maionese verde da casa", color="grey"),
                                    ft.ElevatedButton("Adicionar ao carrinho", on_click=lambda e: adicionar_ao_carrinho(e.control.page, Produto("Catupiry Supremo", 40.00, "Descrição"))),
                                ]
                            ),
                        ),
                    ]
                )
            ]
        )
    elif aba == "Combos":
        return ft.Column(
            scroll=True,
            expand=True,
            controls=[
                ft.Row(
                    wrap=True,
                    controls=[
                        ft.Container(
                            width=200,
                            height=450,
                            padding=ft.padding.all(20),
                            border_radius=10,
                            bgcolor="white",
                            content=ft.Column(
                                controls=[
                                    ft.Image(
                                        "lan.jpg",
                                        width=150,
                                        height=180,
                                        fit="cover",
                                    ),
                                    ft.Text("Combo Hambúrguer + Batata Frita", weight="bold"),
                                    ft.Text("R$ 25,00", style="bodyMedium"),
                                    ft.ElevatedButton("Adicionar ao carrinho", on_click=lambda e: adicionar_ao_carrinho(e.control.page, Produto("Brownie", 15.00, "Descrição"))),
                                ]
                            ),
                        ),
                        ft.Container(
                            width=200,
                            height=450,
                            padding=ft.padding.all(20),
                            border_radius=10,
                            bgcolor="white",
                            content=ft.Column(
                                controls=[
                                    ft.Image(
                                        "lan.jpg",
                                        width=150,
                                        height=180,
                                        fit="cover",
                                    ),
                                    ft.Text("Combo Cachorro Quente + Refrigerante", weight="bold"),
                                    ft.Text("R$ 20,00", style="bodyMedium"),
                                    ft.ElevatedButton("Adicionar ao carrinho"),
                                ]
                            ),
                        ),
                    ]
                )
            ]
        )
    elif aba == "Porções":
        return ft.Column(
            scroll=True,
            expand=True,
            controls=[
                ft.Row(
                    wrap=True,
                    controls=[
                        ft.Container(
                            width=200,
                            height=450,
                            padding=ft.padding.all(20),
                            border_radius=10,
                            bgcolor="white",
                            content=ft.Column(
                                controls=[
                                    ft.Image(
                                        "lan.jpg",
                                        width=150,
                                        height=180,
                                        fit="cover",
                                    ),
                                    ft.Text("Batata Frita Pequena", weight="bold"),
                                    ft.Text("R$ 29,99", style="bodyMedium"),
                                    ft.ElevatedButton("Adicionar ao carrinho"),
                                ]
                            ),
                        ),
                        ft.Container(
                            width=200,
                            height=450,
                            padding=ft.padding.all(20),
                            border_radius=10,
                            bgcolor="white",
                            content=ft.Column(
                                controls=[
                                    ft.Image(
                                        "lan.jpg",
                                        width=150,
                                        height=180,
                                        fit="cover",
                                    ),
                                    ft.Text("Batata Frita Média", weight="bold"),
                                    ft.Text("R$ 29,99", style="bodyMedium"),
                                    ft.ElevatedButton("Adicionar ao carrinho"),
                                ]
                            ),
                        ),
                        ft.Container(
                            width=200,
                            height=450,
                            padding=ft.padding.all(20),
                            border_radius=10,
                            bgcolor="white",
                            content=ft.Column(
                                controls=[
                                    ft.Image(
                                        "lan.jpg",
                                        width=150,
                                        height=180,
                                        fit="cover",
                                    ),
                                    ft.Text("Batata Frita Grande", weight="bold"),
                                    ft.Text("R$ 29,99", style="bodyMedium"),
                                    ft.ElevatedButton("Adicionar ao carrinho"),
                                ]
                            ),
                        ),
                        ft.Container(
                            width=200,
                            height=450,
                            padding=ft.padding.all(20),
                            border_radius=10,
                            bgcolor="white",
                            content=ft.Column(
                                controls=[
                                    ft.Image(
                                        "lan.jpg",
                                        width=150,
                                        height=180,
                                        fit="cover",
                                    ),
                                    ft.Text("Batata Frita Especial", weight="bold"),
                                    ft.Text("R$ 29,99", style="bodyMedium"),
                                    ft.ElevatedButton("Adicionar ao carrinho"),
                                ]
                            ),
                        ),
                        ft.Container(
                            width=200,
                            height=450,
                            padding=ft.padding.all(20),
                            border_radius=10,
                            bgcolor="white",
                            content=ft.Column(
                                controls=[
                                    ft.Image(
                                        "lan.jpg",
                                        width=150,
                                        height=180,
                                        fit="cover",
                                    ),
                                    ft.Text("Batata Frita Rústica", weight="bold"),
                                    ft.Text("R$ 29,99", style="bodyMedium"),
                                    ft.ElevatedButton("Adicionar ao carrinho"),
                                ]
                            ),
                        ),
                    
                ]
            )
        ]
    )
    elif aba == "Bebidas":
        return ft.Column(
            scroll=True,
            expand=True,
            controls=[
                ft.Row(
                    wrap=True,
                    controls=[
                        ft.Container(
                            width=200,
                            height=450,
                            padding=ft.padding.all(20),
                            border_radius=10,
                            bgcolor="white",
                            content=ft.Column(
                                controls=[
                                    ft.Text("Refrigerante", weight="bold"),
                                    ft.Text("R$ 5,00", style="bodyMedium"),
                                    ft.ElevatedButton("Adicionar ao carrinho"),
                                ]
                            ),
                        ),
                        ft.Container(
                            width=200,
                            height=450,
                            padding=ft.padding.all(20),
                            border_radius=10,
                            bgcolor="white",
                            content=ft.Column(
                                controls=[
                                    ft.Text("Suco de Laranja", weight="bold"),
                                    ft.Text("R$ 8,00", style="bodyMedium"),
                                    ft.ElevatedButton("Adicionar ao carrinho"),
                                ]
                            ),
                        ),
                    ]
                )
            ]
        )
def adicionar_ao_carrinho(page, produto):
    global carrinho
    carrinho.append(produto)
    print("Adicionando ao carrinho:", produto.nome)
    page.update()
def criar_carrinho(page):
    total = sum(produto.preco for produto in carrinho)
    produtos = ft.Column(
        controls=[ft.Text(f"{produto.nome} (R${produto.preco:.2f})", weight="bold") for produto in carrinho]
    )
    return ft.Column(
        controls=[
            ft.Text("Carrinho", text_align="center"),
            ft.Divider(),
            produtos,
            ft.Text(f"Total: R${total:.2f}", text_align="right"),
            ft.Row(
                controls=[
                    ft.ElevatedButton("Finalizar pedido", on_click=lambda e: fazer_pedido(page)),
                ]
            ),
        ]
    )
def atualizar_carrinho(page):
    page.controls[0].content = criar_carrinho(page)
    page.update() 

def fazer_pedido(page):
    print("Pedido enviado")
    carrinho_container = page.controls[0].content
    # criand as opções de pagamento
    opcoes_pagamento_container = criar_opcoes_pagamento(page)
    # adicionando as opcoes de pagamento ao container
    carrinho_container.controls.append(ft.Divider())
    carrinho_container.controls.append(ft.Text("Opções de Pagamento", text_align="center"))
    carrinho_container.controls.append(opcoes_pagamento_container)
    page.update()
class Pagamento:
    def __init__(self, nome, descricao):
        self.nome = nome
        self.descricao = descricao

opcoes_pagamento = [
    Pagamento("Cartão de Crédito", "Pagamento seguro via cartão"),
    Pagamento("Pix", "Pagamento instantâneo via Pix"),
    Pagamento("Dinheiro", "Pagamento em dinheiro na entrega"),
]   
    
ft.app(target=main)