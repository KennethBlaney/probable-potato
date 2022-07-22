#%%
from nltk.sentiment import SentimentIntensityAnalyzer

#Input a word or phrase and receive a sentiment score for the entire input.
#%%
def Word_Sentiment(phrase):
    sentiment = SentimentIntensityAnalyzer()
    sentiment_score = sentiment.polarity_scores(phrase)

    print(phrase)
    print("The sentiment of this sentence is: ",  sentiment_score['pos']*100, "% Positive,", sentiment_score['neg']*100, "% Negative, ", sentiment_score['neu']*100, "% Neutral.")


#%%
if __name__ == "__main__":

    Word_Sentiment("phrase")



# %%
