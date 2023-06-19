def is_polindrom(word):
    print(word[::-1])
    return word.strip() == word[::-1].strip()



if __name__ == "__main__":
    print(is_polindrom('лепсспел'))
