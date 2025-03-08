from django.shortcuts import render, redirect, get_object_or_404
from .models import Sticky
from .forms import StickyForm


# Create your views here.
def get_all(request):
    """
    Gets all sticky notes from database and displays them
    """
    stickies = Sticky.objects.all()
    context = {
        'stickies': stickies,
        'page_title': "Stickies"
    }
    return render(request, 'stickies/index.html', context)


def get(request, pk):
    """
    Shows a single sticky note by its ID (pk)
    """
    sticky = get_object_or_404(Sticky, pk=pk)
    return render(request, 'stickies/detail.html', {'sticky': sticky})


def create(request):
    """
    Handles creating a new sticky note
    On POST: saves the submitted data
    On GET: shows the empty form
    """
    if request.method == 'POST':
        form = StickyForm(request.POST)
        if form.is_valid():
            sticky = form.save(commit=False)
            sticky.save()
            return redirect('sticky_list')
    else:
        form = StickyForm()
    return render(request, 'stickies/sticky_form.html', {'form': form})


def update(request, pk):
    """
    Updates an existing sticky note
    On POST: saves the changes
    On GET: shows form with current data
    """
    sticky = get_object_or_404(Sticky, pk=pk)
    if request.method == 'POST':
        form = StickyForm(request.POST, instance=sticky)
        if form.is_valid():
            sticky = form.save(commit=False)
            sticky.save()
            return redirect('sticky_list')
    else:
        form = StickyForm(instance=sticky)
    return render(request, 'stickies/sticky_form.html', {'form': form})


def delete(request, pk):
    """
    Deletes a sticky note
    On POST: confirms deletion
    On GET: asks for confirmation
    """
    sticky = get_object_or_404(Sticky, pk=pk)
    if request.method == 'POST':
        sticky.delete()
        return redirect('sticky_list')
    return render(request, 'stickies/confirm_delete.html', {'sticky': sticky})
