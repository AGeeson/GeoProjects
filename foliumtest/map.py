import folium
import os 
import json
m = folium.Map(locaiton=[42.3601, -71.0589], zoom_start=12)

#Vega Visualisation
vis = os.path.join('data','vis.json')

#global tooltip
tooltip = 'click for more info'

#create markers
folium.Marker([42.363600, -71.099500], 
	popup='<strong>location1</strong>', 
	tooltip=tooltip).add_to(m)

folium.Marker([42.333600, -71.109500], 
	popup='<strong>location2</strong>', 
	tooltip=tooltip,
	icon = folium.Icon(icon='cloud')).add_to(m)

folium.Marker([42.315140, -71.072450], 
	popup=folium.Popup(max_width=450).add_child(folium.Vega(json.load(open(vis))))).add_to(m)


#circle marker
folium.CircleMarker(
	location=[42.466470, -70.942110],
	radius = 50, 
	popup='My Birthplace',
	color= '#428bca',
	fill=True,
	fill_color='#428bva',
	).add_to(m)

m.save('map.html')