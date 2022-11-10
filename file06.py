def main(data:str):
    """
    The data is from the file. Find the each row length and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    a=data.split('\n')
    b=[]
    for i in a:
        b.append(len(i))
    return b
f=open('txt_file/data06.txt').read()
print(main(f))
