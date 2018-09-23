import re


def main():
    file_name = "Development Set.txt"
    f = open(file_name, "r")
    article = str(f.read())

    # Print Counts
    get_word_count(article)
    get_para_count(article)
    sentences = get_sentences(article)

    # Print words starting with
    print("Sentences Starting = ", first(sentences, 'generally'))

    # Print words ending with
    print("Sentences Ending = ", last(sentences, 'activities'))

    # count number of words
    words = bag_of_words(article)
    count_matching_word(words, 'dr')


def get_word_count(s):
    words = re.findall(r'\S+', s)
    print("Number of words = ", len(words))
    return None


def get_para_count(s):
    s = s.strip()
    count = 0
    for i in range(len(s)):
        if s[i] == '\n' and s[i + 1] == '\n':
            count += 1
            while i < len(s) and s[i + 1] == '\n':
                i += 1
            if (i >= len(s)):
                count -= 1
    count += 1
    print("The Number of paragraphs are = ", count)
    return None


def get_words(s):
    words = re.findall(r'\S+', s)
    print(len(words))
    return words


def first(sentences, s):
    a = 0
    for sentence in sentences:
        my_list = sentence.split()
        if my_list[0].lower() == s.lower():
            a += 1
    return a


def last(sentences, s):
    a = 0
    for sentence in sentences:
        my_list = sentence.split()
        if my_list[len(my_list) - 1].lower() == s.lower() or my_list[len(my_list) - 1].lower()[:-1] == s.lower():
            a += 1
    return a


def get_sentences(s):
    s = s.replace('\n', ' ')
    x = re.findall(r'[A-Za-z][^.!?]*[.!?]\s*', s)  # sentences starting with numbers missing
    sentences = []
    temp = ''
    i = 0
    while i < len(x):  # removes Dr, ms, mr
        temp = x[i]
        if i < len(x) - 1 and (x[i + 1][0:3].lower() == 'com' or x[i].strip()[-3:].lower() == 'dr.' or x[i].strip()[
                                                                                                       -2:].lower() == 'mr' or
                               x[i].strip()[-2:].lower() == 'ms' or x[i].strip()[-3:].lower() == 'mr.' or x[i].strip()[
                                                                                                          -3:].lower() == 'ms.'):
            temp = x[i] + x[i + 1]
            i += 1
        sentences.append(temp)
        i += 1

    i = 0
    final = []
    temp = ''
    while i < len(sentences):  # removes abbreviations
        temp = sentences[i]
        if i < len(sentences) - 1 and len(sentences[i + 1].strip()) <= 2:
            while i < len(sentences) - 1 and len(sentences[i + 1].strip()) <= 2:
                temp = temp + sentences[i + 1]
                i += 1
        final.append(temp)
        i += 1
    print("Number of sentences = ", len(final))
    # for i in final:
    #     print(i)
    return final


def bag_of_words(s):
    bag_of_lines = [line.strip() for line in s.splitlines()]
    bag_of_words = []
    for line in bag_of_lines:
        bag = line.split()
        for word in bag:
            w = word.strip()
            w = re.sub(r'[^\w\s]', '', w)
            bag_of_words.append(w.strip())

    # print(len(bag_of_words))
    return bag_of_words


def count_matching_word(bag_of_words, word):
    count = 0
    for w in bag_of_words:
        if w.lower() == word.lower():
            count += 1
    print("The number of matching words = ", count)
    return count


main()
