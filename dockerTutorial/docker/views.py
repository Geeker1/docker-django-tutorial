from django.shortcuts import render
import redis

# Create your views here.
print("Checking redis files, before error")
cache = redis.Redis(
    host='redis',
    port=6379,
    db=0)
default_key = "1"

cache.set(default_key, "one")


def index(request):
    key = default_key

    if request.method == 'POST':
        if 'key' in request.POST:
            key = request.POST['key']

        if (
            request.POST['submit'] == "save" and
            request.POST['cache_value'] is not None
        ):
            cache.set(key, request.POST['cache_value'])

        elif request.POST['submit'] == "load":
            pass

    cache_value = None
    if key in cache:
        cache_value = cache.get(key).decode('utf-8')

    return render(
        request, "index.html",
        context={
            "cache_value": cache_value,
            "key": key
        }
    )
