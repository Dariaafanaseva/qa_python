import pytest
from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test

class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    names = ['', 'А', 'Гарри Поттер и филосовский камень и узни', 'Гарри Поттер и филосовский камень и узни',
             'Гарри Поттер и филосовский камень и узник']

    @pytest.mark.parametrize('name', names)
    def test_add_new_book_boundary_values_name(self, name):
        books_collector = BooksCollector()
        books_collector.add_new_book(name)
        assert name in books_collector.books_genre


    def test_set_book_genre_existent_book_name_positive_result(self):
        books_collector = BooksCollector()
        name = 'Гарри Поттер и филосовский камень'
        books_collector.add_new_book(name)
        books_collector.set_book_genre(name, 'Фантастика')
        assert name in books_collector.books_genre


    def test_get_book_genre_existent_name_true(self):
        books_collector = BooksCollector()
        name = 'Гарри Поттер и филосовский камень'
        books_collector.add_new_book(name)
        books_collector.set_book_genre(name, 'Фантастика')
        assert books_collector.get_book_genre(name) == 'Фантастика'

    def test_get_books_with_specific_genre_existent_genre_true(self):
        books_collector = BooksCollector()
        name = 'Гарри Поттер и филосовский камень'
        genre = 'Фантастика'
        books_collector.add_new_book(name)
        books_collector.set_book_genre(name, genre)
        assert books_collector.get_books_with_specific_genre(genre) == [name]

    def test_get_books_genre_existent_genre_and_name_true(self):
        books_collector = BooksCollector()
        name = 'Гарри Поттер и филосовский камень'
        genre = 'Фантастика'
        books_collector.add_new_book(name)
        books_collector.set_book_genre(name, genre)
        expected_result = {name: genre}
        assert books_collector.get_books_genre() == expected_result


    def test_get_books_for_children_book_for_adult_true(self):
        books_collector = BooksCollector()
        name = 'Дракула'
        genre = 'Ужасы'
        books_collector.add_new_book(name)
        books_collector.set_book_genre(name, genre)
        assert name not in books_collector.get_books_for_children()


    def test_add_book_in_favorites_existent_name_true(self):
        books_collector = BooksCollector()
        name = 'Дракула'
        genre = 'Ужасы'
        books_collector.add_new_book(name)
        books_collector.set_book_genre(name, genre)
        books_collector.add_book_in_favorites(name)
        assert name in books_collector.favorites

    def test_delete_book_from_favorites_existent_name_true(self):
        books_collector = BooksCollector()
        name = 'Дракула'
        genre = 'Ужасы'
        books_collector.add_new_book(name)
        books_collector.set_book_genre(name, genre)
        books_collector.add_book_in_favorites(name)
        books_collector.delete_book_from_favorites(name)
        assert name not in books_collector.favorites


    def test_get_list_of_favorites_books_existent_name_true(self):
        books_collector = BooksCollector()
        name = 'Дракула'
        genre = 'Ужасы'
        books_collector.add_new_book(name)
        books_collector.set_book_genre(name, genre)
        books_collector.add_book_in_favorites(name)
        assert books_collector.get_list_of_favorites_books() == [name]



