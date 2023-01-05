def remove_spaces(string: str)-> str:
    """
    Removes all spaces from a string of fixed length of 5 characters.
    args:
        string: str
    returns:
        str
    """
    if string[0]==" ":
        ans=string[1]+string[2]+string[3]+string[4]
    if string[1]==" ":
        ans=string[0]+string[2]+string[3]+string[4]
    if string[2]==" ":
        ans=string[0]+string[1]+string[3]+string[4]
    if string[3]==" ":
        ans=string[0]+string[1]+string[2]+string[4]
    if string[4]==" ":
        ans=string[0]+string[1]+string[2]+string[3]
    # Your code here
    return ans
string=" absd"
print(remove_spaces(string))