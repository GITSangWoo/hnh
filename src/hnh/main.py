from typing import Union,Annotated
from transformers import pipeline
from fastapi import FastAPI , File, UploadFile
from fastapi.templating import Jinja2Templates
from fastapi import Request
import random

app = FastAPI()

html = Jinja2Templates(directory="public")

@app.get("/hello")
def read_root():
    return {"Hello": "World"}

@app.get("/")
async def home(request: Request):
    hotdog = "https://encrypted-tbn3.gstatic.com/shopping?q=tbn:ANd9GcQweb_7o7OrtlTP75oX2Q_keaoVYgAhMsYVp1sCafoNEdtSSaHps3n7NtNZwT_ufZGPyH7_9MFcao_r8QWr3Fdz17RitvZXLTU4dNsxr73m6V1scsH3_ZZHRw&usqp=CAE"
    dog = "https://hearingsense.com.au/wp-content/uploads/2022/01/8-Fun-Facts-About-Your-Dog-s-Ears-1024x512.webp"
    image_url = random.choice([hotdog, dog])
    

    return html.TemplateResponse("index.html",{"request":request, "image_url": image_url})
    
@app.get("/hot dog")
def hotdog():
    model = pipeline("image-classification", model="julien-c/hotdog-not-hotdog")
    
    return { "pred" : random.choice(["hotdog","not hotdog"])}

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile,request: Request):
    # 파일 저장 
    img = await file.read()
    model = pipeline("image-classification", model="julien-c/hotdog-not-hotdog")
    from PIL import Image
    import io
    img = Image.open(io.BytesIO(img)) # 이미지 바이트를 PIL 이미지로 변환
    # if p 값이 배열과 같이 나오면 높은  확률의 값을 추출해서 리턴하기    
    
    p = model(img)

    result = max(p, key=lambda x: x["score"])  
    
    if result['score'] >= 0.8 :
        label = "hot dog"
    else :
        label = "not hot dog" 


    return  {'label':label,'result':result}
