def greeting(name="noble stranger"):
    if isinstance(name, str):
        print(f"Hello, " + name + ",")
    else:
        print("Errror! It was not a name.")
greeting("Alexandra")
greeting("Wil")
greeting()
greeting(42)