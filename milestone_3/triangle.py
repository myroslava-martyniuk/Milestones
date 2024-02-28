import sys

def get_triangle(rows: int) -> list[list[int]]:
    
    list_of_lists = []

    if rows <= 0:
        return list_of_lists     
    list_of_lists = [[1]] 

    for i in range(1, rows):
        temp = [1] 
        for j in range(len(list_of_lists[i - 1]) - 1):
            temp.append(list_of_lists[i - 1][j] + list_of_lists[i - 1][j + 1])
        temp.append(1)
        list_of_lists.append(temp)
    return list_of_lists



if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Program needs only one integer argument")
        exit()
    if sys.argv[1].isdigit() == False:
        print("The argument you gave is not an integer")
        exit()
    quantity_of_rows = int(sys.argv[1])
    pasqual = get_triangle(quantity_of_rows)
    length = len(pasqual)
    
    for i in pasqual:
        print(' ' * (length - 1), end = '')
        length -= 1
        for j in i:
            print(j, end=' ')
        print()
