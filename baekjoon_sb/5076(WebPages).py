while True:

    try:
        web = input()
        if web == '#': break

        gather = False
        tag, stack = [], []
        for s in web:

            # When Tag starts, start to gather tag name
            # when gather false, don't receive any inputs...
            if s == '<':
                gather = True

            # When Tag ends
            elif s == '>':

                gather = False

                # Normal tags have tag, /tag structure -> unify without /
                ele = ''.join(tag).lstrip('/')
                
                # when last string is /, it is self opening-closing tag, kill
                if ele[-1] == '/': 
                    tag = []
                    continue

                # when it is splitable, it has attributes
                # use the first one only
                elif len(ele.split()) > 1:
                    ele = ele[0]

                # check stack
                if stack:
                    if stack[-1] == ele:
                        stack.pop(-1)

                    else:
                        stack.append(ele)

                else:
                    stack.append(ele)

                # when stack is done, reset tag
                tag = []


            # gather strings when only < is opened(gather=True)
            else:
                if gather:
                    tag.append(s)
            
        # printing part
        if stack:
            print('illegal')

        else:
            print('legal')

    except:
        break