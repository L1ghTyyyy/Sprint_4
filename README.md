# Реализованные тесты  

## Тесты для `add_new_book`  
- **`test_add_new_book_add_one_book`** – проверяет, что можно добавить одну книгу.  
- **`test_add_new_book_add_two_books`** – проверяет добавление двух книг.  
- **`test_add_duplicate_book`** – проверяет, что дубликаты книг не добавляются.  
- **`test_add_new_book_too_long`** – проверяет, что книга с названием более 40 символов не добавляется.  

## Тесты для `set_book_genre`  
- **`test_set_book_genre`** – проверяет успешную установку жанра для книги.  
- **`test_set_invalid_genre`** – проверяет, что нельзя установить несуществующий жанр.  

## Тесты для `get_book_genre`  
- **`test_get_book_genre`** – проверяет, что метод возвращает установленный жанр книги.  
- **`test_get_book_genre_for_nonexistent_book`** – проверяет, что для несуществующей книги возвращается `None`.  

## Тесты для `get_books_genre`  
- **`test_get_books_genre`** – проверяет, что метод возвращает словарь всех книг с их жанрами.  

## Тесты для `get_books_for_children`  
- **`test_get_books_for_children_contains_valid_books`** – проверяет, что в список попадают только книги без возрастных ограничений.  
- **`test_get_books_for_children_excludes_non_children_books`** – проверяет, что книги с возрастными ограничениями не попадают в список.  

## Тесты для `add_book_in_favorites`  
- **`test_add_book_in_favorites`** – проверяет успешное добавление книги в избранное.  

## Тесты для `delete_book_from_favorites`  
- **`test_delete_book_from_favorites`** – проверяет удаление книги из избранного.  

## Тесты для `get_list_of_favorites_books`  
- **`test_get_list_of_favorites_books_contains_added_book`** – проверяет, что метод возвращает список избранных книг.  
- **`test_get_list_of_favorites_books_does_not_contain_non_favorite_books`** – проверяет, что в список избранного не попадают не добавленные туда книги.  