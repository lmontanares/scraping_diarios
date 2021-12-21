# import re


# url = "https://www.biobiochile.cl/noticias/espectaculos-y-tv/notas-espectaculos-tv/2021/12/08/tia-magicarol-de-mundo-magico-sorprendio-con-aparicion-en-mega-mostro-su-emprendimiento.shtml"

# date = re.search(r"\d{4}/\d{2}/\d{2}", url)
# print(date.group())

# category = re.search(r"noticias", url)
# print(category.group())

# from faker import Faker
# from faker.providers import user_agent
# import fake_useragent
# f = Faker()

# print(f.name())


class test:
    name: str


t = test()
t.name = "name_test1"
print(t.name)
t.name = "name_test2"
print(t.name)
