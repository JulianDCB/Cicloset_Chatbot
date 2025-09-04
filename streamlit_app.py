import streamlit as st

st.title("💬 Chatbot Cicloset")
st.write("Chatbot de preguntas frecuentes y recomendaciones de bolsos.")

# Preguntas frecuentes y respuestas
faq = {
    "¿Cuáles son los métodos de pago?": "Aceptamos tarjetas de crédito, débito y pagos en efectivo.",
    "¿Hacen envíos a todo el país?": "Sí, realizamos envíos a toda Colombia.",
    "¿Cómo puedo rastrear mi pedido?": "Recibirás un correo con el enlace de rastreo después de tu compra.",
    "hola": "¡Hola! Bienvenido a Cicloset. ¿En qué puedo ayudarte hoy?",
    "buenos días": "¡Buenos días! Gracias por visitarnos. ¿Buscas algún bolso en especial?",
    "buenas tardes": "¡Buenas tardes! ¿Te gustaría ver nuestras recomendaciones de bolsos?",
    "buenas noches": "¡Buenas noches! Si tienes dudas sobre nuestros productos, estoy aquí para ayudarte.",
}

# Recomendaciones simples según gustos
def recomendar_bolso(gusto):
    if "deportivo" in gusto.lower():
        return "Te recomendamos el Bolso Deportivo Azul de Cicloset."
    elif "elegante" in gusto.lower():
        return "Te recomendamos el Bolso Elegante Negro de Cicloset."
    elif "casual" in gusto.lower():
        return "Te recomendamos el Bolso Casual Beige de Cicloset."
    else:
        return "Visita https://cicloset.com.co/ para ver todos nuestros bolsos y encuentra el que más te guste."

# Mensaje de bienvenida para nuevos usuarios
if "messages" not in st.session_state:
    st.session_state.messages = []
    st.session_state.messages.append({
        "role": "assistant",
        "content": "¡Bienvenido a Cicloset! 😊\n\nGracias por visitarnos. Si tienes alguna pregunta sobre nuestros bolsos o quieres una recomendación personalizada, escríbeme. También puedes visitar nuestra tienda en [cicloset.com.co](https://cicloset.com.co/)."
    })

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("¿En qué te puedo ayudar?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Respuesta automática
    respuesta = faq.get(prompt)
    if not respuesta:
        if "bolso" in prompt.lower() or "gusto" in prompt.lower():
            respuesta = recomendar_bolso(prompt)
        else:
            respuesta = "Lo siento, no entiendo tu pregunta. ¿Puedes reformularla? O visita nuestra tienda en [cicloset.com.co](https://cicloset.com.co/) para más información."

    with st.chat_message("assistant"):
        st.markdown(respuesta)
    st.session_state.messages.append({"role": "assistant", "content": respuesta})
