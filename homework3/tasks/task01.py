valuee = 0


def cache(times):
    cache_list = list()
    print(cache_list)
    print("times ==", times)

    def cache_decorator(function):
        def cache_wrapper(*args):
            if not cache_list:
                global valuee
                valuee = function(*args)
                # print("id val ==", id(valuee))
                if valuee not in cache_list:
                    for j in range(0, times + 1):
                        cache_list.append(valuee)
                # print(cache_list)
                a = cache_list[0]
                print(a)
                cache_list.remove(valuee)
                return a
            else:
                # print(cache_list)
                b = cache_list[0]
                print(b)
                cache_list.remove(valuee)
                return b

        return cache_wrapper

    return cache_decorator
