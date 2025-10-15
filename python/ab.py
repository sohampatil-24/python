from abc import ABC, abstractmethod

class MovieClassifier(ABC):

    @abstractmethod
    def classify(self, movie_title: str) -> str:
        pass

class SimpleGenreClassifier(MovieClassifier):

    def classify(self, movie_title: str) -> str:
        if "pk" in movie_title or "pk" in movie_title:
            return "funny"
        elif "alone" in movie_title or "alone" in movie_title:
            return "Horror"
        else:
            return "Action"

if __name__ == "__main__":

    classifier = SimpleGenreClassifier()

    movie_1 = "pk"
    movie_2 = "alone"
    movie_3 = "kantara"

    print(f"Movie: {movie_1}, Category: {classifier.classify(movie_1)}")
    print(f"Movie: {movie_2}, Category: {classifier.classify(movie_2)}")
    print(f"Movie: {movie_3}, Category: {classifier.classify(movie_3)}")
