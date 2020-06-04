def no_dups(s):
    cache={}
    s = s.split()
    
    for word in s:
        print("WORD", word)
        if word in cache:
            print("REMOVING", word)
            s.remove(word)
            print("STRING NOW", s)
            print("CACHE NOW", cache)
        else:
            cache[word] = 1 
    result = " ".join(cache.keys())
    return result
    
    



if __name__ == "__main__":
    ''' print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs")) '''
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))