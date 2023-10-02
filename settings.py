import menu as m
SHIRINA = 1920
DIFFICULT = 0
BISOTA = 1080
NAME = m.sobitiya['Игрок']
if m.sobitiya['Сложность'] == 'Легко(0.5сек)':
    DIFFICULT = 500
elif m.sobitiya['Сложность'] == 'Нормально(0.4сек)':
    DIFFICULT = 400
elif m.sobitiya['Сложность'] == 'Сложно(0.3сек)':
    DIFFICULT = 300
elif m.sobitiya['Сложность'] == 'Хардкор(0.1сек)':
    DIFFICULT = 100
    

