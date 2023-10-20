frameworks=[{"id":1,"name":"django","rating":5,"language":"python"},
            {"id":2,"name":"angular","rating":4,"language":"javascript"},
            {"id":3,"name":"react","rating":5,"language":"javascript"},
            {"id":4,"name":"spring","rating":3,"language":"java"},
            {"id":5,"name":"asp.net","rating":2,"language":"c#"},
            {"id":6,"name":"flask","rating":3,"language":"python"},
]

lowest_rating=min(frameworks,key=lambda fw:fw.get("rating"))
top_rating=max(frameworks,key=lambda fw:fw.get("rating"))
srt=sorted(frameworks,reverse=True,key=lambda fw:fw.get("rating"))

print(srt)