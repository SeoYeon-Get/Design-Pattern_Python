import functools

# memoize를 사용한 함수 목록을 저장. 그런 후
# `clear_memoized_values`로 일괄 비우기를 수행.
_memoized_functions = []

def memoize(func):
    """함수를 호출해서 반환한 값을 캐시로 저장함"""
    func = functools.lru_cache()(func)
    _memoized_functions.append(func)
    return func

def clear_memoized_values():
    """@memoize에 저장된 모든 값을 비워서 각 테스트가 고립된 환경으로 동작할 수 있도록 함"""
    for func in _memoized_functions:
        func.cache_clear()