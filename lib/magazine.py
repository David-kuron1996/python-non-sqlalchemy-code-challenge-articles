class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category
        self._articles = []
        self._contributors = []
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        if not (2 <= len(value) <= 16):
            raise ValueError("Name must be between 2 and 16 characters")
        self._name = value
    
    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, value):
        if not isinstance(value, str):
            raise TypeError("Category must be a string")
        if len(value) == 0:
            raise ValueError("Category cannot be empty")
        self._category = value
    
    def articles(self):
        return self._articles
    
    def contributors(self):
        return self._contributors
    
    def article_titles(self):
        return [article.title for article in self._articles]
    
    def contributing_authors(self):
        return [author for author in self._contributors 
                if len([a for a in self._articles if a.author == author]) > 1]