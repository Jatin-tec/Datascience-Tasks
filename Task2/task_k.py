print("Name: Jatin Kshatriya")
print("Enrollment no: 0108AI201024")
print("Scholar no: 30494")

row_1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]
row_2 = ['Instagram', 0.0, 'USD', 2161558, 4.5]
row_3 = ['Clash of Clans', 0.0, 'USD', 2130805, 4.5]
row_4 = ['Temple Run', 0.0, 'USD', 1724546, 4.5]
row_5 = ['Pandora - Music & Radio', 0.0, 'USD', 126879, 4.0]
first_4_fb = row_1[:4]
last_3_fb =row_1[-3:]
pandora_3_4=row_5[2:4]

print(first_4_fb)
print(last_3_fb)
print(pandora_3_4)

data_set = [['Facebook', 0.0, 'USD', 2974676, 3.5], ['Instagram', 0.0, 'USD', 2161558, 4.5], ['Clash of Clans', 0.0, 'USD', 2130805, 4.5], ['Temple Run', 0.0, 'USD', 1724546, 4.5], ['Pandora - Music & Radio', 0.0, 'USD', 1126879, 4.0]]

fb_row = data_set[0]
fb_rating = fb_row[-1]
print(fb_rating)
fb_rating = data_set[0][-1]
print(fb_rating)
