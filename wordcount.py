def words(phrase):
        occurs= {}  

        for w in phrase.split():
                occurs[w] = occurs.get(w, 0) +1
                
        for w,c in occurs.items():
            return ("%s: %d times" % (w,c))

