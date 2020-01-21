def a():
    def b():
        #nonlocal val_int
        val_a[0] = 2
        print("b:", val_a)
        val_int = 99
        print("b:", val_int)
    val_a = [1,2,3,4]
    val_int = 100
    b()
    print("a:", val_a)
    print("a:", val_int)

a()
