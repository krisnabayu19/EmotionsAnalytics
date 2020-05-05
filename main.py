import string
from collections import Counter
import pandas as pd
import operator
import matplotlib.pyplot as plt

from collections import UserList
import sumpy
import numpy as np


# reading text file
text = open("read.txt", encoding="utf-8").read()

# converting to lowercase
lower_case = text.lower()

# Removing punctuations
cleaned_text = lower_case.translate(str.maketrans('', '', string.punctuation))

# splitting text into words
tokenized_words = cleaned_text.split()

stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
              "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
              "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
              "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
              "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
              "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
              "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
              "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
              "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
              "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

# Removing stop words from the tokenized words list
final_words = []
for word in tokenized_words:
    if word not in stop_words:
        final_words.append(word)

# NLP Emotion Algorithm
# 1) Check if the word in the final word list is also present in emotion.txt
#  - open the emotion file
#  - Loop through each line and clear it
#  - Extract the word and emotion using split

# 2) If word is present -> Add the emotion to emotion_list
# 3) Finally count each emotion in the emotion list

emotion_list = []
with open('indoemotions.txt', 'r') as file:
    for line in file:
        clear_line = line.replace("\n", '').replace(",", '').replace("'", '').strip()
        word, emotion = clear_line.split(':')

        if word in final_words:
            emotion_list.append(emotion)

print("Clean Text :", text)
print("Lower Case Text :", lower_case)
print("Tokenized Text : ", final_words)
print("Emotions List :", emotion_list)
# print(word)

# Count Emotions
emotion_word = Counter(emotion_list)
count_emotion = pd.Series(emotion_word)


# Sum from Count Emotions
sum_emotion = sum(count_emotion)
# print(sum_emotion)

# Create Calculation Emotions
percent_emotion = (count_emotion / sum_emotion)
print("Klasifikasi Tingkat Emosi :")
print(percent_emotion)
print("=========================================")

# Compare Emotions
compare_emotion = max(percent_emotion.iteritems(), key=operator.itemgetter(1))[0]
print("Emosi Terdeteksi :",compare_emotion)

# Visualization Grafik Emotions
fig, ax1 = plt.subplots()
ax1.bar(emotion_word.keys(), percent_emotion)
fig.autofmt_xdate()
plt.savefig('graph.png')
plt.show()