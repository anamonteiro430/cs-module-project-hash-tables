import re


def word_count(s):
    cache={}

    s = s.lower()
    print(s)
    s_list = re.findall(r"[\w']+|[ª]", s)
    print("SLIST", s_list)
    for word in s_list:
        if word in cache:
            cache[word] += 1
        else:
            cache[word] = 1
    items = list(cache.items())
    print(items) 
    return cache




if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))