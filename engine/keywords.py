from summa import keywords

def main(*args):
    
    
    
    TR_keywords = keywords.keywords(full_text, scores=True)
    print(TR_keywords[0:10])
    
if __name__ == '__main__':
    main()