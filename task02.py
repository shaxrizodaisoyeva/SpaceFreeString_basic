
def count_digits(string: str) -> int:
    """
    Count the number of digits in a string of fixed length.
    args:
        string: string of fixed length
    returns:
        number of digits in the string
    """
    ans=0
    if string[0]=="0" or string[0]=="1" or string[0]=="2" or string[0]=="3" or string[0]=="4" or string[0]=="5" or string[0]=="6" or string[0]=="7" or string[0]=="8" or string[0]=="9":
        ans=ans +1
    if string[1]=="0" or string[1]=="1" or string[1]=="2" or string[1]=="3" or string[1]=="4" or string[1]=="5" or string[1]=="6" or string[1]=="7" or string[1]=="8" or string[1]=="9":
        ans=ans+1
    if string[2]=="0" or string[2]=="1" or string[2]=="2" or string[2]=="3" or string[2]=="4" or string[2]=="5" or string[2]=="6" or string[2]=="7" or string[2]=="8" or string[2]=="9":
        ans=ans+1
    if string[3]=="0" or string[3]=="1" or string[3]=="2" or string[3]=="3" or string[3]=="4" or string[3]=="5" or string[3]=="6" or string[3]=="7" or string[3]=="8" or string[3]=="9":
        ans=ans+1
    if string[4]=="0" or string[4]=="1" or string[4]=="2" or string[4]=="3" or string[4]=="4" or string[4]=="5" or string[4]=="6" or string[4]=="7" or string[4]=="8" or string[4]=="9":
        ans=ans+1
    return ans
    # Your code goes here
string="2ft>5"
print(count_digits(string))