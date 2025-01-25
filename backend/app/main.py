from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Header, Query, Depends, HTTPException, Security
from sqlalchemy.orm import Session
from . import models, schemas, database
from typing import Optional
import logging
from .length_utils import *  # Import from utils
from .temperature_utils import *  # Import from utils
from .area_utils import *  # Import from utils
from fastapi.security.api_key import APIKeyHeader
import secrets

# Initialize the FastAPI app
app = FastAPI()

# Define the header name for the API key
VALID_API_KEYS = {"your-secret-key": "user1", "another-secret-key": "user2"}

# Define the APIKeyHeader security scheme
api_key_header = APIKeyHeader(name="Authorization", auto_error=False)

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
# models.Base.metadata.create_all(bind=database.engine)

# Dependency to validate the API key
async def get_api_key(api_key: str = Security(api_key_header)):
    print(f"Received API Key Header: {api_key}")  # Print the input value

    if not api_key:
        raise HTTPException(status_code=403, detail="Missing API Key")

    # Check if the header starts with "Bearer " and extract the token
    token = api_key[len("Bearer "):] if api_key.startswith("Bearer ") else api_key

    if token in VALID_API_KEYS:
        return token

    raise HTTPException(status_code=403, detail="Invalid API Key")

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

# Conversion endpoint
@app.get("/convert_value", status_code=200)
async def convert_value(
    _: str = Depends(get_api_key),  # Validate API key, but don't use it in the function
    convert_from: str = Query(None, description="Unit to convert from (e.g., 'mile')"),
    convert_to: str = Query(None, description="Unit to convert to (e.g., 'km')"),
    source_value: float = Query(None, description="Value to convert"),
    decimal_points: Optional[int] = Query(2, description="Optional. Defaults to 2. Value to convert")
):
    logging.info("Processing /convert_value request.")

    if not all([convert_from, convert_to, source_value is not None]):
        raise HTTPException(
            status_code=400,
            detail="Missing parameters. Please provide 'convert_from', 'convert_to', and 'source_value'."
        )
    try:
        # Decimal points.
        max_decimal_points = min(decimal_points, 17)
        # Type of conversion.
        target_value = None
        if LengthConverter.is_supported_conversion(convert_from, convert_to):
            target_value = LengthConverter.convert(source_value, convert_from, convert_to)
        elif TemperatureConverter.is_supported_conversion(convert_from, convert_to):
            target_value = TemperatureConverter.convert(source_value, convert_from, convert_to)
        elif AreaConverter.is_supported_conversion(convert_from, convert_to):
            target_value = AreaConverter.convert(source_value, convert_from, convert_to)
        response = {
            "result": round(target_value, max_decimal_points)
        }
        print(f"Returning response: {response}")  # Print the response to the console
        return response
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logging.error(f"Error processing request: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

# Endpoint to generate a secure HTTP key
@app.get("/generate_http_key", status_code=200)
async def generate_http_key(length: int = 32):
    """
    Generate a secure random key for HTTP use.

    :param length: The length of the key in bytes. Default is 32 bytes.
                   Must be between 16 and 64 bytes.
    :return: A hexadecimal string representation of the key.
    """
    if not (16 <= length <= 64):
        raise HTTPException(
            status_code=400,
            detail="Invalid length. Must be between 16 and 64 bytes."
        )
    key = secrets.token_hex(length)
    return {"key": key}
