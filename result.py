import pandas as pd
import clustering

clothes_data = pd.read_csv('clothes_dataset.csv')

dry_cleaning = clothes_data[clothes_data['care_label'].isin(['Dry'])]
handwash_only = clothes_data[clothes_data['care_label'].isin(['Hand wash only'])]

dry_cleaning_df = pd.DataFrame(dry_cleaning)
handwash_only_df = pd.DataFrame(handwash_only)

dry_cleaning_df.to_csv('dry_cleaning.csv', index=False)
handwash_only_df.to_csv('handwash_only.csv', index=False)

clothes_data = clothes_data[~clothes_data['care_label'].isin(['Dry', 'Hand wash only'])]

num_samples = clothes_data.shape[0]
print(num_samples)

result = []

if num_samples >= 2:
    clustering_result = clustering.color_clustering(clothes_data)

    basket_0 = pd.read_csv('basket_0.csv')
    basket_1 = pd.read_csv('basket_1.csv')

    basket_0_dehydration_1 = basket_0[basket_0['dehydration_type'].isin(['Light', 'Mid'])]
    basket_0_dehydration_0 = basket_0[basket_0['dehydration_type'].isin(['None'])]

    basket_1_dehydration_1 = basket_1[basket_1['dehydration_type'].isin(['Light', 'Mid'])]
    basket_1_dehydration_0 = basket_1[basket_1['dehydration_type'].isin(['None'])]

    water_temperature_basket_0_dehydration_1 = basket_0_dehydration_1['water_temperature'].astype(int)
    avg_water_temperature_basket_0_dehydration_1 = water_temperature_basket_0_dehydration_1.sum() // \
                                                   basket_0_dehydration_1.shape[0] if basket_0_dehydration_1.shape[
                                                                                          0] > 0 else 0
    indices_basket_0_dehydration_1 = basket_0_dehydration_1.index.tolist()

    water_temperature_basket_0_dehydration_0 = basket_0_dehydration_0['water_temperature'].astype(int)
    avg_water_temperature_basket_0_dehydration_0 = water_temperature_basket_0_dehydration_0.sum() // \
                                                   basket_0_dehydration_0.shape[0] if basket_0_dehydration_0.shape[
                                                                                          0] > 0 else 0
    indices_basket_0_dehydration_0 = basket_0_dehydration_0.index.tolist()

    water_temperature_basket_1_dehydration_1 = basket_1_dehydration_1['water_temperature'].astype(int)
    avg_water_temperature_basket_1_dehydration_1 = water_temperature_basket_1_dehydration_1.sum() // \
                                                   basket_1_dehydration_1.shape[0] if basket_1_dehydration_1.shape[
                                                                                          0] > 0 else 0
    indices_basket_1_dehydration_1 = basket_1_dehydration_1.index.tolist()

    water_temperature_basket_1_dehydration_0 = basket_1_dehydration_0['water_temperature'].astype(int)
    avg_water_temperature_basket_1_dehydration_0 = water_temperature_basket_1_dehydration_0.sum() // \
                                                   basket_1_dehydration_0.shape[0] if basket_1_dehydration_0.shape[
                                                                                          0] > 0 else 0
    indices_basket_1_dehydration_0 = basket_1_dehydration_0.index.tolist()

    result.append({
        'basket': 'basket_0',
        'dehydration': 'Light',
        'average_wash_temperature': avg_water_temperature_basket_0_dehydration_1,
        'indices': indices_basket_0_dehydration_1
    })

    result.append({
        'basket': 'basket_0',
        'dehydration': 'None',
        'average_wash_temperature': avg_water_temperature_basket_0_dehydration_0,
        'indices': indices_basket_0_dehydration_0
    })

    result.append({
        'basket': 'basket_1',
        'dehydration': 'Light',
        'average_wash_temperature': avg_water_temperature_basket_1_dehydration_1,
        'indices': indices_basket_1_dehydration_1
    })

    result.append({
        'basket': 'basket_1',
        'dehydration': 'None',
        'average_wash_temperature': avg_water_temperature_basket_1_dehydration_0,
        'indices': indices_basket_1_dehydration_0
    })

    print("결과", result)

else:
    print("옷을 분리 해서 세탁할 필요 없습니다.")
    try:
        water_temperature = clothes_data['water_temperature'].astype(int)
        avg_water_temperature = water_temperature.sum() // num_samples

    except:
        print("세탁기를 사용할 수 있는 옷이 없습니다. 드라이 클리닝 및 손세탁 해야하는 옷은 다음과 같습니다.")
        # dry_cleaning.csv, handwash_only.csv 출력

