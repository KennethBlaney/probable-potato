#%%
from collections import Counter

#Input a word or phrase and receive the quantity of each character.
#%%
def char_freq(user_str):

    elements = Counter(user_str)
    str_elements = str(elements)
    return str_elements

#%%
if __name__ == "__main__":

    char_freq("Let's Go Brooklyn!")

# %%
