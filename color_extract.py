import colorgram

colors = colorgram.extract('spot_paintings.jpg', 25)
extract = []
t = []
for c in colors:
    for e in c.rgb:
        t.append(e)
    extract.append(tuple(t))
    t = []
print(extract)
print(colors)
