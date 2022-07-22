#%%
import requests
from lxml import html

#%%
def word_definition(word):
    response = requests.get("https://www.merriam-webster.com/dictionary/{}".format(word))
    tree = html.fromstring(response.text)
    title = tree.xpath('//title/text()')
    print(title)

    #definition = tree.xpath('//*[@id="dictionary-entry-1"]/div[2]/div[1]/span/div/span[2]/span/text()')
    definition = tree.xpath('//*[@id="dictionary-entry-1"]/div[2]/div[1]/span[1]/div/span[2]/span/text()')
    definition = ''.join(definition)
    print(definition)

    #definition = definition.split('\n')
    #definition = [d for d in definition if d]
    #for d in definition:
    #    print(d)

    
# %%
#issues with the word 'portal'
#a href tags within span thus xpath does not grab text
word_definition('portal')
# %%
if __name__ == "__main__":

    word_definition("basketball")
