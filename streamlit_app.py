import streamlit as st
from pathlib import Path



def get_file_content_as_bytes(file_path):
    with open(file_path, "rb") as file:
        return file.read()

# Pfad zur PDF-Datei
file_path = 'lebenslauf1.pdf'

# Lese den Inhalt der PDF-Datei als Bytes
file_bytes = get_file_content_as_bytes(file_path)

left, right = st.columns(2)

left.image("https://schulenwien-my.sharepoint.com/:i:/r/personal/tyron_francisco_s_edu_magwien_gv_at/Documents/Microsoft%20Teams-Chatdateien/profile-pic%20(2).png%20TYRON.png?csf=1&web=1&e=vBmbKP")

right.markdown("""<h3>Tyron Francisco</h3>
     <em>Ich finde IT faszinierend .</em>
     """,unsafe_allow_html=True)

right.download_button(
        label="📄 Lebenslauf",
        data=file_bytes,
        file_name=file_path,
        mime='application/pdf'
)

 

st.header("IT-Kompetenzen" , anchor=False, divider="blue")

st.markdown("""
            -   Webentwicklung: Fundierte Grundkenntnisse in HTML, CSS und Streamlit
            -  Programmierung: Praktische Erfahrung in Python, Entwicklung kleiner Anwendungen und Skripte
            -   Office-Suite: Versierter Umgang mit Microsoft Word, Excel und PowerPoint
            -   Eigene Projekte: Konzeption und Umsetzung verschiedener Projekte inklusive Hosting
            -   Schulprojekte: Erstellung datenbasierter Präsentationen und interaktiver Tabellenkalkulationen
            
            """, unsafe_allow_html=True)
st.header("Schulbildung" , anchor=False, divider="blue")

st.subheader("FMS SCHAUMBURGASSE" , anchor=False)
st.markdown("""
            - Schwerpunkte:Intensive IT-Spezialisierung,Fokus auf moderne Webtechnologin und Wirtschaft

            - Zeitraum:2024-Laufend
            """, unsafe_allow_html=True)
st.subheader("OMS Florian-Hedorfer-Sraße" , anchor=False)
st.markdown("""
          - Schwerpunkte:Berufsorientierung,Soziales lernen,Bewegung und Sport
          - Zeitraum:2020-2024
            """, unsafe_allow_html=True   )
            
st.header("Arbeitserfahrung" , anchor=False, divider="blue") 

st.markdown("""
            
    -   Berufspraktische Tage 1: Bei KFZ-Mechatronik von 18.November bis 24.November 2024
    -  Berufspraktische Tage 2: Bei Hotel Doubletree von 22.Oktober bis 26.Oktober 2023       
           

         """, unsafe_allow_html=True   )


st.header("Zusätzliche Qualifikationen" , anchor=False, divider="blue") 

st.markdown("""
            -   Schnelle Auffassungsgabe für neue Softwareanwendungen und Technologien
            -   Großes Interesse an der kontinuierlichen Weiterentwicklung im IT-Bereich
            -   Teamfähigkeit und Kommunikationsstärke bei gemeinsamen Coding-Projekten
     """, unsafe_allow_html=True)

st.header("Interessen und Hobbys" , anchor=False, divider="blue") 

st.markdown("""
            -   Fußball: Mitglied in einem Fußballverein
            -  Basketball
            -  Krafttraining
            """, unsafe_allow_html=True)