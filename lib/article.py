class Article:
    all = []
    
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)
        
        # Add article to author's list
        if self not in author._articles:
            author._articles.append(self)
        
        # Add article to magazine's list
        if self not in magazine._articles:
            magazine._articles.append(self)
        
        # Add author to magazine's contributors if not already there
        if author not in magazine._contributors:
            magazine._contributors.append(author)