import codecs
content = "\u00bfCu\u00e1ntas calor\u00edas?"
with codecs.open("src/pages/country/spain/test_py.txt", "w", "utf-8") as f:
    f.write(content)
