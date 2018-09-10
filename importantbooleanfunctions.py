# use of     endswith(),startswith(),isdigit(),islower(),isspace()....

s="hello python"
print(s.endswith("hon"))     # true
print(s.endswith("xy"))     # false

print(s.startswith("he"))   # true
print(s.startswith("py"))   # false


b="hello123"
print(b.isalnum())
print(b.isalpha())

print(b.islower())

e="     "
print(s.isspace())   # false
print(e.isspace())   #true