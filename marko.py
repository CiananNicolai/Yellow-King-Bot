import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import markovify #Markov Chain Generator
import re
import spacy



def BibleLovecraftGrim():
    nlp = spacy.load("en_core_web_sm") #python -m spacy download en

    inp = pd.read_csv('t_asv.csv')
    inp.head(3)

    with open("concat.txt", encoding="utf8") as f:
        inp2 = f.read()

    with open("grimmstales.txt", encoding="utf8") as f:
        inp3 = f.read()

    class POSifiedText(markovify.Text):
        def word_split(self, sentence):
            return ["::".join((word.orth_, word.pos_)) for word in nlp(sentence)]

        def word_join(self, words):
            sentence = " ".join(word.split("::")[0] for word in words)
            return sentence

    model_a = markovify.Text(inp.t, state_size = 2)
    model_b = markovify.Text(inp2, state_size = 2)
    model_c = markovify.Text(inp3, state_size = 2)

    model_combo = markovify.combine([model_a, model_b, model_c], [0.5, 1.5,1])


    #for i in range(1):
        #for i in range(3):
            
    result1 = model_combo.make_short_sentence(50,tries=40)
    result2 = model_combo.make_short_sentence(50,tries=40)
    result3 = model_combo.make_short_sentence(50,tries=40)

    return result1,result2,result3

