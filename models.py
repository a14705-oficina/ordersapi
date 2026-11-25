from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Boolean, Float
from sqlalchemy.ext.declarative import declarative_base

db = create_engine('sqlite://pizzaria.db') # Base de dados SQLite
Base = declarative_base() # Classe base para os modelos

class User(Base):
    __tablename__ = 'users' # Nome da tabela
    id = Column("id",Integer, primary_key=True, autoincrement=True) # Coluna de ID do usuário
    name = Column("name",String)
    email = Column("email",String)
    password = Column("password",String, nullable=False) # Preenchimento obrigatório
    active = Column("active",Boolean)
    admin = Column("admin",Boolean, default=False)

    def __init__(self, name, email, password, active=True, admin=False):
        self.name = name
        self.email = email
        self.password = password
        self.active = active
        self.admin = admin

class Order(Base):
    __tablename__ = 'orders' # Nome da tabela
    id = Column("id",Integer, primary_key=True, autoincrement=True)
    user = Column("user",Integer, ForeignKey('users.id')) # Chave estrangeira para a tabela do User
    status = Column("status",String, nullable=False) # Status do pedido
    price = Column("price",Float)
    # Items = Column("items",String)

    def __init__(self, user, status="pending", price=0):
        self.user = user
        self.status = status
        self.price = price

class OrderItems(Base):
    __tablename__ = 'order_items' # Nome da tabela
    id = Column("id",Integer, primary_key=True, autoincrement=True)
    quantity = Column("quantity",Integer, nullable=False) # Quantidade do item
    flavour = Column("flavour",String) # Nome do item
    size = Column("size",String, nullable=False) # Tamanho do item
    unit_price = Column("unit_price",Float)
    order = Column("order",Integer, ForeignKey('orders.id'))

    def __init__(self, quantity, flavour, size, unit_price, order):
        self.quantity = quantity
        self.flavour = flavour
        self.size = size
        self.unit_price = unit_price    
        self.order = order