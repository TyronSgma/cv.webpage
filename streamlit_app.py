import streamlit as st
from pathlib import Path

def get_file_content_as_bytes(file_path):
    with open(file_path, "rb") as file:
        return file.read()

# Pfad zur PDF-Datei
file_path = 'test.pdf'

# Lese den Inhalt der PDF-Datei als Bytes
file_bytes = get_file_content_as_bytes(file_path)

left, right = st.columns(2)

left.image("data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBxISEA8PDxIVDw8PEBAPDw4PDw8PDxAQFRIWFhUVFRUYHSggGBomHRUVITEhJSkrLi4uFx8zODMsNygtLisBCgoKDg0OGxAQGi0hHyUtLSsrLS0tLS0tKy0rKy0tLS0tLS0rLS0tLS0tLS0tLSsvLS0tLS0tLS0tLS0tLS0tLf/AABEIALcBEwMBIgACEQEDEQH/xAAcAAACAgMBAQAAAAAAAAAAAAAAAQIDBQYHBAj/xABCEAABBAADBAcFBgQFAwUAAAABAAIDEQQSIQUxQVEGEyJhcYGRBzJSobEUQnKCwfAjYpLRM6LC4fFTY7MkJUODsv/EABoBAQADAQEBAAAAAAAAAAAAAAABAgMEBQb/xAApEQEAAgICAgAFBAMBAAAAAAAAAQIDESExBBIiMkFRcROxweGBkfBh/9oADAMBAAIRAxEAPwDecqKSzph4V1TClajmClYUCTXKWZV2EiUF4Kla84cmHoLgpBqpD1PrEFlJKGZGZBMlIAKuSRrQXOIa1oLnOcQGtA3kk7gtV2ntiSc9XhiY4dzphbZJfwcWt7957uNMmStI3LTHitknVWd2ntzDwHLJJcn/AEowZJPNo93zpYaTpswe7hpyOZ6tv6lePA7KYwbt+p7zzVs2EA3BcM+ZMzxD0K+DTXM7l6MP05gJqaOXD/zuaHsHiWWfktlw2IZI1skT2yMcLa9jg5p8CFz7GYQG+axuGlmwrzJh3ZCTbmHWKT8bf10PetMflxM6srk8DjdHV1IFYjo/tyPFR5m9iVmksJNuYeY5tPA/Q6LKrsid8w86YmJ1KadqCLUoTQoZk7QSQlaMyCQCeVRDk7QMNUqUbTtA8qMqMyjaCVIStFqQUE0k0GKSKdqNqBNpVgpU2pAoLgApZQq2lTCCQaE8iQTtBEhAITJUCUFgIUgqQ5eXa2O6mCaYamON7mjm4Dsj1pQaaxtzFnF4kwMP/pcM6ngbp8Q063zaw6AfECeArJ4bDAAUFidhRBsbBv3W46knme871sEQ3Lyc1/e23sYafp1iEo8Pe5Slwui92HYrHsSMfC85OWsYvDb1g8dDXetvxkVWtd2o3RZTGrN623DWw6SJ7ZoHZJYzbTvB5tcPvNO4j6Gium7C2q3FQMnYMua2vYd8cjTT299HceIo8VzqYLNez+bJiMRB92WMThvDMxwY4+JD2f0hej41p6eb5lI+ZvgRSVphdbzxSAEWnaATUbRaCaYUAUw5BOkUo5lK0BSdJWmgdIpJCB0hCEGKDU+rTCYKCIjUgxSBTzIFlRqnaYKBWU9U00FRtRNq0pIlXlWE6ZuLcDMboXCD4GeMLPgLCdN482z8SOQjf/TKx36Ktuk1nmGK2PICxncPmsw3HRMNPe1tamzuWmbL2hkYWODmvIaGnKTb3WA0cM240a3+NefEYTDjSV0kjpDZZ10gJdXAx0XHefddx4Lza4ed2/w9Scu+K/Tt0nA7cwrjlbMxzqsAOB05r3xSBxsHTnzXGMLiQ1zn4VmRjercXSsmc6ni2El3A8CKB4WtmwfTIRjJLDL1taNhb1oI5ita8lrNJidVhnExrc/Vuu1ZGMaXuNABaRjukWELi0vynhmFA+BXl2x0pMjWdWLzFwDTo6xvBB3bxvC1TGwRl7RM1oc/UNYMS4O7IdecDKdCDppRB3apGHc/Fwn9aYj4ZbE7Fsf7jg4XwOoWa6Jt/wDcABwwcp3f9yH9+S0rZmFja9r47DT8JL2kHXdeo3bluHQaZr9oTOzNJZA6MNshxt0TrAIBqgd26vAnfFjivMOfPlm3E9ugZSnqrA5FrocirVSFqSKQIJ5UKQKBZUsqnmTtBCimAVMJobV0VLVTTtNG0BaeqlmRaCFlCmhBiA5PMi1MIlEFSa5CEQlaLStGZBLMlnTzItEladoRSBrG7Y7RjhcCIZ2yxyPbVtNDLemgPaF86WSteLa9mKQNrN1bsl7g49kHyJvyWWaZik6beNETkiJc/i2YyFknV9oQYgyOc4kkxNmt7id5IYXG+5ZvD7AqfrwO2A9ozDMMrhRFclRsAhuJxMe9omlaLo5hYu/G1sOGhliGVjRNEPcD3lkkbeDc1EOHAWAa3k715+533y9GNRH/AIw2yejAhztjDWtlI6zMHSW1t5WjNw14r27OwLftU8gAyQxMwzNPvDtSa8atjfFrlLGbQxRcI2RMgzGjK6brXgH4WgVfifVZXZmEaxnVt0DQeNmybJJO8kkkk7ySp3KfXr7OeYvZEZ2i8O1D2l5bTSDVA9kinUSLHeF7trbMBxIxTRcgG7O7JnyNbny5TRpjLoj3RyV23sE50znsJY6Knte0jO12oNXodDuOhXrw/wBpLWu6qDEAgHrGSvhJ/wDrc13/AOknJbjUrRirvmP+lrjtk9UyR3uh10OAe7TQd5IWLnkdBL9ojcWSRRgMLSQS5w6sXX4vQnmtx2oXkVI0N4hoFAednN8h3bitMxso+0PYTocjQKu7D9e6nBpvuW2O0zWZY2rWLxEw7dDeVub3sozfirX5qajG6wHfEAfUWpLteVITQE1ISE00EUwUFACCQKmFABNBK0rSCdIHaeZKkZUDtCjSaDEAp5lCk6QWZknOUQ0KWQIE11poEYTyIBOk8iAxEmCpBR6tGRBKl58W2ssm/Jv1rski/or8qRYq2r7Rpal5raJc0wmKy7Sxsd1/Gke3WwM1GvQj0W0y7Te1hI3AXmJptVvtaV0rwwg2qaIY2djHsoU0Etyn5svz71dBtB0uFxEQNyt0o6ferf8AveFw5cM+z0MOaPXlmm7dhja8yOdJKWm6NZeQb8te9a3h+khj6wxySl7vdEry8O4+I47hqp9FujpnjdM57X25zHRvEgcNbtrmnX0WxYboRGx7pmRxvcQAGyTPI376LdP9laKUjcdtInLfmNQ55iNvzvlc+Rz47NZWvAFeC2zo90gYwNjDjRFDNu0CNu9DmAmRojBDQ2hJJlNd1fO1qWP2O+EtdnHb90NDsoqgdSf+Vaa478dKWnLh5tqYbztLGvc4cjxWvbKwzsTjzFGLtpaXVeQa248gE9o7eaGMZ99rA13HWqK2j2QRnqcVLwkmaL4HK2/9Sthxz66llnzRFtw6DG0AADcAAPAKSQCF1OA01A2mLQTCagmEEkKKYQNO0gmgAU0BNAItCEAhCaDDITATpSBpU1ENUqUB0mEkIJWgFRTQTKQCjmUg5A0ItFoloPtbwFwQ4luj4ZCwm67DweXeB6lcywW0XRuztPvGiBu4D9F0fpftlk20IMHocPGXQza9l00jctflOUeJcua7X2e7DzyROFUTlvW22aIv6qLRqfWfttas/D7R99Nr6I7aEY6txIbK91g2KsDKR++C9GOx+ODw2N7yxzqac5y67jfAd60NsjgeySCC05vp9N/is+3pDK6JrXE03QH+Y6jvrVZWxc7htTLxqZZfrcTvxGYtbYcC8mjrvvwpa9tbaTpC7gBdHXSzWny/4RituSOBGbRxBINgd/hw9VietsHnWUEbzdcPIhWpj1O5Rky7jUGJS48zpu4nzXf+g+yzh8FDGTmc4da8mvefrWm8DQX3Lk/s+6NvxU7ZnX9nge3NYItw+6PAUfJdzjNClowmViLUcyVqBMFSDlXaLQWFAVYKdohNNQtCCwJ2q7TtSLAUWqwUZkFlqSqzJh6CxNV50kGMpMBQzpdYgtCmFQJE+tROlyFUJU86g0stAKqD0dYguQoB6pxu0IoWGSZ7Y2D7zjWvIDeT3DVSh6lrHSrpjFhSYY6mxRF9WD2YRwdIfo3ee4arV+k3tCkfcOCBhadDiHf4pH8g+547/wAK0bDmi47yTbnmy5zjqSSd5XRjwTM/Eyvk1HD1OJJLiTnLi4vvtZrvNfO9VuO08E3aWCZM0BuJZbH/AMsg94HuNgjuIWotN6rLdG9sfZpgX/4Epayazo34ZPK6Pce4LXzcE3p7U+aFfDzRW/rbqWn4jDuifle05wa14i73DuPyVL5gdBRFag3XGq136rrnSXYbJAXZRfgP3wC5rtHZJYSANBa8vH5EW4niXo38aY5jmGMaToNTxJBB/elLI7G2HNOQPdjui5wI0vWq7lVgcMS5ra+9xG4nj8gt6hIia0bqFuPgrXya6MeHfMvB0P6anAPnwskXXQukMkRY4NkYHa0M3vAgg0SKN66rfdm+0bZ8ujpH4d3wzxubX5m235rheNcSIJObHNJ72yO0/pcz1Uw7ML4jiuitYly2nT6WwW04JaMM0ct/9OVj/kCvWQvl5ruevestgtv4qIVFiZmD4RNJlHkTQU/pq7fRSAuFQ9ONoAV9pcdfvMhcfUtW8dCenxxDxhcYGsmd/hTMGVkp+Ej7rvke7jE45hPtDf6SpR6wI60KiUwmqxIE84QTTCrDwpZ0E6TAUA9POgnSVJB4TzIFSE7QgxACC0Jgpokg0KWUICaADQpZUgUw5ABoSdlALnUGgWXEgADmSdwWI6Q9JIcI3tnPKR2IGEZzyLvhb3nytcw27t/EYx38V2WIG2wMJETeV/Ge8+VLXHhtdnbJFW5dIOn0Udx4MCeTd1zr6hvhxk8qHeVz/H4+bEP6yd5ldrWY01o5NA0aO4Kpsdb9UyV34/HijlvlmytsQvXVRnI3bgFa0a6qDj2rWsxERwzieVcEld44HeF6XCxru4BUPYLDgBZ4jir2G0j7E/dvfQrGfacO7CPdWIwzR1Tj/wDJBuaD+HRt8sqx22cCQ5zHtyuG8HQ/2Pite2Zj3YeePEM1MbrLfjYdHN8x86PBdWx+EjxkEcjCLc0OglO4hwvI7jr++R87y/Bi/wAdPm/d6HiebNPhv8v7f05T9jyusaKG3MeREQDqRlWw4vZz2OLHtLXDga9QeI7wsLtXY7nZdNF5UTqdWetaN13VjINiOlwbXAe6BMDzaW1JXo0/lKwkPZJB4Giuu9AMPUMkEg7UD26E3cUrc7fLX6LTtv8ARl8TnhrTmhJFDXPFva4c9KPqF9BGKt6Raveng2vNLTW33a49gFUbv3u7kotCty6fvcouasrVWiU2FTPMaEaggkEHuPBUhWtKhLs/s/6R/bMPkkN4mABspqs7TeV/iao9471tYYFwPortp2DxTJWmmOIbM3g6IuGbzHvDvC74x4IBabBAII3EHcVzZK+stK23BhgUurCLRmWa5iMJ9WEAplyCGRPKglRtEJZUwFEKSB0hK0IMTSmlSaJSCajaC5AEd65Z0q6byyvfDhHmLDtJb1sZqSbmQ4atZyrU7ydaG5dPNoGHATuaafIGwNINH+IadXflzHyXGWlb4axPMs8kzHEPY3U2SXOJJcSSSTxJPEr1tbovLhwvZCvSp04rokJUrJBr47vHkq7UzKqtygVY4KKrMraVtO8Hd9D/AGU2GtEyNVEhCTcVvns22nbZMG52rbkjB1DmE9oeRN/m7loDnL0bNx7oJop274nAkD7zdzm+YseibNOs7bkj7MWJtriagxFsyZjZy61W7cTrpu0WMbCCSx1ZmnKaII3cPUHzW0RdXiIWmhJFKwH+UtcLBrjvXNOjsBwuJfhXAgGVsY+EyNdlJ3DUgjyAXn+b4kWrN47/AI/p6Hh+TNZ9J6/lvGN2I8P+0YQ5ZAxrHx3lbK1rQBqNx7Le45R3348dtWGQwF1NxBBZJFvIb3nle7xdyIGvdM9tzTTvw2He5sUJyO6txbnkHvFxGpAOld1rx9Huik+ds7tO0NDdnUL08eL1t7fRw5M3tT1nuP8AbE9MdlNw+KexnuPa2Zo5B5II/qB9Vr5auudOdi9bC6QNuSGJrgRvLWl2cehJ8QFydwo1yWWSv1KyoCkEnDU+qkFhptsP4Hlr5cfkuv8Asx2wZsMcO82/DUGk8YjYb6UR4UuR0sz0L2wcLiYpSexfVyjnGSGu9NHeSzvXdVqzqXd6KKKdozLkbi0wUBCIO0WlaAUAQUxaLRaJSQkhEMMZTyUhIeSaYULE4lRsq0IUDnvtZxPYwkPxPllP5Gho/wDIVz5i3H2ry3ioGfDh83m6R4/0hafCF24eoc+Xt68OvdGvJCF6Y3Lur05J7WPFjkeB5FefNevr3HivRYXmk0dXB2o8R/t9FMkAlQIRaaqkUoFSScoSokPH18UmlTkHmONcl5waNKNradP9l+2c0b8I89qLtR3xicdR+V3yc1ZTbGw3fb8Ni2NBjDg6UirDmNPaOmoIAb4gcyVyzYu0zh8RFONzHfxAOMZ0eO/TUd4C7nFO1zGvuwRvB0ojQq0cwrPHLTeieyszetfq6V7nudzLu1+q3YQgZGgULXg2HhBGxkY1ygbzfCh9Pkss73h4K97TKsRpRPHZ/KfquF9IcD1GImi3CORzR+Dez/KWrvTxr5LlftOwOWeOYbpotfxxmif6XM9FTuE9S0OUbvRRtWP3H1VVrCW0L49xCgw06uf0IH9k4Xa93FUPJzt4EsafC7VVn0B0Rx/X4LDyE27J1bzzdGSwnzy35rMrQPZPjQYJYCe0x/WtH8rgAa8x81vlrivGrTDorO4TtMKolMOKqlYUKNpWgmi1EFO0QlaEkIMXadpUEUFCx51HrgpZQgsCDkPtLmzbQd/JDCz5F/8ArWv4dZPpu69o4v8AGwekTB+ix0C7sMdObLL1xr0M8lQwKwfviu2HKtce9ePFu0sakajx30rXOXkneNyi3S1e1rng04ahwvghrl4sFLo5nwmx4FekOVIncbWmNcLS5Bd/ZRtRcVKNESvPJ9NR4cVaXKp5+SzleIGZdQ9nm1OswhgebMJ6o60clZmHTdpbfyrlV8tx3LY+gu0eqxjWE9nEN6o/jGrPnY/Mr0tyi1eHYoic7XDdrZJAuzm8dAT6he8nteSxGFlzR3VuZmFkaAt48efnSycLrrwG/f3K9oZQsetP9o2Dz4PON8EjX6fC45CP8wP5VuL1jNq4ProZoeMsUjB3OLSAfWkqS4G7evMTS9U/vHhetLxuGp8ePBYW4ltVOMWRe7lz/wBkY19S/kH1KcO8KrHf4o/C36lZW4aQ2/2f7R6raGEF9mds8J8w0t/zNHqu0WvnXAzlmJwbhvjljfp3PB/RfRNLnzR8W2uOeApAJJrJc0KBCAUE6UgoUnlQTQo0kiGOSzJoRYs6YKaEHEul5vaGMP8A3nD0Ab+i8eH10Qhd+H6OTI9UDrsHeFZXNCF1wwlGT9+q8OKZx4oQq26Wr28GFkqUd4I/X9FkAhCww9T+WuTs8yRKELVQEKlyEKtkwrHEctR4cU45C0te005hD2nk5psH1CEKsLS7VsjEiRvWjRmIhjmAN2C4ZSPmPRZ7AH3e9tUBQBaSD+iELpt0544l7Xqho1J4oQqQlwTpFDkxOIZ8M8zR4CRwCw53ny+iELLJ21p0uw+8LzYo/wAXyahCxv1H5aU7WYNx60OG9pBF663p9F9F7MxgmhhmGgljZJXLMAaQhYZPlify0p3p6bRaELFoRKLQhBMFO0IQFoQhEP/Z")

