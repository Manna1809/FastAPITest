from fastapi import FASTAPI

app=FASTAPI()




@app.get("/")
def home():
    return {"message":"Hello TutLinks.com"}
