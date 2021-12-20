graph = {}
graph['you'] = ['alice', 'bob', 'claire']
graph['bob'] = ['anuj', 'peggy']
graph['alice'] = ['peggy']
graph['claire'] = ['thom', 'jonny']
graph['anuj'] = []
graph['peggy'] = []
graph['thom'] = []
graph['jonny'] = []
from collections import deque

def person_is_seller(name):
    return name[0] == 'd'

def search(name):
    search_queue = deque() # Создание новой очереди
    search_queue += graph[name] # Все соседи добавляются в очередь поиска
    searched = [] # Этот массив используется для отслеживания уже проверенных людей
    while search_queue: # Пока очередь пуста
        person = search_queue.popleft() # Из очереди излекается первый человек
        if not person in searched: # Человек проверяется только в том случае если он не проверялся ранее
            if person_is_seller(person): # Проверяем является ли он продовцом манго
                print(person + ' is a mango seller!') # Да это продавец манго
                return True
            else:
                search_queue += graph[person] # Нет не является. Все друзья этого человека добавляются в очередь поиска
                searched.append(person) # Человек помечается как проверенный

    return False # Если выполнение дошло до этой строки, значит, в очереди нет продавца манго


search('you')

