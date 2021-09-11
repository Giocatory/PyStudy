countries = ['Russia', 'USA', 'UK', 'Germany', 'France', 'India']
capitals = ['Moscow', 'New York', 'London', 'Berlin', 'Paris', 'Delhi']
population = [145_934_462, 331_002_651, 80_345_321, 67_886_011, 65_273_511, 1_380_004_385]

for cap, cou, pop in zip(capitals, countries, population):
    print(f"{cap} is the capital of {cou}, population equal {pop} people.")
