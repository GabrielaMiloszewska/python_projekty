def formatuj(*args, **kwargs): # dla każdej linii argumentów pozycyjnych przechodze po wszystkich kwargs
    print(args, kwargs)
    result_text = [] # wrzucam przetworzone stringi do tej listy
    for arg in args: # iteruje po argumentach
        text = arg # tworzę zmienną na bazie otrzymanego stringa, którą bede modyfikować
        for key, value in kwargs.items(): # dzieki temu mam parę (key, value) np ("x", 10)
            text = text.replace(f"${key}", str(value)) # tworzę string w formacie $x
        result_text.append(text)
        print(result_text)
    return "\n".join(result_text) # łącze wszystkie linie znakiem nowej linii

#print(dir(str)) # zobacz jak dziala join, replace przy pomocy help
#help(str)

assert formatuj("") == ""
assert formatuj("A", "B") == "A\nB"
assert formatuj("to jest tekst ze zmienna a=$a", a=1) == "to jest tekst ze zmienna a=1"
assert formatuj("to jest tekst ze zmienna a=$a", a="xyz") == "to jest tekst ze zmienna a=xyz"
assert formatuj("$x, $y", "$x, $z", "$z, $v", x=10, y=20, z="a", v="b", j="100") == "10, 20\n10, a\na, b"