import uvicorn

from main import create_app

app = create_app()

if __name__ == "__main__":
    uvicorn.run("asgi:app", host="0.0.0.0", port=3000, reload=True)
