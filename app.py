import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Mi Primera App en Render", page_icon="🚀")

st.title("📈 Calculadora de Interés Compuesto")
st.write("¡Bienvenido! Esta es una app de Streamlit desplegada en Render.")

# Entradas del usuario
principal = st.number_input("Monto inicial ($)", min_value=0.0, value=1000.0, step=100.0)
tasa = st.number_input("Tasa de interés anual (%)", min_value=0.0, value=5.0, step=0.5)
anios = st.slider("Número de años", min_value=1, max_value=30, value=10)

# Cálculo
tasa_decimal = tasa / 100
monto_final = principal * ((1 + tasa_decimal) ** anios)
ganancia = monto_final - principal

# Resultado
st.subheader("Resultados")
col1, col2 = st.columns(2)
with col1:
    st.metric(label="Monto Final", value=f"${monto_final:,.2f}")
with col2:
    st.metric(label="Total Ganado", value=f"${ganancia:,.2f}")
    