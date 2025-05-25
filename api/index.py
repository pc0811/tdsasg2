from fastapi import FastAPI, Query, HTTPException
from fastapi.responses import JSONResponse

app = FastAPI()

# Mock database (replace with real data)
marks_db = {
    "X": 85,
    "Y": 92,
    "Alice": 78,
    "Bob": 88
}

@app.get("/api")
async def get_marks(names: list[str] = Query(..., alias="name")):
    try:
        result = []
        for name in names:
            if name in marks_db:
                result.append({"name": name, "mark": marks_db[name]})
            else:
                result.append({"name": name, "mark": None})
        
        return JSONResponse(content={"marks": result})
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
