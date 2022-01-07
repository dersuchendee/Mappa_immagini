import pandas as pd
import datetime
import folium
from folium import Map
from folium.map import Layer, FeatureGroup, LayerControl, Marker
from folium.plugins import MarkerCluster, FeatureGroupSubGroup, Fullscreen

df = pd.read_csv('dataset mappa 27-12-2021.csv')
df.fillna('', inplace=True)


df['Latitude'] = pd.to_numeric(df['Latitude'].str.replace(',', '.'))
df['Longitude'] = pd.to_numeric(df['Longitude'].str.replace(',', '.'))
df.Latitude = df.Latitude.astype(float)
df.Longitude = df.Longitude.astype(float)
#print(df.head(5))

it_coords = [41.902782, 12.496366]
m = folium.Map(location=it_coords, zoom_start=6.2, tiles='openstreetmap', control_scale=True,
               prefer_canvas=True)

mon1 = folium.FeatureGroup(name = 'Personaggio realmente esistito')
mon2 = folium.FeatureGroup(name = 'Personaggio letterario o leggendario')
mon3 = folium.FeatureGroup(name = 'Figura anonima collettiva')
mon4 = folium.FeatureGroup(name = 'Gruppo di figure anonime collettive')
mon5 = folium.FeatureGroup(name = 'Altro')




for i, v in df.iterrows():
    tipologia = v['Tipologia personaggio']

    popup = f"""
        <img src="{df.iloc[i]['Immagine']}"  width="250" height="200">
<p style="text-align: center;"><span style="font-family: Garamond, serif; font-size: 17px;"><b>{df.iloc[i]['Titolo']}</b></span></p>
        

<section class="container">
  <div class="left-half" style="float: left;
  width: 50%; margin-top: 4px;">
    <article style="top: 50%;"
  "left: 50%; ">
      <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/69/Calendar_font_awesome.svg/1200px-Calendar_font_awesome.svg.png" 
        width="17" height="17"><span style="font-family: Garamond, serif; font-size: 12px;"> <b> {df.iloc[i]['Anno di collocazione']} </b></span>
    </article>
  </div>
  <div class="right-half" style="float: right;
  width: 50%; margin-top: 4px;">
    <article style="top: 50%;"
  "left: 50%;"  >
      <img src="https://img.favpng.com/20/8/5/computer-icons-font-awesome-user-profile-png-favpng-7jVAAybsvYHn2EqV2wQ1b60iG.jpg" 
        width="18" height="15"><span style="font-family: Garamond, serif; font-size: 12px;"> <b> {df.iloc[i]['Autrice/autore']} </b></span>
    </article>
  </div>



</section>
      
        <div style="display:inline-block;
  width: 100%; margin-top: 3px;">
<article>
        <p style="text-align: center;"><span style="font-family: Garamond, serif; font-size: 13px;">{df.iloc[i]['Descrizione']}</p></span>
</article>
</div>


        <p style="text-align: center;"><span style="font-family: Garamond, serif; font-size: 13px;">   <a href="{df.iloc[i]['Crediti fotografici link']}" target= "_blank">© foto {df.loc[i]['Crediti fotografici']}</a></span></p>
        </body>
    """
    iframe = folium.IFrame(html=popup, width=290, height=300)
    popup = folium.Popup(iframe, max_width=2650)

    if tipologia == "Personaggio realmente esistito":
        folium.Marker(location=[v['Latitude'],
                                      v['Longitude']],
                      icon=folium.Icon(color="pink", icon='info-sign'),
                            popup=popup).add_to(mon1)
    elif tipologia == "Personaggio letterario o leggendario":
        folium.Marker(location=[v['Latitude'],
                                      v['Longitude']],
                            weight=0,
                      icon=folium.Icon(color="blue", icon='info-sign'),
                            popup=popup).add_to(mon2)
    elif tipologia == "Figura anonima collettiva":
        folium.Marker(location=[v['Latitude'],
                                      v['Longitude']],
                            weight=0,
                      icon=folium.Icon(color="purple", icon='info-sign'),
                            popup=popup).add_to(mon3)
    elif tipologia == "Altro":
        folium.Marker(location=[v['Latitude'],
                                      v['Longitude']],
                            weight=0,
                      icon=folium.Icon(color="lightblue", icon='info-sign'),
                            popup=popup).add_to(mon5)
    else:
        folium.Marker(location=[v['Latitude'],
                                v['Longitude']],
                      weight=0,
                      icon=folium.Icon(color="darkblue", icon='info-sign'),
                      popup=popup).add_to(mon4)


mon1.add_to(m)
mon2.add_to(m)
mon3.add_to(m)
mon4.add_to(m)
mon5.add_to(m)
folium.LayerControl(collapsed = False).add_to(m)


m.save(outfile='map_2.html')
