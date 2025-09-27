### Problem-10: Most Frequent Word (Excluding Stopwords)
# Analyze blog content and find the most frequent word, excluding common stopwords.
#-   **Hint**: Clean punctuations, lowercase all, use `Counter`.

import string
from collections import Counter

content_text = """The optimization of avoidance behaviors in response to stress is an instinctual life function 
universally present in animals. In many sexually dimorphic animals, males exhibit higher stress resistance than 
females, but there have been no reports of comparative studies on stress resistance in sexually dimorphic 
hermaphrodites capable of reproducing alone. In the present study, we aimed to utilize a reversal/turn behavioral 
choice to conduct a comparative analysis of optimized avoidance behavior patterns in hermaphrodite and male 
Caenorhabditis elegans. We found that C. elegans males showed greater resistance to physical movement under 
acute stress and to lifespan reduction under chronic stress than C. elegans hermaphrodites. Interestingly, males 
exhibited a stronger avoidance behavior pattern known as “turn” than did the hermaphrodites, even in response to 
mild acute stress stimuli, to which they responded as if they had been exposed to strong stimuli. Stress conditions 
can lead to unsuccessful mating in C. elegans, and exaggerated stress avoidance in males may have biological 
significance for successful mating. This sexual dimorphism in avoidance behavior optimization was attributed to 
neural circuits downstream of the AIB neurons, the center of turn behavior, suggesting the presence of a novel 
mechanism distinct from previously reported neural and molecular mechanisms of avoidance behavior optimization"""

content_text = content_text.lower()
stop_words = set([
    'i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've",
    "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his',
    'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself',
    'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom',
    'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be',
    'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a',
    'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at',
    'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during',
    'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on',
    'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when',
    'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other',
    'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very',
    's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd',
    'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn',
    "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't",
    'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't",
    'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won',
    "won't", 'wouldn', "wouldn't"
])

translator = str.maketrans('', '', string.punctuation)
text_no_punc = content_text.translate(translator)
splited_text= content_text.split()

filterd_words = [ words for words in splited_text if words not in stop_words]
word_counts = Counter(filterd_words)
most_common_word, most_common_count = word_counts.most_common(1)[0]
print(f"The most frequent word is '{most_common_word}' which appears {most_common_count} times.")



