

                                             #For this project, you’ll create a “word cloud” from a text by writing a script.
                             #This script needs to process the text, remove punctuation, count the frequencies, and ignore uninteresting or irrelevant words.
#use this to generate cloud image
cloud = wordcloud.WordCloud()
cloud.generate_from_frequencies(frequencies)
cloud.to_file("myfile.jpg")