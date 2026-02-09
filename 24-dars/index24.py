from avto import Avto

avto1 = Avto("GM", "Nexia 3", "oq", 2020, 10000, 1000)
avto2 = Avto("GM", "Nexia 2", "qizil", 2014, 6000, 10000)
avto3 = Avto("GM", "Nexia 1", "qora", 2009, 2000, 30000)

print(avto1.get_id)
print(avto3.get_id)
print(avto2.get_id)
print(avto1.add_km(200))
print(avto1.add_km(200))
print(avto1.add_km(-200))
# print(Avto.get_num_auto())
print(avto1.get_num_auto())