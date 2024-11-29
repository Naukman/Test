import streamlit as st

# Titel und Beschreibung
st.title("Taschenrechner")
st.write("Ein einfacher Taschenrechner mit Streamlit.")

# Eingaben für die Zahlen
num1 = st.number_input("Erste Zahl eingeben:", value=0.0, format="%.2f")
num2 = st.number_input("Zweite Zahl eingeben:", value=0.0, format="%.2f")

# Auswahl der Operation
operation = st.radio(
    "Wähle die Operation:",
    ("Addition", "Subtraktion", "Multiplikation", "Division")
)

# Berechnung und Anzeige des Ergebnisses
if st.button("Berechnen"):
    if operation == "Addition":
        result = num1 + num2
        st.success(f"Das Ergebnis ist: {result}")
    elif operation == "Subtraktion":
        result = num1 - num2
        st.success(f"Das Ergebnis ist: {result}")
    elif operation == "Multiplikation":
        result = num1 * num2
        st.success(f"Das Ergebnis ist: {result}")
    elif operation == "Division":
        if num2 != 0:
            result = num1 / num2
            st.success(f"Das Ergebnis ist: {result}")
        else:
            st.error("Fehler: Division durch Null ist nicht erlaubt.")
          
