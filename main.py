from fastapi import FastAPI
from accounts_pay_receive.routers import accounts_pay_receive_router
import asyncio
import uvicorn

app = FastAPI()

@app.get('/')
def hello():
    return "Hell-o world  teste"

#async def main():  
#    config = uvicorn.Config("main:app", port="8001", log_level="info")
#    server = uvicorn.Server(config)
#    await server.serve()

app.include_router(accounts_pay_receive_router.router)

if __name__ == "__main__":
    uvicorn.run("main:app", port="5000", log_level="info")
