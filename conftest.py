
from main import BooksCollector


@pytest.fixture
def books_dict():
    collector = BooksCollector()
    collector.add_new_book('1984')
    collector.set_book_genre('1984', 'Фантастика')
    collector.add_new_book('Сияние')
    collector.set_book_genre('Сияние', 'Ужасы')
    collector.add_new_book('Шерлок Холмс')
    collector.set_book_genre('Шерлок Холмс', 'Детективы')
    collector.add_new_book('Винни-Пух')
    collector.set_book_genre('Винни-Пух', 'Мультфильмы')
    collector.add_new_book('Ревизор')
    collector.set_book_genre('Ревизор', 'Комедии')
    return collector


@pytest.fixture
def favorites_books(books_dict):
    books_dict.add_book_in_favorites('1984')
    books_dict.add_book_in_favorites('Сияние')
    return books_dict.favorites
