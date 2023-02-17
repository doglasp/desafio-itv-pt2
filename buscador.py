def buscar(Input):
    Output = []
    if(Input.__contains__(5)):
        Output.append(5)
    if(Input.__contains__(7)):
        Output.append(7)
    if(Input.__contains__(9)):
        Output.append(9)

    return Output

Input = [7, 3, 9, 9 , 12, 40, 5]
Output = buscar(Input)
print(Output)