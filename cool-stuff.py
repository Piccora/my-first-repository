highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"
# print(highlighted_poems)
highlighted_poems_list = highlighted_poems.split(",")
# print(highlighted_poems_list)
highlighted_poems_stripped = []
for i in highlighted_poems_list:
  highlighted_poems_stripped.append(i.strip())
# print(highlighted_poems_stripped)
highlighted_poems_details = []
for j in highlighted_poems_stripped:
  highlighted_poems_details.append(j.split(":"))
# print(highlighted_poems_details)
titles = []
poets = []
dates = []
for z in highlighted_poems_details:
  titles.append(z[0])
  poets.append(z[1])
  dates.append(z[2])
t = 0
for s in titles:
  print("The poem {} was published by {} in {}.".format(titles[t], poets[t], dates[t]))
  t += 1
