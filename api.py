from typing import List

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session
from schemas import CategoryCreate, CategoryOut, CategoryUpdate, MenuItemCreate,MenuItemUpdate, MenuItemOut, OrderItemCreate, OrderItemUpdate, OrderItemOut, OrderCreate, OrderUpdate, OrderOut
from database import Base, get_db, engine
from models import Category, MenuItem, Order, OrderItem


Base.metadata.create_all(bind=engine)
api_router = APIRouter(prefix='/api/res')

#          Category

@api_router.post('/categories', response_model=CategoryOut)
def create_category(category_in: CategoryCreate, db: Session = Depends(get_db)):
    category = Category(**category_in.model_dump())
    
    db.add(category)
    db.commit()
    db.refresh(category)
    
    return category

@api_router.get('/categories', response_model=List[CategoryOut])
def get_categories(db: Session = Depends(get_db)):
    stmt = select(Category)
    categories = db.scalars(stmt).all()
    
    return categories

@api_router.get("/categories/{category_id}", response_model=CategoryOut)
def get_category(category_id: int, db: Session = Depends(get_db)):
    stmt = select(Category).where(Category.id == category_id)
    category = db.scalar(stmt)
    
    if not category:
        raise HTTPException(status_code=404, detail=f"{category_id} - raqamli category mavjud emas")
    return category

@api_router.put('/categories/{category_id}', response_model=CategoryOut)
def update_category(category_id: int, category_in: CategoryUpdate, db: Session = Depends(get_db)):
    stmt = select(Category).where(Category.id == category_id)
    category: CategoryOut = db.scalar(stmt)
    
    if not category:
        raise HTTPException(status_code=404, detail=f"{category_id} - raqamli category mavjud emas")
    
    category.name = category_in.name
    
    db.add(category)
    db.commit()
    db.refresh(category)
    
    return category

@api_router.delete('/categories/{category_id}', status_code=204)
def delete_category(category_id: int, db: Session = Depends(get_db)):
    stmt = select(Category).where(Category.id == category_id)
    category = db.scalar(stmt)
    
    if not category:
        raise HTTPException(status_code=404, detail=f"{category_id} - raqamli category mavjud emas")
    db.delete(category)
    db.commit()
    
    return



#              MenuItem

@api_router.post('/menu_items', response_model=MenuItemOut)
def create_menu_item(menu_item_in: MenuItemCreate, db: Session = Depends(get_db)):
    menu_item = MenuItem(**menu_item_in.model_dump())
    
    db.add(menu_item)
    db.commit()
    db.refresh(menu_item)
    
    return menu_item

@api_router.get('/menu_items', response_model=List[MenuItemOut])
def get_menu_items(db: Session = Depends(get_db)):
    stmt = select(MenuItem)
    menu_items = db.scalars(stmt).all()
    
    return menu_items

@api_router.get("/menu_items/{menu_item_id}", response_model=MenuItemOut)
def get_MenuItem(menu_item_id: int, db: Session = Depends(get_db)):
    stmt = select(MenuItem).where(MenuItem.id == menu_item_id)
    menu_item = db.scalar(stmt)
    
    if not menu_item:
        raise HTTPException(status_code=404, detail=f"{menu_item_id} - raqamli menu_item mavjud emas")
    return menu_item

@api_router.put('/menu_items/{menu_item_id}', response_model=MenuItemOut)
def update_menu_item(menu_item_id: int, menu_item_in: MenuItemUpdate, db: Session = Depends(get_db)):
    stmt = select(MenuItem).where(MenuItem.id == menu_item_id)
    menu_item: MenuItemOut = db.scalar(stmt)
    
    if not menu_item:
        raise HTTPException(status_code=404, detail=f"{menu_item_id} - raqamli menu_item mavjud emas")
    
    menu_item.name = menu_item_in.name
    menu_item.price = menu_item_in.price
    menu_item.description = menu_item_in.description
    
    
    db.add(menu_item)
    db.commit()
    db.refresh(menu_item)
    
    return menu_item

