char_entered=input("Enter a character: ")
if(char_entered.islower()):
    print(char_entered,"is  a lower case  letter.")
elif(char_entered.isupper()):
    print(char_entered,"is  an  upper case  letter.")
elif(char_entered.isdigit()):
    print(char_entered,"is  a digit.")
elif(not char_entered.isalpha()):
    print(char_entered,"is  a non-alphanumeric  character.")