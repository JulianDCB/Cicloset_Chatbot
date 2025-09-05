import streamlit as st
import time
import re

st.title("💬 Chatbot Cicloset")
st.write("Chatbot de preguntas frecuentes y recomendaciones de bolsos.")

# --- 1. Separar saludos y preguntas frecuentes en listas ---
saludos = [
    "hola", "buenos días", "buenas tardes", "buenas noches", "hola, ¿cómo estás?",
    "buen día", "qué tal", "hey", "holi", "saludos", "buenas", "qué onda", "hello"
]
respuestas_saludos = [
    "¡Hola! Bienvenido a Cicloset. ¿En qué puedo ayudarte hoy?",
    "¡Buenos días! Gracias por visitarnos. ¿Buscas algún bolso en especial?",
    "¡Buenas tardes! ¿Te gustaría ver nuestras recomendaciones de bolsos?",
    "¡Buenas noches! Si tienes dudas sobre nuestros productos, estoy aquí para ayudarte.",
    "¡Hola! Estoy muy bien, gracias por preguntar. ¿En qué puedo ayudarte hoy?",
    "¡Buen día! ¿Te gustaría ver nuestras novedades en bolsos?",
    "¡Qué tal! ¿Buscas algún bolso en particular?",
    "¡Hey! ¿Te ayudo a encontrar el bolso perfecto?",
    "¡Holi! ¿Quieres una recomendación de bolso?",
    "¡Saludos! ¿En qué puedo ayudarte?",
    "¡Buenas! ¿Buscas algo especial?",
    "¡Qué onda! ¿Te gustaría ver nuestras colecciones?",
    "¡Hello! ¿Te ayudo a elegir un bolso?"
]

preguntas_frecuentes = [
    "¿Cuáles son los métodos de pago?",
    "¿Hacen envíos a todo el país?",
    "¿Cómo puedo rastrear mi pedido?",
    "¿Puedo cambiar o devolver un producto?",
    "¿Cuánto tarda el envío?",
    "¿Tienen garantía los productos?",
    "¿Dónde están ubicados?"
]
respuestas_faq = [
    "Aceptamos tarjetas de crédito, débito y pagos en efectivo.",
    "Sí, realizamos envíos a toda Colombia.",
    "Recibirás un correo con el enlace de rastreo después de tu compra.",
    "Sí, puedes cambiar o devolver tu producto dentro de los 30 días posteriores a la compra.",
    "El envío tarda entre 2 y 5 días hábiles dependiendo de tu ubicación.",
    "Sí, todos nuestros productos tienen garantía de 6 meses por defectos de fábrica.",
    "Nuestra tienda es 100% online, pero puedes contactarnos para más información."
]

# --- 2. Función para normalizar texto (quitar tildes, mayúsculas, espacios y signos) ---
def normalizar(texto):
    texto = texto.lower()
    texto = re.sub(r'[áàäâ]', 'a', texto)
    texto = re.sub(r'[éèëê]', 'e', texto)
    texto = re.sub(r'[íìïî]', 'i', texto)
    texto = re.sub(r'[óòöô]', 'o', texto)
    texto = re.sub(r'[úùüû]', 'u', texto)
    texto = re.sub(r'[^a-z0-9 ]', '', texto)
    texto = re.sub(r'\s+', ' ', texto).strip()
    return texto

# --- 3. Recomendaciones mejoradas por gustos, colores, marcas, estilos, ocasiones ---
def recomendar_bolso(gusto):
    gusto_norm = normalizar(gusto)
    # Colores
    colores = {
        "rojo": "Bolso Rojo Pasión",
        "azul": "Bolso Deportivo Azul",
        "negro": "Bolso Elegante Negro",
        "beige": "Bolso Casual Beige",
        "verde": "Bolso Verde Primavera",
        "blanco": "Bolso Blanco Clásico"
    }
    for color, nombre in colores.items():
        if color in gusto_norm:
            return f"Te recomendamos el {nombre} de Cicloset. ¡Es ideal para quienes aman el color {color}!"

    # Marcas
    if "louis vuitton" in gusto_norm:
        return "Tenemos bolsos inspirados en el estilo de Louis Vuitton. ¿Te gustaría verlos?"
    if "carolina herrera" in gusto_norm:
        return "Nuestros bolsos tipo Carolina Herrera son perfectos para un look elegante y sofisticado."
    if "prada" in gusto_norm:
        return "Nuestros bolsos tipo Prada son sinónimo de lujo y estilo. ¿Te gustaría verlos?"

    # Estilos
    if "deportivo" in gusto_norm:
        return "Te recomendamos el Bolso Deportivo Azul de Cicloset."
    if "elegante" in gusto_norm:
        return "Te recomendamos el Bolso Elegante Negro de Cicloset."
    if "casual" in gusto_norm:
        return "Te recomendamos el Bolso Casual Beige de Cicloset."
    if "formal" in gusto_norm:
        return "El Bolso Formal Negro es perfecto para eventos importantes."
    if "juvenil" in gusto_norm:
        return "El Bolso Juvenil Rosa es ideal para un look fresco y moderno."

    # Ocasiones especiales
    if "boda" in gusto_norm or "bautizo" in gusto_norm or "fiesta" in gusto_norm:
        return "Para ocasiones especiales como bodas o bautizos, te sugerimos el Bolso de Fiesta Plateado de Cicloset."
    if "trabajo" in gusto_norm:
        return "El Bolso Ejecutivo Negro es ideal para el trabajo y reuniones de negocios."
    if "universidad" in gusto_norm or "clases" in gusto_norm:
        return "El Bolso Mochila Cicloset es perfecto para la universidad o clases."

    return "Visita https://cicloset.com.co/ para ver todos nuestros bolsos y encuentra el que más te guste."

# --- 4. Mensaje de bienvenida para nuevos usuarios ---
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

    # --- 5. Procesar la entrada del usuario ---
    prompt_norm = normalizar(prompt)
    respuesta = None

    # Buscar saludo
    for i, saludo in enumerate(saludos):
        if normalizar(saludo) == prompt_norm:
            respuesta = respuestas_saludos[i]
            break

    # Buscar pregunta frecuente si no es saludo
    if respuesta is None:
        for i, pregunta in enumerate(preguntas_frecuentes):
            if normalizar(pregunta) == prompt_norm:
                respuesta = respuestas_faq[i]
                break

    # Buscar recomendación por gustos si no es saludo ni FAQ
    if respuesta is None:
        if any(palabra in prompt_norm for palabra in ["bolso", "gusto", "color", "marca", "estilo", "ocasion", "boda", "bautizo", "fiesta", "trabajo", "universidad", "clases"]):
            respuesta = recomendar_bolso(prompt)
        else:
            respuesta = "Lo siento, no entiendo tu pregunta. ¿Puedes reformularla? O visita nuestra tienda en [cicloset.com.co](https://cicloset.com.co/) para más información."

    # --- 6. Esperar entre 1 y 1.5 segundos antes de responder ---
    time.sleep(1.2)

    # --- 7. Añadir seguimiento a la respuesta ---
    respuesta += "\n\n¿Te puedo ayudar en algo más?"

    with st.chat_message("assistant"):
        st.markdown(respuesta)
    st.session_state.messages.append({"role": "assistant", "content": respuesta})