right.markdown("""<h3>Tyron Francisco</h3>
     <em>Ich finde IT faszinierend .</em>
     """,unsafe_allow_html=True)

right.download_button(
        label="📄 Download CV",
        data=file_bytes,
        file_name=file_path,
        mime='application/pdf'
)

 

st.header("IT-Kompetenzen" , anchor=False, divider="blue")

st.markdown("""
            -  💻 Webentwicklung: Fundierte Grundkenntnisse in HTML, CSS und Streamlit (Fullstack-Framework)
            -  ⌨️Programmierung: Praktische Erfahrung in Python, Entwicklung kleiner Anwendungen und Skripte
            -  📱 Office-Suite: Versierter Umgang mit Microsoft Word, Excel und PowerPoint
            -  📽️ Eigene Projekte: Konzeption und Umsetzung verschiedener Projekte inklusive Hosting
            -  👨‍🎓 Schulprojekte: Erstellung datenbasierter Präsentationen und interaktiver Tabellenkalkulationen
            
            """, unsafe_allow_html=True)
st.header("Schulbildung" , anchor=False, divider="blue")

st.subheader("FMS SCHAUMBURGASSE" , anchor=False)
st.markdown("""
            - Schwerpunkte:Intensive IT-Spezialisierung,Fokus auf moderne Webtechnologin und Wirtschaft

            Zeitraum:September-Laufend
            """, unsafe_allow_html=True)
            
st.header("Arbeitserfahrung" , anchor=False, divider="blue") 

st.markdown("""
            
    -  🤕 Berufspraktische Tage 1: Bei KFZ-Mechatronik von 18.November bis 24.November 2024
    -  😢Berufspraktische Tage 2: Bei XYZ von 24. bis 28. Feb. 2025        
           

         """, unsafe_allow_html=True   )


st.header("Zusätzliche Qualifikationen" , anchor=False, divider="blue") 

st.markdown("""
            -  😓 Schnelle Auffassungsgabe für neue Softwareanwendungen und Technologien
            -  😟 Großes Interesse an der kontinuierlichen Weiterentwicklung im IT-Bereich
            -  😉 Teamfähigkeit und Kommunikationsstärke bei gemeinsamen Coding-Projekten
     """, unsafe_allow_html=True)

st.header("Interessen und Hobbys" , anchor=False, divider="blue") 

st.markdown("""
            -  ⚽️ Fußball: Mitglied in einem Fußball
            -  🗣 Lesen: Begeisterte Leserin verschiedenster Literatur
            -  ♟️Schach: Engagiert im Schachklub
            """, unsafe_allow_html=True)