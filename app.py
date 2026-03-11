
import streamlit as st

def calcular_porcentaje(valor, porcentaje=16):
    return valor * porcentaje / 100

def main():
    st.set_page_config(page_title="Calculadora de Porcentaje", page_icon="📊", layout="centered")
    st.title("Calculadora del 16%")
    st.write("Ingresa un número y el resultado se mostrará automáticamente.")

    with st.form(key="input_form"):
        numero = st.number_input("Escribe un número:", min_value=0.0, step=1.0, format="%.2f")
        submit = st.form_submit_button("Ingresar")

    if numero > 0:
        resultado = calcular_porcentaje(numero)
        st.info(f"El 16% de {numero:.2f} es {resultado:.2f}")
    elif numero == 0:
        st.warning("Por favor ingresa un número mayor a cero.")

if __name__ == "__main__":
    main()
