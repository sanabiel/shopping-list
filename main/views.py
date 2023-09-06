from django.shortcuts import render

# Create my views here.
def show_main(request):
    context = {
        'name': 'Nabiel Ahmad Ardhityo',
        'class': 'PBP F'
    }

    return render(request, "main.html", context)
