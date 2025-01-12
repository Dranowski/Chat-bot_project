import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model

# Загрузка модели
model = load_model('my_model.h5')

# Функция для предсказания
def predict(input_data):
    input_data = np.array(input_data).reshape(1, -1)  # Измените по необходимости в зависимости от вашей модели
    prediction = model.predict(input_data)
    return prediction


# Ввод данных пользователем
user_input = st.text_area("Введите текст для анализа:")

if st.button("Предсказать"):
    if user_input:
        # Преобразование входных данных в нужный формат
        input_data = [user_input]  # Если нужен другой формат, преобразуйте здесь
        result = predict(input_data)

        # Отображение результата
        st.write(f"Результат: {result}")
    else:
        st.warning("Пожалуйста, введите текст!")