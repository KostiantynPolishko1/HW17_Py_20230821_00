data = {'win_size': {'h_min': 1100, 'h_max': 1800, 'w_min': 950, 'w_max': 1700},
        'profile': {'Rehau': 1500, 'WDS': 1250, 'Steko': 1000}}
arr_key = list(data.keys())

arr_profile = list(data[arr_key[1]].keys())
arr_profile.insert(0, arr_key[1])

# for i in arr_profile:
#     print(i)
