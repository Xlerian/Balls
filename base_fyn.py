import sqlalchemy as sq
import sqlalchemy.orm as sqo
import base as b
Sessia_for_podkl = sqo.sessionmaker()
def proverka (name):
    sessia = Sessia_for_podkl(bind = b.base)
    query = sessia.query(b.score)
    for zapis in query:
        if zapis.name == name:
            sessia.close()
            return True
    sessia.close()
    return False
def dobavlenie_obnovlenie(name,size):
    if proverka(name) == True:
        sessia = Sessia_for_podkl(bind = b.base)
        query = sessia.query(b.score)
        for query1 in query:
            if query1.name == name:
                query1.size = size
                break
        sessia.commit()
        sessia.close()
    else:
        sessia = Sessia_for_podkl(bind = b.base)
        player = b.score(name = name, size = size)
        sessia.add(player)
        sessia.commit()
        sessia.close()