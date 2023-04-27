# The list is a circle with 100 cats (number of cats can be changed)
# False means there is no hat on the cat; True - cat has hat
cats = [False for i in range(0, 100)]


def put_on_take_off(hat_presence: bool):
    if hat_presence:
        return False
    else:
        return True


def cats_hats(cats_list: list) -> list:
    k = 1
    for i in range(0, len(cats_list)):
        cats_list = [put_on_take_off(cats_list[j-1]) if j % k == 0 else cats_list[j-1] for j in range(1, len(cats_list) + 1)]
        k += 1
    return cats_list


print(cats_hats(cats))
for i in range(0, len(cats_hats(cats))):
    if cats_hats(cats)[i]:
        print(f"Cat number {i + 1} HAS a HAT")
    else:
        print(f"Cat number {i+1} doesn't have any hat(((")


"""Quick sort algorythm:
def quick_sort(list_):
    if len(list_) < 2:
        return list_
    else:
        pivot = list_[0]
        less = [i for i in list_[1:] if i <= pivot]
        greater = [i for i in list_[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)
Береться опорний рандомний елемент колекції і порівнюється з іншими і в залежності від цього порівняння колекція 
ділиться на дві: з елементами більшими за нього і меншими. Далі рекурсивно це робиться з кожною з утворених підколекцій, 
доки в утвореній колекції не залишиться один елемент, що стоятиме на своєму місці. 
Середня складність O(n log n), максимальна - O(n^2)
"""