#===========================================
library_users = [
    {
        "id": 1,
        "name": "Oleksandr Ivanenko",
        "email": "olex.ivanenko@example.com",
        "membership_date": "2021-08-15",
        "books_borrowed": 3,
        "active": True
    },
    {
        "id": 2,
        "name": "Marina Petrenko",
        "email": "marina.petrenko@example.com",
        "membership_date": "2022-01-10",
        "books_borrowed": 5,
        "active": True
    },
    {
        "id": 3,
        "name": "Ihor Sydorenko",
        "email": "igor.sydorenko@example.com",
        "membership_date": "2020-11-20",
        "books_borrowed": 2,
        "active": False
    },
    {
        "id": 4,
        "name": "Hanna Oleksienko",
        "email": "ganna.aleksienko@example.com",
        "membership_date": "2021-05-30",
        "books_borrowed": 7,
        "active": True
    },
    {
        "id": 5,
        "name": "Maksym Shevchenko",
        "email": "maks.shevchenko@example.com",
        "membership_date": "2019-12-01",
        "books_borrowed": 0,
        "active": False
    },
    {
        "id": 6,
        "name": "Olena Koval",
        "email": "olena.koval@example.com",
        "membership_date": "2023-03-05",
        "books_borrowed": 1,
        "active": True
    },
    {
        "id": 7,
        "name": "Yuriy Stepanenko",
        "email": "yuriy.stepanenko@example.com",
        "membership_date": "2022-09-15",
        "books_borrowed": 4,
        "active": True
    },
    {
        "id": 8,
        "name": "Kateryna Kozak",
        "email": "kat.kozak@example.com",
        "membership_date": "2021-07-22",
        "books_borrowed": 6,
        "active": True
    },
    {
        "id": 9,
        "name": "Denys Pavlenko",
        "email": "den.pavlenko@example.com",
        "membership_date": "2020-04-12",
        "books_borrowed": 2,
        "active": False
    },
    {
        "id": 10,
        "name": "Lyudmyla Tkachenko",
        "email": "lyudmyla.tkachenko@example.com",
        "membership_date": "2023-01-25",
        "books_borrowed": 8,
        "active": True
    }
]
#===========================================
# i = 0

# while i < len(library_users):
#     print(library_users[i])
    
#     print()
    
#     i += 1
#===========================================
# for item in library_users:
#     print(item)
#     print()
#===========================================
i = 0

while i < len(library_users):
    print("-------------------------------------")
    for key, value in library_users[i].items():
        print(f"| {key}: {value}")
    i += 1
print("-------------------------------------")
#===========================================