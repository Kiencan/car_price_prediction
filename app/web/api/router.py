from fastapi.responses import StreamingResponse
from fastapi.routing import APIRouter, HTTPException

from app.schemas.request_schema import Car
from app.utils.api_utils import make_response
# from app.web.api import echo, monitoring

from app.services.carservice import predict_price_and_recommend , load_dataset,loadModel
from fastapi.responses import JSONResponse

api_router = APIRouter()
# api_router.include_router(monitoring.router, prefix="/monitoring", tags=["monitoring"])
# api_router.include_router(echo.router, prefix="/echo", tags=["echo"])

@api_router.post("/predict_price")
async def predict_price(request: Car):
    model = loadModel()  
    dataset = load_dataset()  
    
    input_data = request.dict()
    predicted_price, recommendations = predict_price_and_recommend(input_data, model, dataset)
    print(predict_price)
    return JSONResponse({
        "predicted_price": predicted_price,
        "recommendations": recommendations.to_dict(orient="records")
    })