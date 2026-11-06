# Cara 1: import module_name
import book_functions
book_functions.favorite_book("Laskar Pelangi")

# Cara 2: from module_name import function_name
from book_functions import favorite_book
favorite_book("Bumi")

# Cara 3: from module_name import function_name as fn
from book_functions import favorite_book as fb
fb("Dilan 1990")

# Cara 4: import module_name as mn
import book_functions as bf
bf.favorite_book("Filosofi Kopi")

# Cara 5: from module_name import *
from book_functions import *
favorite_book("Hujan")