import pickle
with open(r"haloid_list.pkl", "rb") as input_file:
    e = pickle.load(input_file)
print(e[0][:])