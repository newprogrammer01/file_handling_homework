def main(data:str):
    """
    The data is from the file. Find the each row length and return the largest row.
    Args:
        data: str
    Returns:
        int: return answer
    """
    list=[]
    for i in data:
        if i.isalpha():
            list.append(str(i))
    return min(list)
# Read data from file
f=open('txt_file/data10.txt').read().split("\n")
print(main(f))
