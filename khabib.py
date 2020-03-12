from PIL import Image
# %matplotlib inline
import matplotlib as mpl
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
import numpy as np



# print('Imported')

quote = open('khabib.txt', 'r').read()

print ('File downloaded and saved!')

stopwords = set(STOPWORDS)

# Setting up redundant stopwords
stopwords.add('Khabib')
stopwords.add('Nurmagomedov')
stopwords.add('quote')

khabib = np.array(Image.open('khabib.jpg'))

print('Image downloaded and saved!')

# instantiating a word cloud object
khabib_wc = WordCloud(
    background_color='white',
    max_words=2000,
    stopwords=stopwords
)


# generating the word cloud
khabib_wc.generate(quote)


# display the word cloud
plt.imshow(khabib_wc, interpolation='bilinear')
plt.axis('off')
plt.savefig('khabib_wc.png',bbox_inches='tight',dpi = 1200)
plt.show()

