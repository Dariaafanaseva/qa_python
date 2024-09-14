import pytest


from main import BooksCollector
names = ['', 'А', 'Гарри Поттер и филосовский камень и узни', 'Гарри Поттер и филосовский камень и узни', 'Гарри Поттер и филосовский камень и узник']
@pytest.mark.parametrize('name', names)
class TestBooksCollector:
    def test_add_new_book_boundary_values_name(self, name):
        books_collector = BooksCollector()
        books_collector.add_new_book(name)
        assert name in books_collector.books_genre




