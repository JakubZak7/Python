countries = [ 
{
    "name":"Poland", "population":38000000
},

{
   "name":"Germany", "population":  84480000
},

{
    "name":"Belarus", "population": 35345345
},

{
    "name":"Litwa", "population": 1231312
},
{
    "name":"USA", "population": 12312323
}]


print(f"{'Country':<10} {"Population":>10}")

for country in countries:
    print(f"{country['name']:<10} {country['population']:>10}") 