# backend/app/main.py
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Query, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, database
from typing import Optional
import logging
from .utils import miles_to_kms  # Import from utils

# Initialize the FastAPI app
app = FastAPI()

# Allow frontend to access backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Logging setup
logging.basicConfig(level=logging.INFO)

# Create the database tables
#models.Base.metadata.create_all(bind=database.engine)

# Endpoint to create an item
@app.post("/items/", response_model=schemas.ItemResponse)
def create_item(item: schemas.ItemCreate, db: Session = Depends(database.get_db)):
    db_item = models.Item(name=item.name, description=item.description, price=item.price)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

# Endpoint to get all items
@app.get("/items/", response_model=list[schemas.ItemResponse])
def read_items(db: Session = Depends(database.get_db)):
    return db.query(models.Item).all()


@app.get("/http_convert")
async def http_convert(name: Optional[str] = Query(None, description="Name to greet")):
    """
    Greet the user with a name if provided, otherwise return a generic message.
    """
    logging.info("Processing /http_convert request.")

    if name:
        return f"Hello, {name}. This HTTP triggered function executed successfully."
    else:
        return (
            "This HTTP triggered function executed successfully. "
            "Pass a name in the query string or in the request body for a personalized response."
        )

@app.get("/convert_value")
async def convert_value(
    convert_from: Optional[str] = Query(None, description="Unit to convert from (e.g., 'miles')"),
    convert_to: Optional[str] = Query(None, description="Unit to convert to (e.g., 'kms')"),
    source_value: Optional[float] = Query(None, description="Value to convert")
):
    logging.info("Processing /convert_value request.")

    if not all([convert_from, convert_to, source_value is not None]):
        raise HTTPException(
            status_code=400,
            detail="Missing parameters. Please provide 'convert_from', 'convert_to', and 'source_value'."
        )

    if convert_from.lower() == "miles" and convert_to.lower() == "kms":
        target_value = miles_to_kms(source_value)
        return f"{source_value} miles is equal to {target_value:.2f} kilometers."
    else:
        raise HTTPException(
            status_code=400,
            detail="Unsupported conversion. Only miles to kilometers is supported."
        )