@api_router.delete('/menu_item/{menu_item_id}', status_code=204)
def delete_menu_item(menu_item_id: int, db: Session = Depends(get_db)):
    stmt = select(MenuItem).where(MenuItem.id == menu_item_id)
    menu_item = db.scalar(stmt)
    
    if not menu_item:
        raise HTTPException(status_code=404, detail=f"{menu_item_id} - raqamli menu_item mavjud emas")
    db.delete(menu_item)
    db.commit()
    
    return


#          Order

@api_router.post('/orders', response_model=OrderOut)
def create_order(order_in: OrderCreate, db: Session = Depends(get_db)):
    order = Order(**order_in.model_dump())
    db.add(order)
    db.commit()
    db.refresh(order)
    return order


@api_router.get('/orders', response_model=List[OrderOut])
def get_orders(db: Session = Depends(get_db)):
    stmt = select(Order)
    orders = db.scalars(stmt).all()
    return orders


@api_router.get('/orders/{order_id}', response_model=OrderOut)
def get_order(order_id: int, db: Session = Depends(get_db)):
    stmt = select(Order).where(Order.id == order_id)
    order = db.scalar(stmt)
    if not order:
        raise HTTPException(status_code=404, detail=f"{order_id} - raqamli order mavjud emas")
    return order


@api_router.put('/orders/{order_id}', response_model=OrderOut)
def update_order(order_id: int, order_in: OrderUpdate, db: Session = Depends(get_db)):
    stmt = select(Order).where(Order.id == order_id)
    order = db.scalar(stmt)
    
    if not order:
        raise HTTPException(status_code=404, detail=f"{order_id} - raqamli order mavjud emas")
    
    order.address = order_in.address
    order.total = order_in.total
    order.phone_number = order_in.phone_number
    order.status = order_in.status
    
    db.commit()
    db.refresh(order)
    
    return order


@api_router.delete('/orders/{order_id}', status_code=204)
def delete_order(order_id: int, db: Session = Depends(get_db)):
    stmt = select(Order).where(Order.id == order_id)
    order = db.scalar(stmt)
    
    if not order:
        raise HTTPException(status_code=404, detail=f"{order_id} - raqamli order mavjud emas")
    
    db.delete(order)
    db.commit()
    
    return


#               OrderItem 

@api_router.post('/order_items', response_model=OrderItemOut)
def create_order_item(order_item_in: OrderItemCreate, db: Session = Depends(get_db)):
    order_item = OrderItem(**order_item_in.model_dump())
    
    db.add(order_item)
    db.commit()
    db.refresh(order_item)
    
    return order_item


@api_router.get('/order_items', response_model=List[OrderItemOut])
def get_order_items(db: Session = Depends(get_db)):
    stmt = select(OrderItem)
    order_items = db.scalars(stmt).all()
    
    return order_items


@api_router.get('/order_items/{order_item_id}', response_model=OrderItemOut)
def get_order_item(order_item_id: int, db: Session = Depends(get_db)):
    stmt = select(OrderItem).where(OrderItem.id == order_item_id)
    order_item = db.scalar(stmt)
    
    if not order_item:
        raise HTTPException(status_code=404, detail=f"{order_item_id} - raqamli order_item mavjud emas")
    
    return order_item


@api_router.put('/order_items/{order_item_id}', response_model=OrderItemOut)
def update_order_item(order_item_id: int, order_item_in: OrderItemUpdate, db: Session = Depends(get_db)):
    stmt = select(OrderItem).where(OrderItem.id == order_item_id)
    order_item = db.scalar(stmt)
    
    if not order_item:
        raise HTTPException(status_code=404, detail=f"{order_item_id} - raqamli order_item mavjud emas")
    
    order_item.menu_item = order_item_in.menu_item
    order_item.quantity = order_item_in.quantity
    order_item.total = order_item_in.total
    order_item.order = order_item_in.order
    
    db.add(order_item)
    db.commit()
    db.refresh(order_item)
    
    return order_item


@api_router.delete('/order_items/{order_item_id}', status_code=204)
def delete_order_item(order_item_id: int, db: Session = Depends(get_db)):
    stmt = select(OrderItem).where(OrderItem.id == order_item_id)
    order_item = db.scalar(stmt)
    
    if not order_item:
        raise HTTPException(status_code=404, detail=f"{order_item_id} - raqamli order_item mavjud emas")
    
    db.delete(order_item)
    db.commit()
    
    return
