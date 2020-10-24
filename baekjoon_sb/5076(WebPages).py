def check_stack(stack):
    pass


while True:

    try:
        web = input()

        gather = False
        tag = []
        stack = []
        for s in web:

            if s == '<':
                gather = True

            elif s == '>':

                gather = False

                ele = ''.join(tag).lstrip('/')
                if ele[-1] == '/': 
                    tag = []
                    continue

                if stack:
                    if stack[-1] == ele:
                        stack.pop(-1)

                    else:
                        stack.append(ele)

                else:
                    stack.append(ele)
                #stack.append(''.join(tag).lstrip('/'))
                tag = []

            else:
                if s == ' ':
                    gather = False
                    continue

                if gather:
                    tag.append(s)
            
        print(stack)
        if stack:
            print('illegal')

        else:
            print('legal')

    except:
        break