file = open("data.txt", "r") 
data = file.read()
list = data.split(" ")

freq = {}
total = 0
possible = input("Enter the word: ")
for i in range(len(list)):
    if list[i] == possible:
        if list[i+1] not in freq:
            freq[list[i+1]] = 1
            total += 1
        else:
            freq[list[i+1]] += 1
            total += 1

probability = {}
for i in list:
    if i in freq:
        probability[i] = freq[i]/total
    else:
        continue
        
sortedDic = sorted(probability.items(), key=lambda x: x[1], reverse=True)
sortedDic = dict(sortedDic)


print(f"The next words after '{possible}' can be: ")
for keys, values in sortedDic.items():
    print(keys)
