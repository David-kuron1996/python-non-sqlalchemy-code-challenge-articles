class Author:
    def __init__(self, name):
        self._name = name
        self._articles = []
        self._magazines = []
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        if len(value) == 0:
            raise ValueError("Name cannot be empty")
        self._name = value
    
    def articles(self):
        return self._articles
    
    def magazines(self):
        return self._magazines
    
    def add_article(self, magazine, title):
        article = Article(self, magazine, title)
        self._articles.append(article)
        if magazine not in self._magazines:
            self._magazines.append(magazine)
        return article
    
    def topic_areas(self):
        topics = list(set([magazine.category for magazine in self._magazines]))
        return topics