#%%
import nltk
#nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
stop_words = set(stopwords.words('english'))

#%%
def part_of_speech(phrase):
    tokenized = sent_tokenize(phrase)
    for i in tokenized:
        words = word_tokenize(i)

        words = [w for w in words if not w in stop_words]

        tags = nltk.pos_tag(words)
        print(tags)

# %%
if __name__ == "__main__":

    part_of_speech("Let's Go Brooklyn!")

# %%
