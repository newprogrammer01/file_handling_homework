def main(data:str):
    """
    The data is from the file. Find the largest of the numeric characters.
    Args:
        data: str
    Returns:
        int: return answer
    """
    list1=[]
    for i in data:
        if i.isdigit():
            list1+=i
    return max((list1))
# Read data from file
f=open('txt_file/data08.txt').read()
print(main(f))
