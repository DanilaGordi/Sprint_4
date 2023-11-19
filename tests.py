import pytest
from main import BooksCollector

class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        assert len(collector.get_books_genre()) == 2


    def test_add_new_book_empty_book(self):
        # Тест на отсутствие книги
        collector = BooksCollector()
        book_name = ""
        collector.add_new_book(book_name)
        assert book_name not in collector.get_books_genre()

    def test_add_add_new_book_long_book_name(self):
        # Тест на длинное название
        collector = BooksCollector()
        book_name = "КакоеТоДлинноеНазваниеДляКнигиБольше41Символов"
        collector.add_new_book(book_name)
        assert book_name not in collector.get_books_genre()

    def test_set_book_genre_fantasy_book(self):
        # Тест на установку жанра для книги
        collector = BooksCollector()
        collector.add_new_book("Мастер и Маргарита")
        collector.set_book_genre("Мастер и Маргарита", "Фантастика")
        result = collector.get_book_genre("Мастер и Маргарита")
        assert result == "Фантастика"

    @pytest.mark.parametrize("book_name, genre", [
        ("Мастер и Маргарита", "Фантастика"),
        ("Тихий Дон", "Драма"),
        ("Оно", "Ужасы"),
    ])

    def test_get_book_genre_by_name(self, book_name, genre):
        # Тест на достоверонсть получения жанра книги по её имени
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        result = collector.get_book_genre(book_name)
        assert result == genre

    def test_books_for_children_include_non_age_rated_books(self):
        # Проверка, что книги без возрастного рейтинга попадают в список книг для детей
        collector = BooksCollector()
        collector.add_new_book("Сказки")
        collector.set_book_genre("Сказки", "Мультфильмы")
        result = collector.get_books_for_children()
        assert "Сказки" in result

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
        collector.add_new_book("Cказки")
        collector.set_book_genre("Сказки", "Мультфильмы")
        result = collector.get_books_with_specific_genre("Мультфильмы")
        assert result == ["Сказки"]

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


