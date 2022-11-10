def main(data:str):
    """
    The data is from the file. Find the number of digital and str(non-digital) data and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    a=[]
    
    for i in data:
        if i.isalpha():
            a.append(i)
        if i=='\n':
            a.append(' ')
    l1=len(a)
    l2=len(data)-l1
    r=[l2,l1]
    return r
f=open('txt_file/data05.txt').read()
print(main(f))

    

