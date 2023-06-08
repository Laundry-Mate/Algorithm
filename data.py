import pandas as pd
import numpy as np
import colorsys

fabric_types = {'Cotton': ['Normal', 30, 'Light'],
                'Polyester': ['Normal', 30, 'None'],
                'Denim': ['Normal', 30, 'Mid'],
                'Knit': ['Normal', 30, 'None'],
                'Nylon': ['Normal', 30, 'Light'],
                'Napping': ['Normal', 30, 'None'],
                'Canvas': ['Normal', 30, 'Light'],
                'Pique': ['Normal', 30, 'Light'],
                'Rayon': ['Dry', 'X', 'None'],
                'Silk': ['Dry', 'X', 'None'],
                'Leather': ['Dry', 'X', 'None'],
                'Pur': ['Dry', 'X', 'None'],
                'Wool': ['Hand wash only', 'X', 'None'],
                'Acrylic': ['Hand wash only', 'X', 'Light'],
                'Linen': ['Hand wash only', 'X', 'None']}

care_labels = ['Normal', 'Hand wash only', 'Dry']

dehydration_types = ['None', 'Light', 'Mid', 'Strong']

num_clothes = 10

fabric_type = np.random.choice(list(fabric_types.keys()), size=num_clothes)
care_label = [fabric_types[fabric][0] for fabric in fabric_type]
water_temperature = [fabric_types[fabric][1] for fabric in fabric_type]
dehydration_type = [fabric_types[fabric][2] for fabric in fabric_type]

color_r = []
color_g = []
color_b = []

h_list = []
s_list = []
v_list = []

for _ in range(num_clothes):
    r = np.random.randint(0, 256)
    g = np.random.randint(0, 256)
    b = np.random.randint(0, 256)

    r /= 255
    g /= 255
    b /= 255

    color_r.append(r)
    color_g.append(g)
    color_b.append(b)

    h, s, v = colorsys.rgb_to_hsv(r, g, b)

    h *= 360
    s *= 100
    v *= 100

    h_list.append(h)
    s_list.append(s)
    v_list.append(v)

clothes_data = pd.DataFrame({
    'fabric_type': fabric_type,
    'care_label': care_label,
    'water_temperature': water_temperature,
    'dehydration_type': dehydration_type,
    'r': color_r,
    'g': color_r,
    'b': color_r,
    'h': h_list,
    's': s_list,
    'v': v_list
})

# Save the clothing dataset to a CSV file
clothes_data.to_csv('clothes_dataset.csv', index=False)

