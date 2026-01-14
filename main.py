import uvicorn

if __name__ == "__main__":
    uvicorn.run("src.app:app", host="localhost", port=8800, reload=True)
