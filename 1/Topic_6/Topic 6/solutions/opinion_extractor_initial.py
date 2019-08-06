# coding: utf-8
def opinion_extractor(aspect_token,parsed_sentence):
    opinions = []
    for token in parsed_sentence:
        if token.pos_ == 'NOUN' and token.orth_ == aspect_token:
            for child in token.children:
                opinions.append(child.orth_)
    return opinions

def show_results(results,aspect_word):
    print("Results for aspect word '{}'\n".format(aspect_word))
    for word,sent,opinions in results:
        if word == aspect_word:
            print("Sentence:\n\t{}".format(sent))
            print("Opinion of '{0}':\n\t '{1}'".format(aspect_word,"', '".join(opinions)))
            print("\n")
                
aspect_words = ["plot","characters","cinematography","dialogue"]
   
results = [] 
for review in dvd_reviews[:200]:
    parsed_review = nlp(review)
    for sentence in parsed_review.sents:
        for aspect_token in aspect_words:
            opinions = opinion_extractor(aspect_token,sentence)
            if opinions:
                results.append((aspect_token,sentence.orth_,opinions))
                
show_results(results,"plot")
show_results(results,"characters")
show_results(results,"cinematography")
show_results(results,"dialogue")       
