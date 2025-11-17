class Article:
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title

class Author:
    def __init__(self, name):
        self.name = name
        self.authored_articles = []  # Track articles by this author

    def articles(self):
        return self.authored_articles

    def magazines(self):
        # Get unique magazines the author has written for
        return list(set(article.magazine for article in self.authored_articles))

    def add_article(self, magazine, title):
        article = Article(self, magazine, title)
        self.authored_articles.append(article)
        magazine.magazine_articles.append(article)  # Add to magazine's articles

    def topic_areas(self):
        # Get unique categories of magazines the author has written for
        return list(set(article.magazine.category for article in self.authored_articles))

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category
        self.magazine_articles = []  # Track articles in this magazine

    def articles(self):
        return self.magazine_articles

    def contributors(self):
        # Get unique authors who have written for this magazine
        return list(set(article.author for article in self.magazine_articles))

    def article_titles(self):
        # Get titles of all articles in this magazine
        return [article.title for article in self.magazine_articles]

    def contributing_authors(self):
        # Get authors with more than two articles in this magazine
        author_counts = {}
        for article in self.magazine_articles:
            author = article.author
            author_counts[author] = author_counts.get(author, 0) + 1
        return [author for author, count in author_counts.items() if count > 1]