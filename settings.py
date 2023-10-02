import menu as m
SHIRINA = 1920
DIFFICULT = 0
BISOTA = 1080
NAME = m.sobitiya['Игрок']
if m.sobitiya['Сложность'] == 'Легко(5сек)':
    DIFFICULT = 500
elif m.sobitiya['Сложность'] == 'Нормально(4сек)':
    DIFFICULT = 400
elif m.sobitiya['Сложность'] == 'Сложно(3сек)':
    DIFFICULT = 300
elif m.sobitiya['Сложность'] == 'Хардкор(1сек)':
    DIFFICULT = 100
    

