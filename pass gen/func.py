def pass_gen(pass_length) :
    import random
    print('lets start')
    UpcaseChars = 'QWERTYUIOPASDFGHJKLZXCVBNM'
    LowcaseChars = 'qwertyuiopasdfghjklzxcvbnm'
    nums = '1234567890'
    symbols = "[]{};':<>,./?!@#$%^&*()_+=-/*-+"
    chars_list = [UpcaseChars,LowcaseChars,nums,symbols]
    password = ''
    if pass_length<=8 :
        print('it should be more then 8 chars')
    else :
        for i in range(int(pass_length)) :
            Rnum1 = random.randrange(4)
            if Rnum1 == 1 or Rnum1 == 0 :
                password += chars_list[Rnum1][random.randrange(len(chars_list[Rnum1])-1)]
            elif Rnum1 == 2 :
                password += chars_list[Rnum1][random.randrange(len(chars_list[Rnum1])-1)]
            elif Rnum1 == 3 :
                password += chars_list[Rnum1][random.randrange(len(chars_list[Rnum1]))-1]
    return password