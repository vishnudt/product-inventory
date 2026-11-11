from fastapi import FastAPI, Request, Depends, Form
from sqlalchemy.orm import Session
from database import Base, SessionLocal, engine
from models import Products
from fastapi.templating import Jinja2Templates

app = FastAPI()
Base.metadata.create_all(bind=engine)

template = Jinja2Templates(directory="templates")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def form(
    request : Request
):
    return template.TemplateResponse(
        request=request,
        name="product_add.html"
    )

@app.get("list-product/")
def list_product(
    request : Request,
    db : Session = Depends(get_db)
):
    products = db.query(Products).all()

    return template.TemplateResponse(
        request=request,
        name="",
        context={
            "products" : products
        }
        
    )



@app.post("/save")
def add_product(
    request : Request,
    title : str = Form(),
    price : str =  Form(),
    quantity : int = Form(),
    db : Session = Depends(get_db)
):
    product = Products(
        title = title,
        price = price,
        quantity = quantity
    )
    db.add(product)
    db.commit()
    db.refresh(product)

    return {
        "message" : "added"
    }




