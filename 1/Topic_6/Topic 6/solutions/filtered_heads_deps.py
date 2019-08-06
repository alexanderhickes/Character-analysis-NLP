# coding: utf-8
unwanted_head_deps = ['pobj', 'attr', 'pobj']
unwanted_head_lemmas = ['be','have','do']
unwanted_head_pos = ['PROPN']
unwanted_dependent_deps = ['det', 'predet','nummod', 'cc', 'prep', 'punct', 'case']
unwanted_dependent_pos = ['SPACE','PROPN']
unwanted_dependent_lemmas = ['-PRON-','do','be']

def uninteresting_head(token):
    return token.dep_ in unwanted_head_deps or token.head.lemma_ in unwanted_head_lemmas

def uninteresting_dep(token):
    return token.dep_ in unwanted_dependent_deps or token.pos_ in unwanted_dependent_pos or token.lemma_ in unwanted_dependent_lemmas

aspect_words = ["plot","characters","cinematography","dialogue"]
linked_words = defaultdict(lambda: defaultdict(list)) 
for review in dvd_reviews:
    parsed_review = nlp(review)
    for token in parsed_review:
        if token.pos_ == 'NOUN' and token.orth_ in aspect_words:
            if not uninteresting_head(token): 
                linked_words[token.orth_]["heads"].append((token.head.orth_,token.head.pos_,token.dep_,token.head.lemma_))
            for child in token.children:
                if not uninteresting_dep(child):
                    linked_words[token.orth_]["deps"].append((child.orth_,child.pos_,child.dep_,child.lemma_))
all_heads = [linked_words[word]["heads"] for word in aspect_words]
all_dependents = [linked_words[word]["deps"] for word in aspect_words]
df_heads = pd.DataFrame(list(zip_longest(*all_heads)),
                columns = aspect_words).applymap(lambda x: '' if x == None else x)
print("Heads")
display(df_heads)
df_deps = pd.DataFrame(list(zip_longest(*all_dependents)),
                columns = aspect_words).applymap(lambda x: '' if x == None else x)
print("Dependents")
display(df_deps)
