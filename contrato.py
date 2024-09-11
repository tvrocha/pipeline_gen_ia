from datetime import datetime
from typing import Tuple
from pydantic import BaseModel, EmailStr, PositiveFloat, PositiveInt
from enum import Enum


class ProdutoEnum(str, Enum):
    produto1 = "Loja Física"
    produto2 = "Loja Online"
    produto3 = "Terceiros"


class Vendas(BaseModel):
    """
    
    Modelo de dados para as vendas

    Args:
        email (EmailStr): email do vendedor
        data (datetime): data da compra
        valor (PositiveFloat): valor da compra
        qtde (PositiveInt): quantidade de vendas
        produto (ProdutoEnum): categoria da venda

    """


    email: EmailStr
    data: datetime
    valor: PositiveFloat
    qtde: PositiveInt
    produto: ProdutoEnum

    def __str__(self):
        return (
            f"Venda realizada por: {self.email}\n"
            f"Data: {self.data.strftime('%Y-%m-%d %H:%M:%S')}\n"
            f"Valor: R${self.valor:.2f}\n"
            f"Quantidade: {self.qtde}\n"
            f"Produto: {self.produto.value}"
        )

