import streamlit as st
import pandas as pd
import altair as alt

st.header("Die meisten Internetnutzer finden den Umgang im Web respektlos")
st.subheader("Internet für 90% der Nutzer respektloser Raum")

source = pd.DataFrame({
        'Anteil': [42, 42, 12, 10],
        'Top 4 Gründe dafür': ['Anonymität', 'Kein persönlicher Kontakt', 'Geringe Hemmschwellen', 'keine Konsequenzen zu befürchten']
     })
 
bar_chart = alt.Chart(source).mark_bar().encode(
        y='Anteil:Q',
        x='Top 4 Gründe dafür:O',
    )
st.altair_chart(bar_chart, use_container_width=True)


txt = st.text_area('', '''
    Basis = 1025 Befragten;
    ''')
st.text("Klicke an die Balken um die Daten genauer anzuschauen. Du kannst auch die Diagramm vergrößern und ein Bild davon machen")
st.text("Quelle:  forsa-Umfrage")