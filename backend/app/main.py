# backend/app/main.py
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Query, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, database
from typing import Optional
import logging
from .length_utils import *  # Import from utils

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

@app.get("/convert_value", status_code=200)
async def convert_value(
    convert_from: Optional[str] = Query(None, description="Unit to convert from (e.g., 'miles')"),
    convert_to: Optional[str] = Query(None, description="Unit to convert to (e.g., 'kms')"),
    source_value: Optional[float] = Query(None, description="Value to convert"),
    decimal_points: Optional[int] = Query(2, description="Value to convert")
):
    logging.info("Processing /convert_value request.")

    if not all([convert_from, convert_to, source_value is not None]):
        raise HTTPException(
            status_code=400,
            detail="Missing parameters. Please provide 'convert_from', 'convert_to', and 'source_value'."
        )
    try:
        # Type of conversion.
        # Decimal points.
        max_decimal_points = min(decimal_points, 17)
        target_value = convert_length(source_value, convert_from.lower(), convert_to.lower())
        return {
            "target_value": round(target_value, max_decimal_points)
        }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logging.error(f"Error processing request: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")


