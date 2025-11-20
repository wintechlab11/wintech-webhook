from fastapi import FastAPI, Request
from pydantic import BaseModel
import uvicorn

app = FastAPI()

class WebhookData(BaseModel):
    pair: str
    direction: str
    price: float
    strategy: str
    time: str

@app.post("/webhook")
async def receive_webhook(request: WebhookData):
    print(f"Получен сигнал: {request.pair} {request.direction} по цене {request.price}")
    # Здесь твоя логика: считать SL/TP, отправить в cTrader/Bybit
    # Пока просто возвращаем OK
    return {"status": "received", "message": "Сигнал обработан"}

@app.get("/healthz")
def health():
    return {"status": "alive"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
