from main import BooksCollector

class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    def test_add_new_book_too_long(self):
        collector = BooksCollector()
        book_name = "Очень длинное название книги, превышающее 40 символов"
        collector.add_new_book(book_name)
        assert book_name not in collector.get_books_genre()

    def test_add_duplicate_book(self):
        collector = BooksCollector()
        book_name = "1984"
        collector.add_new_book(book_name)
        collector.add_new_book(book_name)
        assert len(collector.get_books_genre()) == 1

    def test_set_book_genre(self):
        collector = BooksCollector()
        book_name = "1984"
        genre = "Фантастика"
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.get_book_genre(book_name) == genre

    def test_set_invalid_genre(self):
        collector = BooksCollector()
        book_name = "Незнайка"
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, "Приключения")
        assert collector.get_book_genre(book_name) == ""

    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()
        collector.add_new_book("Гарри Поттер")
        collector.set_book_genre("Гарри Поттер", "Фантастика")
        assert collector.get_books_with_specific_genre("Фантастика") == ["Гарри Поттер"]

    def test_get_books_for_children(self):
        collector = BooksCollector()
        collector.add_new_book("Король Лев")
        collector.set_book_genre("Король Лев", "Мультфильмы")
        collector.add_new_book("Оно")
        collector.set_book_genre("Оно", "Ужасы")
        assert "Оно" not in collector.get_books_for_children()
        assert "Король Лев" in collector.get_books_for_children()

    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book("Гарри Поттер")
        collector.add_book_in_favorites("Гарри Поттер")
        assert "Гарри Поттер" in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book("Гарри Поттер")
        collector.add_book_in_favorites("Гарри Поттер")
        collector.delete_book_from_favorites("Гарри Поттер")
        assert "Гарри Поттер" not in collector.get_list_of_favorites_books()

    def test_get_list_of_favorites_books(self):
        collector = BooksCollector()
        collector.add_new_book("Гарри Поттер")
        collector.add_new_book("Дюна")
        collector.add_book_in_favorites("Гарри Поттер")
        assert collector.get_list_of_favorites_books() == ["Гарри Поттер"]
