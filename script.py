import utils
import sorts

bookshelf = utils.load_books('books_small.csv')
long_bookshelf = utils.load_books('books_large.csv')

for book in bookshelf:
  print(book['title'])
  
print(ord("a"))
print(ord(" "))
print(ord("A"))

def by_title_ascending(book_a, book_b):
  if book_a["title_lower"] > book_b["title_lower"]:
    return True
  else:
    return False
  
def by_author_ascending(book_a, book_b):
  return book_a['author_lower'] > book_b['author_lower']

def by_total_lenght(book_a, book_b):
  return len(book_a['author_lower']) + len(book_a['title_lower']) > len(book_b['author_lower']) + len(book_b['title_lower'])
  
bookshelf_v1 = bookshelf[:]  
bookshelf_v2 = bookshelf[:]

#can use method built in copy()

sort_1 = sorts.bubble_sort(bookshelf, by_title_ascending)
for book in sort_1:
  print(book['title'])
  
sort_2 = sorts.bubble_sort(bookshelf_v1, by_author_ascending)
print("__________Sorting bubble authors__________")
for book in  sort_2:
  print(book['author'])
sorts.quicksort(bookshelf_v2, 0, len(bookshelf_v2) - 1,  by_author_ascending)
print("___________Sorting quicksort authors___________")
for book in bookshelf_v2:
  print(book['author'])
  
print("___Running quicksort by total_lenght ______")
#sorts.bubble_sort(long_bookshelf, by_total_lenght)
sorts.quicksort(long_bookshelf, 0 , len(long_bookshelf)-1,  by_total_lenght)
for book in long_bookshelf:
  tamanho_titulo = len(book['title'])
  tamanho_autor =  len(book['author'])
  total = tamanho_titulo + tamanho_autor
  
  print("{} letters for {}".format(total, book["title"]))

