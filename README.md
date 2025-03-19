# Реализованные тесты  

## Тесты для `add_new_book`  
- **`test_add_new_book_add_one_book`** – проверяет, что можно добавить одну книгу.  
- **`test_add_new_book_add_two_books`** – проверяет добавление двух книг.  
- **`test_add_duplicate_book`** – проверяет, что дубликаты книг не добавляются.  
- **`test_add_new_book_too_long`** – проверяет, что книга с названием более 40 символов не добавляется.  

## Тесты для `set_book_genre`  
- **`test_set_book_genre`** – проверяет успешную установку жанра для книги.  
- **`test_set_invalid_genre`** – проверяет, что нельзя установить несуществующий жанр.  
- **`test_set_genre_for_nonexistent_book`** – проверяет, что нельзя установить жанр для книги, которой нет в словаре.  

## Тесты для `get_book_genre`  
- **`test_get_book_genre`** – проверяет, что метод возвращает установленный жанр книги.  
- **`test_get_book_genre_for_nonexistent_book`** – проверяет, что для несуществующей книги возвращается `None`.  

## Тесты для `get_books_with_specific_genre`  
- **`test_get_books_with_specific_genre`** – проверяет, что метод возвращает список книг заданного жанра.  
- **`test_get_books_with_nonexistent_genre`** – проверяет, что метод возвращает пустой список для жанра, которого нет в словаре.  

## Тесты для `get_books_genre`  
- **`test_get_books_genre`** – проверяет, что метод возвращает словарь всех книг с их жанрами.  

## Тесты для `get_books_for_children`  
- **`test_get_books_for_children`** – проверяет, что книги с возрастным рейтингом не попадают в список.  

## Тесты для `add_book_in_favorites`  
- **`test_add_book_in_favorites`** – проверяет успешное добавление книги в избранное.  
- **`test_add_nonexistent_book_in_favorites`** – проверяет, что нельзя добавить в избранное книгу, которой нет в словаре.  
- **`test_add_duplicate_book_in_favorites`** – проверяет, что одна и та же книга не добавляется в избранное дважды.  

## Тесты для `delete_book_from_favorites`  
- **`test_delete_book_from_favorites`** – проверяет удаление книги из избранного.  
- **`test_delete_nonexistent_book_from_favorites`** – проверяет, что удаление несуществующей книги из избранного не вызывает ошибок.  

## Тесты для `get_list_of_favorites_books`  
- **`test_get_list_of_favorites_books`** – проверяет, что метод возвращает список избранных книг.  
- **`test_get_list_of_favorites_books_empty`** – проверяет, что при отсутствии избранных книг метод возвращает пустой список.  