import spacy

nlp = spacy.load('en_core_web_md')

# read the movies.txt file
movie_list = []
with open("movies.txt", "r") as file:
    for line in file:
        movie_list.append(line)

def movie_finder(description):
    model_sentence = nlp(description)
    most_similar = 0
    similarity = 0
    movie_index = 0

    # find the most similar movie
    for i in range(len(movie_list)):
        similarity = nlp(movie_list[i]).similarity(model_sentence)
        if similarity > most_similar:
            most_similar = similarity
            movie_index = i

    # return movie name
    return movie_list[movie_index][0:8]

summary = input("Please enter description of movie: ")
print(movie_finder(summary))

# recognise which movive's summary