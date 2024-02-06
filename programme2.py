g = input("Enter gender only M or F: ")
blood = float(input("Enter hemoglobin value: "))

if g == 'M':
    if 134 <= blood <= 167:
        print("normal level of hemoglobin for males.")
    elif blood < 134:
        print("low level of hemoglobin for males.")
    else:
        print("high level of hemoglobin for males.")
elif g == 'F':
    if 117 <= blood <= 155:
        print("normal level of hemoglobin  for females")
    elif blood < 117:
        print("low level of hemoglobin females.")
    else:
        print("high level of hemoglobin for females.")
else:
    print("provide only M OR F")