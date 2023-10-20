from json import load
path="C:\\Users\\My\\OneDrive\\Desktop\\my_pythonworks\\movies\\db.json"
with open(path) as f:
    data=load(f)

# print(len(data))
# all_names=[m.get("Title") for m in data]
# print(all_names)

# all_directors={m.get("Director") for m  in data}
# all_directors.discard("N/A")
# print(all_directors)


# filtered_data=[m for m in data if m.get("imdbRating")!="N/A"]
# top_movie=max(filtered_data,key=lambda m:float(m.get("imdbRating")))
# print(top_movie.get("Title"))


# #print all genres....................
# #printvall movies with action genree
# #movies released before 2014
print("|SET OF GENRES|")
all_genres=set()
for m in data:
    for gn in m.get("Genre").split():
        all_genres.add(gn.rstrip(","))  
print(all_genres)
print("|MOVIES WITH ACTION GENRES")
for mv in data:
 if mv.get("Genre").count("Action")>0:
        print(mv.get("Title"))
print("|Movies released before 2014|")
for mv in data:
    r_date=mv.get("Released")
    year=r_date.split(" ")[-1]

    if year.isdigit():
        if int(year)<2014:
            print(mv.get("Title"),mv.get("Released"))



# filtered_genre=[m for m in data if m.get("Genre")=="Action"]
# # f_genre=filtered_genre,key=lambda m:m.get("Genre")
# print(filtered_genre.get("Title"))
