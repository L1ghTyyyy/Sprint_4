Реализованные тесты

Тесты для add_new_book
	•	test_add_new_book_add_one_book – проверяет, что можно добавить одну книгу.
	•	test_add_new_book_add_two_books – проверяет добавление двух книг.
	•	test_add_duplicate_book – проверяет, что дубликаты книг не добавляются.
	•	test_add_new_book_too_long – проверяет, что книга с названием более 40 символов не добавляется.

Тесты для set_book_genre
	•	test_set_book_genre – проверяет успешную установку жанра.
	•	test_set_invalid_genre – проверяет, что нельзя установить жанр, которого нет в списке.

Тесты для get_books_with_specific_genre
	•	test_get_books_with_specific_genre – проверяет, что метод возвращает книги с заданным жанром.

Тесты для get_books_genre
	•	Покрывается в тестах test_add_new_book_add_one_book и test_add_new_book_add_two_books.

Тесты для get_books_for_children
	•	test_get_books_for_children – проверяет, что книги с возрастным рейтингом не попадают в список.

Тесты для add_book_in_favorites
	•	test_add_book_in_favorites – проверяет успешное добавление книги в избранное.

Тесты для delete_book_from_favorites
	•	test_delete_book_from_favorites – проверяет удаление книги из избранного.

Тесты для get_list_of_favorites_books
	•	test_get_list_of_favorites_books – проверяет, что список избранных книг сначала пуст, но заполняется при добавлении книг.