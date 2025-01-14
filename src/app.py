import streamlit as st
from neuron import Neuron

st.title("¡Hola neurona! :sunglasses:")
st.write("Ahora podemos elegir la función de activación")
st.divider()

total_entradas = st.slider("Número de entradas y pesos que quieras aplicar", 1, 10, 1)

cols = st.columns(total_entradas)

for i in range(len(cols)):
    pesos = []
    entradas = []
    with cols[i]:
        pesos.append(st.slider("Ingresa el peso", 0.0, 5.0, 0.0, key=f"peso_{i}"))
        entradas.append(st.number_input("Ingresa la entrada", key=f"entrada_{i}"))

st.divider()

col1, col2 = st.columns(2)

with col1:
    b = st.number_input("Ingresa el sesgo")

with col2:
    func = st.selectbox("Selecciona la función de activación", ["sigmoide", "tanh", "relu", "binary_step"])

n = Neuron(pesos, b, str(func))

y = n.run(entradas)

if st.button("Calcular la salida"):
    st.write(f"La salida de la neurona es {y}")