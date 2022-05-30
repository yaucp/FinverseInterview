from django.http import HttpResponse
from .models import KeyDatabase


# Handler for the set page
def set(request):
    # Getting the parameters from the querydict object
    if request.method == "POST":
        params = request.POST.dict()
    elif request.method == "GET":
        params = request.GET.dict()
    else:
        return HttpResponse(status=405)

    keyDB = KeyDatabase.objects

    # Checking whether there is extra parameters given or not in the URL
    if len(params.keys()) != 1:
        return HttpResponse("Invalid parameters. Please retry.")

    for key, value in params.items():
        try:
            # Search for the role with same primary key
            row = keyDB.filter(pk=key)
            if row.exists():
                row.update(values=value)
            else:
                # Update the same value for the same key
                newKey = KeyDatabase(keys=key, values=value)
                newKey.save()
        except Exception as error:
            return HttpResponse(error)
    return HttpResponse("Success")


def get(request):
    # Getting the parameters from the querydict object
    if request.method == "POST":
        params = request.POST.dict()
    elif request.method == "GET":
        params = request.GET.dict()
    else:
        return HttpResponse(status=405)

    keyDB = KeyDatabase.objects

    # Checking whether there is extra parameters given or not in the URL or did the user use type 'key' in the
    # parameters accurately
    if len(params.keys()) != 1 or "key" not in params.keys():
        return HttpResponse("Invalid parameters. Please retry.")

    requestkey = params["key"]
    try:
        row = keyDB.filter(pk=requestkey)
        if row.exists():
            # Print the value
            return HttpResponse(row[0].values)
        else:
            # Indicate that the key does not exist
            return HttpResponse(status=404)
    except Exception as error:
        return HttpResponse(error)
    return HttpResponse("Unknown Error")
