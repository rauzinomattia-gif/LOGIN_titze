from fastapi import FastAPI, Form
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import pandas as pd

app = FastAPI()

df = pd.read_excel("/workspaces/LOGIN_titze/Foglio di lavoro senza nome.xlsx")

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/") # Endpoint: punto in cui andiamo a richiamare il server web
def home():
    # Restituisce direttamente il file HTML
    return FileResponse('static/index.html')

@app.post("/login")
def Controlla(username: str = Form(...), password: str = Form(...)):
    risultato = df[(df["USERNAME"] == username) & (df["PASSWORD"] == password)]
    if not risultato.empty:
        return {"messaggio": 1}
    else:
        return {"messaggio": 0}
