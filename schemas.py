from pydantic import BaseModel, Field
from decimal import Decimal
from typing import Optional

class CategoryBase(BaseModel):
    name: str = Field(max_length=100)
    
class CategoryCreate(CategoryBase):
    pass

class CategoryOut(CategoryBase):
    id: int

class CategoryUpdate(BaseModel):
    pass
    
    
         
  
class MenuItemBase(BaseModel):
    name: str = Field(max_length=100)
    price: Decimal = Field(..., gt=0, max_digits=10, decimal_places=2)
    description: str = Field(max_length=500)
    category: Optional[int] = None

class MenuItemCreate(MenuItemBase):
    pass

class MenuItemOut(MenuItemBase):
    id: int

class MenuItemUpdate(BaseModel):
    pass
        
  
   



class OrderItemBase(BaseModel):
    menu_item: int
    quantity: int = Field(...,  gt=0, le=500) 
    total: Decimal = Field(..., gt=0, max_digits=10, decimal_places=2)
    order: Optional[int] = None

class OrderItemCreate(OrderItemBase):
    pass

class OrderItemUpdate(BaseModel):
    pass

class OrderItemOut(OrderItemBase):
    id: int
    
  

class OrderBase(BaseModel):
    address: str = Field(max_length=500)
    total: Decimal = Field(..., gt=0, max_digits=10, decimal_places=2)
    phone_number: str = Field(max_length=20)
    status: str = Field(max_length=50)

class OrderCreate(OrderBase):
    pass

class OrderUpdate(BaseModel):
    pass

class OrderOut(OrderBase):
    id: int
    order_items: list[OrderItemOut] = []   

    
  

