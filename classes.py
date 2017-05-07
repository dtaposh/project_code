import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet

class Sentence:
    token=[]
    pos_tag=[]

    def lemmaFunc(self):
        lem=WordNetLemmatizer()
        temp_list=[]
        for i in range(len(self.pos_tag)):
            w=self.pos_tag[i]
            pos_temp=(w[1].lower())[0]
            if pos_temp == 'j':
                temp_list.append((lem.lemmatize(w[0], 'a'), 'a'))
            elif pos_temp == 'r':
                temp_list.append((lem.lemmatize(w[0], 'r'), 'r'))
            elif pos_temp == 'v':
                temp_list.append((lem.lemmatize(w[0], 'v'), 'v'))
            elif pos_temp == 'n':
                temp_list.append((lem.lemmatize(w[0], 'n'), 'n'))
            #temp_list.append((lem.lemmatize(w[0], 'n'),w[1]))
        return temp_list


    #CONSTRUCTOR
    def __init__(self, sentence):
        input_sentence = sentence
        self.token = nltk.word_tokenize(input_sentence)
        self.pos_tag = nltk.pos_tag(self.token)
        #print(self.token)
        self.pos_tag = self.lemmaFunc()
        print(self.pos_tag)
        self.sim_mat=[]

    def check_similarity(self,source):
        test=0
        plag_value=0
        for word1 in self.pos_tag:
            for word2 in source.pos_tag:
                if word1[1] == word2[1]:
                    syn1 = wordnet.synsets(word1[0])
                    syn2 = wordnet.synsets(word2[0])
                    max_sim=0
                    for s1 in syn1:
                        for s2 in syn2:
                            sim=s1.wup_similarity(s2)
                            if sim != None and sim>max_sim:
                                max_sim=sim
                    print(max_sim);
                    test+=1
                    plag_value+=max_sim
        print("\nplag val: "+str(plag_value/test))
