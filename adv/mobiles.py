mobiles=[
    {"id":1,"name":"samsungs22","brand":"samsung","varients":[
        {"ram":"8gb","rom":"128gb","price":84000},
        {"ram":"8gb","rom":"256gb","price":100000},

    ]}, 
    {"id":2,"name":"samsungsa52","brand":"samsung","varients":[
        {"ram":"4gb","rom":"128gb","price":54000},
        {"ram":"8gb","rom":"256gb","price":650000},

    ]},
     {"id":3,"name":"one plus nord2","brand":"one plus","varients":[
        {"ram":"8gb","rom":"128gb","price":34000},
        {"ram":"8gb","rom":"256gb","price":450000},

    ]},
     {"id":4,"name":"miii1","brand":"redmi","varients":[
        {"ram":"8gb","rom":"128gb","price":24000},
        {"ram":"8gb","rom":"256gb","price":350000},

    ]},
]

# all_mobile_name=[mob.get("name") for mob in mobiles]
# print(all_mobile_name)

# #print brand names
# br_name=[mob.get("brand")for mob in mobiles]
# print(br_name)

# #printmobile rate 20k - 30k

# for mob in mobiles:
#     for v in mob.get("varients"):
#         if v.get("price") in range(20000,30001):
#             print(mob.get("name"))

# price_filter=[mob.get("name")for mob in mobiles for v in mob.get("varients") if v.get("price") in range(20000,30001)]
# print(price_filter)

# #print 4gb ram phones

# for mob in mobiles:
#     for v in mob.get("varients"):
#         if v.get("ram")=="4gb":
#             print(mob.get("name"))

# ram_ft=[mob.get("name")for mob in mobiles for v in mob.get("varients") if v.get("ram")=="4gb"]
# print(ram_ft)


# #8gb ram below 40k
# for mob in mobiles:
#     for v in mob.get("varients"):
#         if v.get("ram")=="8gb" and v.get("price")<40000:
#             print(mob.get("name"))

# ramprice_f=[mob.get("name")for mob in mobiles for v in mob.get("varients") if v.get("ram")=="8gb" and v.get("price")<=40000]
# print(ramprice_f)

# #costly

# for mob in mobiles:
#     for v in mob.get("varients"):
#         print (v.get("price"))


costly_price=max(v.get("price") for mob in mobiles for v in mob.get("varients"))
print(costly_price)