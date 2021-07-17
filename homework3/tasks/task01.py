def cache(times):
    cache_list = list()

    def cache_decorator(function):
        def cache_wrapper(*args):
            value = 0
            if not cache_list:
                value = function(*args)
                if value not in cache_list:
                    for i in range(0, times + 1):
                        cache_list.append(value)
                # print(value) # use for example with print
                cache_list.remove(value)
                return value
            else:
                temp_value = cache_list[0]
                # print(temp_value) # use for example with print
                cache_list.remove(temp_value)
                return temp_value

        return cache_wrapper

    return cache_decorator
