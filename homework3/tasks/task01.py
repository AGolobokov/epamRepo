

def cache(times):
    cache_list = list()

    def cache_decorator(function):
        def cache_wrapper(*args):
            if not cache_list:
                value = function(*args)
                if value not in cache_list:
                    for j in range(0, times + 1):
                        cache_list.append(value)
                print(cache_list[0])
                cache_list.remove(value)
            else:
                print(cache_list[0])
                cache_list.remove(cache_list[0])
        return cache_wrapper
    return cache_decorator
