class Article:
    all = []
    
    def __init__(self, author, magazine, title):
        if not isinstance(title, str) or len(title) < 5 or len(title) > 50:
            raise ValueError("Title must be a string between 5 and 50 characters")
        
        self._title = title
        self.author = author
        self.magazine = magazine
        Article.all.append(self)
    
    @property
    def title(self):
        return self._title
    
    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise ValueError("Author must be an instance of Author")
        self._author = value
    
    @property
    def magazine(self):
        return self._magazine
    
    @magazine.setter
    def magazine(self, value):
        if not isinstance(value, Magazine):
            raise ValueError("Magazine must be an instance of Magazine")
        self._magazine = value
    
    @classmethod
    def find_by_title(cls, title):
        for article in cls.all:
            if article.title == title:
                return article
        return None
    
    @classmethod
    def find_by_author(cls, author):
        return [article for article in cls.all if article.author == author]
    
    @classmethod
    def find_by_magazine(cls, magazine):
        return [article for article in cls.all if article.magazine == magazine]


class Author:
    all = []
    
    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Name must be a non-empty string")
        self._name = name
        Author.all.append(self)
    
    @property
    def name(self):
        return self._name
    
    def articles(self):
        return [article for article in Article.all if article.author == self]
    
    def magazines(self):
        return list(set([article.magazine for article in self.articles()]))
    
    def add_article(self, magazine, title):
        if not isinstance(magazine, Magazine):
            raise ValueError("Magazine must be an instance of Magazine")
        return Article(self, magazine, title)
    
    def topic_areas(self):
        if not self.articles():
            return None
        return list(set([magazine.category for magazine in self.magazines()]))


class Magazine:
    all = []
    
    def __init__(self, name, category):
        if not isinstance(name, str) or len(name) < 2 or len(name) > 16:
            raise ValueError("Name must be a string between 2 and 16 characters")
        if not isinstance(category, str) or len(category) == 0:
            raise ValueError("Category must be a non-empty string")
        
        self._name = name
        self._category = category
        Magazine.all.append(self)
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str) or len(value) < 2 or len(value) > 16:
            raise ValueError("Magazine name must be a string between 2 and 16 characters")
        self._name = value
    
    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError("Magazine category must be a non-empty string")
        self._category = value
    
    def articles(self):
        return [article for article in Article.all if article.magazine == self]
    
    def contributors(self):
        return list(set([article.author for article in self.articles()]))
    
    def article_titles(self):
        if not self.articles():
            return None
        return [article.title for article in self.articles()]
    
    def contributing_authors(self):
        authors_with_multiple_articles = []
        for author in self.contributors():
            if len([article for article in self.articles() if article.author == author]) > 2:
                authors_with_multiple_articles.append(author)
        
        if not authors_with_multiple_articles:
            return None
        return authors_with_multiple_articles