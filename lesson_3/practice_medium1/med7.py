# munsters = {
#     "Herman": {"age": 32, "gender": "male"},
#     "Lily": {"age": 30, "gender": "female"},
#     "Grandpa": {"age": 402, "gender": "male"},
#     "Eddie": {"age": 10, "gender": "male"},
#     "Marilyn": {"age": 23, "gender": "female"},
# }

munsters = {
    "Herman_age": 32,
    "Herman_gender": "male",
    "Lily_age": 30,
    "Lily_gender": "female",
    "Grandpa_age": 402,
    "Grandpa_gender": "male",
    "Eddie_age": 10,
    "Eddie_gender": "male",
    "Marilyn_age": 23,
    "Marilyn_gender": "female"
}



def mess_with_demographics(demo_dict):
    for key, value in demo_dict.items():
        value["age"] += 42
        value["gender"] = "other"
mess_with_demographics(munsters)
print(munsters) #yes 