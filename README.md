# How to run FastApi

Step 1: Install all dependencies:

Instead of using Poetry. I'm using pip

```
pip install -r requirements.txt
```

Step 2: Run local server

```
uvicorn app.web.application:app --reload
```

Note:

You should check the path of the file car_data.json and car_pricing_model.pkl in your `app/services/carservice.py`
