from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import BigInteger, String, Numeric, SmallInteger, ForeignKey, Integer
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from decimal import Decimal
from typing import Optional, List

from database import Base

class Category(Base):
    __tablename__='categorys'
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(length=100))
    
    menu_items: Mapped[List['Menu_item']] = relationship(back_populates='categories')

class Menu_item(Base):
    __tablename__='menu_items'
    

    id: Mapped[int]=mapped_column(Integer, primary_key=True)
    name: Mapped[str]=mapped_column(String(length=500))
    price: Mapped[Decimal] = mapped_column(Numeric(precision=10, scale=2))
    description: Mapped[str] = mapped_column(String(length=500), nullable=True)
    
    category: Mapped[Optional[int]] = mapped_column(BigInteger, ForeignKey("categories.id"))
    categories: Mapped[Category] = relationship(back_populates='menu_items')

class Order(Base):
    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    address: Mapped[str] = mapped_column(String(500))
    total: Mapped[Decimal] = mapped_column(Numeric(12, 2))
    phone_number: Mapped[str] = mapped_column(String(20))
    status: Mapped[str] = mapped_column(String(50))
    
    order_items: Mapped[List['OrderItem']] = relationship(back_populates='orders')
    
class OrderItem(Base):
    __tablename__ = "order_items"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    menu_item: Mapped[int] = mapped_column(BigInteger, ForeignKey("menu_items.id"))
    
    quantity: Mapped[int] = mapped_column(SmallInteger) 
    
    total: Mapped[Decimal] = mapped_column(Numeric(12, 2))
    
    order: Mapped[Optional[int]] = mapped_column(BigInteger, ForeignKey("orders.id"), unique=True)
    orders: Mapped[Order] = relationship(back_populates='order_items')