def main(data:str):
    """
    The data is from the file. Find the each row length and return the largest row.
    Args:
        data: str
    Returns:
        int: return answer
    """
    a=data.split('\n')
    b=[]
    for i in a:
        b.append(len(i))
    return max(b) 
f=open('txt_file/data10.txt').read()
print(main(f))

