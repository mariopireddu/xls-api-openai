
from fastapi import FastAPI, File, UploadFile
import pandas as pd
import io

app = FastAPI()

@app.post("/read-xls/")
async def read_xls(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        df = pd.read_excel(io.BytesIO(contents), engine="xlrd")
        return {"status": "success", "data": df.to_dict(orient="records")}
    except Exception as e:
        return {"status": "error", "message": str(e)}
