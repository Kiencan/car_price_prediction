import pandas as pd
import numpy as np
from pycaret.regression import *
from sklearn.metrics.pairwise import cosine_similarity

num_recommendations = 5

def predict_price_and_recommend(input_data, model, dataset):
    """
    Hàm dự đoán giá xe và trả về 5 mẫu xe tương tự.
    
    Args:
        model: Mô hình PyCaret đã huấn luyện.
        input_data: Dictionary chứa dữ liệu đầu vào của xe cần dự đoán.
        dataset: Dataset chứa các thông tin về xe (dùng để tìm xe tương tự).
        num_recommendations: Số lượng xe tương tự cần trả về (mặc định là 5).
    
    Returns:
        predicted_price: Giá xe dự đoán.
        recommendations: Danh sách 5 xe tương tự.
    """
    # Chuyển input_data thành DataFrame
    input_df = pd.DataFrame([input_data])

    # Dự đoán giá xe
    predicted_result = predict_model(model, data=input_df)
    predicted_price = predicted_result['prediction_label'].iloc[0]

    # Tìm xe tương tự dựa trên cosine similarity
    # Chuyển dataset phân loại sang dummy encoding để tính toán khoảng cách
    categorical_cols = ['ten_xe', 'xuat_xu', 'kieu_dang', 'hop_so', 
                        'mau_ngoai_that', 'mau_noi_that']
    encoded_dataset = pd.get_dummies(dataset[categorical_cols])
    encoded_input = pd.get_dummies(input_df[categorical_cols])
    
    # Đảm bảo các cột của encoded_input khớp với encoded_dataset
    encoded_input = encoded_input.reindex(columns=encoded_dataset.columns, fill_value=0)
    
    # Tính toán cosine similarity
    similarity_scores = cosine_similarity(encoded_input, encoded_dataset)
    
    # Lấy index của num_recommendations xe tương tự nhất
    similar_indices = np.argsort(similarity_scores[0])[-num_recommendations:][::-1]

    # Lấy thông tin của các xe tương tự
    recommendations = dataset.iloc[similar_indices]

    return predicted_price, recommendations

def loadModel():
    # Tải mô hình PyCaret từ file .pkl (giả sử mô hình được lưu dưới dạng .pkl)
    return load_model(r'D:/dulieu108/Đi làm/fastapi-dify-tool-template/app/services/car_pricing_model')

def load_dataset():
    # Tải dataset từ file JSON
    return pd.read_json(r'D:/dulieu108/Đi làm/fastapi-dify-tool-template/app/services/car_data.json')