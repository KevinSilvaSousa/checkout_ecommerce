from fastapi import FastAPI
import os
from app.checkout.router import router as checkout_router
from dotenv import load_dotenv


app = FastAPI(title="Checkout Commerce", version="0.1.0")


app.include_router(checkout_router)

@app.get("/health")
async def health_check():
    payment_url = os.getenv("PAYMENT_SERVICE_URL")
    return {"status": payment_url}


if __name__ == "__main__":
    import uvicorn

    host = os.getenv("APP_HOST", "0.0.0.0")
    port = int(os.getenv("APP_PORT", 8005))
    uvicorn.run(app, host=host, port=port)


