#%%
from deep_translator import PonsTranslator

# %%
def word_translator(word, lang_in, lang_out):
    trans_word = PonsTranslator(source = lang_in, target = lang_out).translate(word, return_all=False)
    print(trans_word)
# %%
word_translator('good', 'english', 'italian')

#%%
if __name__ == "__main__":

    word_translator("Let's Go Brooklyn!")