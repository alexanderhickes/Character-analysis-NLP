# coding: utf-8
aspect_words = ["plot","characters","cinematography","dialogue"]
linked_words = defaultdict(lambda: defaultdict(list)) 
for review in dvd_reviews:
    parsed_review = nlp(review)
    for token in parsed_review:
        if token.pos_ == 'NOUN' and token.orth_ in aspect_words:
            linked_words[token.orth_]["heads"].append((token.head.orth_,token.head.lemma_,token.head.pos_,token.dep_))
            for child in token.children:
                linked_words[token.orth_]["deps"].append((child.orth_,child.lemma_,child.pos_,child.dep_))
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
