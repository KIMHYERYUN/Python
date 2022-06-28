#lists(중첩리스트) : 두개이상의 list가 관계는 있으나 분리하고 싶은 경우
#list =[A, B]
#A = [a, a, a...]
#B = [b, b, b...]
#list라는 공통점을 가진 A, B의 리스트 존재

#dirty_dozen이라는 리스트 아래 fruits, vegetables의 별도 리스트 존재
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
dirty_dozen = [fruits, vegetables]
print(dirty_dozen)
#[['Strawberries', 'Nectarines', 'Apples', 'Grapes', 'Peaches', 'Cherries', 'Pears'], ['Spinach', 'Kale', 'Tomatoes', 'Celery', 'Potatoes']]
print(dirty_dozen[1][1])
#index 1의 리스트 중 index 1의 항목
#Kale
