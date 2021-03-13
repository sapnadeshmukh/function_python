def find_max(numbers) :
    maxelement = numbers[0]
    for element in numbers :
        if element<maxelement :
            maxelement= element  
    return maxelement

marks=[-45,-88]
result = find_max(marks)
print(result)

