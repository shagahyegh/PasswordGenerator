from random import choices,shuffle
from string import ascii_lowercase,ascii_uppercase,digits,punctuation
lst_pass = choices(digits, k=2) + choices(ascii_uppercase, k=2) + choices(ascii_lowercase, k=2) + choices(punctuation, k=2)
shuffle(lst_pass)
C_lst_pass = "".join(lst_pass)
print(f'PassWord Generator is : {C_lst_pass}')
