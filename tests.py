import pytest
from main import BooksCollector

class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        assert len(collector.get_books_genre()) == 2

    @pytest.mark.parametrize("book_name, expect", [
        ("", False),
        ("A", True),
        ("AB", True),
        ("A" * 39, True),
        ("A" * 40, True),
        ("A" * 41, False),
        ("A" * 42, False)
    ])
    def test_add_new_book_different_length_book_name(self, book_name, expect):
        # тест на размер названия книги
        collector = BooksCollector()
        collector.add_new_book(book_name)
        assert (book_name in collector.get_books_genre()) == expect

    def test_set_book_genre_fantasy_book(self):
        # Тест на установку жанра для книги
        collector = BooksCollector()
        collector.add_new_book("Мастер и Маргарита")
        collector.set_book_genre("Мастер и Маргарита", "Фантастика")
        result = collector.get_book_genre("Мастер и Маргарита")
        assert result == "Фантастика"

    def test_get_book_genre_by_name(self):
        # Тест на достоверонсть получения жанра книги по её имени
        collector = BooksCollector()
        book_name = "Мастер и Маргарита"
        genre = "Фантастика"

        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        result = collector.get_book_genre(book_name)

        assert result == genre

    def test_books_for_children_include_non_age_rated_books(self):
        # Проверка, что книги без возрастного рейтинга попадают в список книг для детей
        collector = BooksCollector()
        children_books = {
            "Сказки Пушкина": "Мультфильмы",
            "Юмористические рассказы": "Комедии",
            "Метро 2033": "Фантастика"
        }

        for book, genre in children_books.items():
            collector.add_new_book(book)
            collector.set_book_genre(book, genre)

        assert collector.get_books_for_children() == ['Сказки Пушкина', 'Юмористические рассказы', 'Метро 2033']

    def test_books_for_children_exclude_age_rated_books(self):
        # Проверка, что книги с возрастным рейтингом не попадают в список книг для детей
        collector = BooksCollector()
        collector.add_new_book("Оно")
        collector.set_book_genre("Оно", "Ужасы")
        result = collector.get_books_for_children()
        assert "Оно" not in result

    def test_add_book_without_genre(self):
        # Тест на проверку, что у добавленной книги нет жанра без присвоения
        collector = BooksCollector()
        collector.add_new_book("Война и мир")
        assert collector.get_book_genre("Война и мир") == ""

    def test_get_books_with_specific_genre_by_book(self):
        # Тест на получение списка книг с заданным жанром
        collector = BooksCollector()
        books_data = {
            "Мастер и Маргарита": "Фантастика",
            "Тихий Дон": "Драма",
            "Оно": "Ужасы",
            "Война и мир": "История"
        }

        for book, genre in books_data.items():
            collector.add_new_book(book)
            collector.set_book_genre(book, genre)

        result = collector.get_books_with_specific_genre("Ужасы")
        assert result == ["Оно"]

    def test_get_books_genre_by_book(self):
        # Тест на получение текущего словаря по книге
        collector = BooksCollector()
        collector.add_new_book("Колобок")
        collector.set_book_genre("Колобок", "Мультфильмы")
        result = collector.get_books_genre()
        assert result == {"Колобок": "Мультфильмы"}

    def test_add_book_in_favorites_one_favorite_book(self):
        # тест на добавление книги в избранное
        collector = BooksCollector()
        collector.add_new_book("Анна Каренина")
        collector.add_book_in_favorites("Анна Каренина")
        result = collector.get_list_of_favorites_books()
        assert "Анна Каренина" in result

    def test_delete_book_from_favorites_one_favorite_book(self):
        # тест на удаление книги из избранного
        collector = BooksCollector()
        collector.add_new_book("Братья Карамазовы")
        collector.add_book_in_favorites("Братья Карамазовы")
        collector.delete_book_from_favorites("Братья Карамазовы")
        result = collector.get_list_of_favorites_books()
        assert "Братья Карамазовы" not in result


