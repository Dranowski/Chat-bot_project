import streamlit as st
import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model
from gigachat_api import get_access_token, send_prompt, get_image, sent_prompt_and_get_response

model = load_model('best_model.h5')

def analyse(input_data):
    result = model.analyse(input_data)
    return result

st.title("Чат бот")

if st.button("Что посмотреть?"):
    pass

if st.button("Выбрать любимые фильмы"):
    pass

if st.button("Анализ новости"):
    user_input = st.text_area("Введите новость для анализа >>> ")

    if user_input:
        input_data = [user_input]
        result = analyse(input_data)

        # Отображение результата
        st.write(f"Результат: {result}")
    else:
        st.warning("Пожалуйста, введите текст!")


# CLIENT_ID = st.secrets["CLIENT_ID"]
# SECRET = st.secrets["SECRET"]

if "access_token" not in st.session_state:
    try:
        st.session_state.access_token = get_access_token()
        st.toast("Получил токен")
    except Exception as e:
        st.toast(f"Не удалось получить токен: {e}")

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "ai", "content": "С чем вам помочь?"}]

for msg in st.session_state.messages:
    if msg.get("is_image"):
        st.chat_message(msg["role"]).image(msg["content"])
    else:
        st.chat_message(msg["role"]).write(msg["content"])

if user_prompt := st.chat_input():
    st.chat_message("user").write(user_prompt)
    st.session_state.messages.append({"role": "user", "content": user_prompt})

    with st.spinner("В процессе..."):
        movie_keywords = ['фильм', 'кино', 'просмотр', 'рекомендация', 'жанр', 'актёр', 'рейтинг']
        if any(keyword in user_prompt.lower() for keyword in movie_keywords):
            response, is_image = sent_prompt_and_get_response(user_prompt, st.session_state.access_token)
            if is_image:
                st.chat_message("ai").image(response)
                st.session_state.messages.append({"role": "ai", "content": response, "is_image": True})
            else:
                st.chat_message("ai").write(response)
                st.session_state.messages.append({"role": "ai", "content": response})
        else:
            st.toast("Это кино-бот. Спросите что-нибудь про кино")


