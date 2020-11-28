# <codecell>
# module imports
import os
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
import string

# <codecell>
# import the data
full_string = ""
data_directory = os.path.abspath("./")+ "\\data"

for filename in os.listdir(data_directory):
	filename = "data/"+filename
	f = open(filename, "r")
	full_string += f.read()

# <codecell>
# sanitise the full string
full_string = full_string.translate(str.maketrans('', '', string.punctuation))
full_string = full_string.lower()

# <codecell>
# Generate the word cloud from full_string
stopwords = set(STOPWORDS)
wordcloud = WordCloud(width=800, height=800, background_color="black", stopwords=stopwords).generate_from_text(full_string)

# <codecell>
# Plot the worrd cloud
plt.figure(figsize = (8, 8), facecolor = None) 
plt.imshow(wordcloud) 
plt.axis("off") 
plt.tight_layout(pad = 0) 
  
plt.show()