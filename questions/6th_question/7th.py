def user_fullname(u):
    return f"{u['first']} {u['last']}"

def admin_fullname(a):
    return f"{a['first']} {a['last']}"

#example before refactoring with output
print(user_fullname({'first': 'John', 'last': 'Doe'}))   # Output: John Doe
print(admin_fullname({'first': 'Jane', 'last': 'Smith'})) # Output: Jane Smith

# extract the repeated name-formatting code into a reusable helper
def format_fullname(person):
    return f"{person['first']} {person['last']}"
def user_fullname(u):
    return format_fullname(u)
def admin_fullname(a):
    return format_fullname(a)

#example after refactoring with output
print(user_fullname({'first': 'John', 'last': 'Doe'}))   # Output: John Doe
print(admin_fullname({'first': 'Jane', 'last': 'Smith'})) # Output: Jane Smith
