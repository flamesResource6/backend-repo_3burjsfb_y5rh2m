import os
from typing import List, Optional
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(title="VRO API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ----- Models -----
class Product(BaseModel):
    id: str
    title: str
    image: str
    price: Optional[float] = None
    tag: Optional[str] = None
    category: Optional[str] = None


class Tile(BaseModel):
    id: str
    title: str
    subtitle: Optional[str] = None
    image: str
    tag: Optional[str] = None
    category: Optional[str] = None


class RoutineItem(BaseModel):
    id: str
    title: str
    image: str
    time: Optional[str] = None


# ----- Sample Catalog Data (static for homepage) -----
RECOMMENDS: List[Product] = [
    Product(id="rec-1", title="Minimal Leather Wallet", image="https://images.unsplash.com/photo-1613490493576-7fde63acd811?w=1200&q=80&auto=format&fit=crop", price=39.0, tag="Essentials", category="VRO Essentials"),
    Product(id="rec-2", title="Classic Chronograph Watch", image="https://images.unsplash.com/photo-1524805444758-089113d48a6d?w=1200&q=80&auto=format&fit=crop", price=149.0, tag="Watches", category="Fashion & Lifestyle"),
    Product(id="rec-3", title="Premium Running Shoes", image="https://images.unsplash.com/photo-1608231387042-66d1773070a5?w=1200&q=80&auto=format&fit=crop", price=89.0, tag="Shoes", category="Fashion & Lifestyle"),
    Product(id="rec-4", title="Noise Cancelling Headphones", image="https://images.unsplash.com/photo-1518443952243-9e5aef4fbf38?w=1200&q=80&auto=format&fit=crop", price=199.0, tag="Tech", category="Tech & Gadgets"),
    Product(id="rec-5", title="Athleisure Hoodie", image="https://images.unsplash.com/photo-1540575467063-178a50c2df87?w=1200&q=80&auto=format&fit=crop", price=59.0, tag="Athleisure", category="Sports & Nutrition"),
    Product(id="rec-6", title="Grooming Kit Pro", image="https://images.unsplash.com/photo-1598440947619-2c35fc9aa908?w=1200&q=80&auto=format&fit=crop", price=79.0, tag="Grooming", category="Grooming & Care"),
]

TRANSFORM: List[Tile] = [
    Tile(id="tr-1", title="Lose Weight", subtitle="Calorie control & fat burn", image="https://images.unsplash.com/photo-1517963628607-235ccdd5476c?w=1400&q=80&auto=format&fit=crop", tag="Programs", category="Health & Nutrition"),
    Tile(id="tr-2", title="Gain Weight", subtitle="High-calorie clean bulk", image="https://images.unsplash.com/photo-1517836357463-d25dfeac3438?w=1400&q=80&auto=format&fit=crop", tag="Programs", category="Health & Nutrition"),
    Tile(id="tr-3", title="Build Strength", subtitle="Progressive overload", image="https://images.unsplash.com/photo-1526401485004-2fda9f4b5c4f?w=1400&q=80&auto=format&fit=crop", tag="Programs", category="Health & Nutrition"),
    Tile(id="tr-4", title="Improve Recovery", subtitle="Mobility & rest", image="https://images.unsplash.com/photo-1599058917212-d750089bc07e?w=1400&q=80&auto=format&fit=crop", tag="Programs", category="Health & Nutrition"),
]

CONCERNS: List[Tile] = [
    Tile(id="c-1", title="Acne Control", image="https://images.unsplash.com/photo-1556228578-8c89e362d2b5?w=1200&q=80&auto=format&fit=crop", category="Grooming & Care"),
    Tile(id="c-2", title="Oil Control", image="https://images.unsplash.com/photo-1522335789203-aabd1fc54bc9?w=1200&q=80&auto=format&fit=crop", category="Grooming & Care"),
    Tile(id="c-3", title="Anti Aging", image="https://images.unsplash.com/photo-1596755094514-f87e9b9cf1e9?w=1200&q=80&auto=format&fit=crop", category="Grooming & Care"),
    Tile(id="c-4", title="Dark Circles", image="https://images.unsplash.com/photo-1519415943484-9fa8a8f4d2f5?w=1200&q=80&auto=format&fit=crop", category="Grooming & Care"),
]

ROUTINE: List[RoutineItem] = [
    RoutineItem(id="r-1", title="Electric Toothbrush", image="https://images.unsplash.com/photo-1609840114035-7d661c181214?w=1200&q=80&auto=format&fit=crop", time="Morning"),
    RoutineItem(id="r-2", title="Trimmer", image="https://images.unsplash.com/photo-1540910419892-4a36d2c6a740?w=1200&q=80&auto=format&fit=crop", time="Anytime"),
    RoutineItem(id="r-3", title="Face Wash", image="https://images.unsplash.com/photo-1585577529540-a8096a7d4a15?w=1200&q=80&auto=format&fit=crop", time="Morning"),
    RoutineItem(id="r-4", title="Shampoo", image="https://images.unsplash.com/photo-1582095133179-bfd08e2fc6b3?w=1200&q=80&auto=format&fit=crop", time="Shower"),
    RoutineItem(id="r-5", title="Hair Brush", image="https://images.unsplash.com/photo-1616394584738-fc6e6122fd10?w=1200&q=80&auto=format&fit=crop", time="Anytime"),
    RoutineItem(id="r-6", title="Hair Dryer", image="https://images.unsplash.com/photo-1522335789203-aabd1fc54bc9?w=1200&q=80&auto=format&fit=crop", time="Morning"),
    RoutineItem(id="r-7", title="Sunscreen", image="https://images.unsplash.com/photo-1585238342028-4bbc0eac2c6f?w=1200&q=80&auto=format&fit=crop", time="Day"),
    RoutineItem(id="r-8", title="Sunglasses", image="https://images.unsplash.com/photo-1519681393784-d120267933ba?w=1200&q=80&auto=format&fit=crop", time="Day"),
]


@app.get("/")
def read_root():
    return {"message": "VRO Backend Running"}


@app.get("/api/hello")
def hello():
    return {"message": "Hello from the backend API!"}


@app.get("/api/recommendations", response_model=List[Product])
def get_recommendations(limit: int = Query(12, ge=1, le=24)):
    return RECOMMENDS[:limit]


@app.get("/api/transform", response_model=List[Tile])
def get_transform_tiles():
    return TRANSFORM


@app.get("/api/concerns", response_model=List[Tile])
def get_concerns():
    return CONCERNS


@app.get("/api/routines", response_model=List[RoutineItem])
def get_routines():
    return ROUTINE


@app.get("/api/search", response_model=List[Product])
def search(q: str = Query("", description="Search query")):
    """Simple text search across recommended items. In a full app this would query a DB or search service."""
    ql = q.lower().strip()
    if not ql:
        return RECOMMENDS
    results = []
    for p in RECOMMENDS:
        hay = f"{p.title} {p.tag or ''} {p.category or ''}".lower()
        if ql in hay:
            results.append(p)
    return results


@app.get("/test")
def test_database():
    """Test endpoint to check if environment variables for database are present"""
    response = {
        "backend": "✅ Running",
        "database": "❌ Not Connected",
        "database_url": "✅ Set" if os.getenv("DATABASE_URL") else "❌ Not Set",
        "database_name": "✅ Set" if os.getenv("DATABASE_NAME") else "❌ Not Set",
        "connection_status": "Not Connected",
        "collections": []
    }
    return response


if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
