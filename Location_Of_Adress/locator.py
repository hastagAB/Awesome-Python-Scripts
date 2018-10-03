import geocoder
t=input("enter the location:")
g = geocoder.arcgis(t)
print(g.latlng)

