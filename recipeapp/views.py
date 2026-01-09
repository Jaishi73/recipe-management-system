from django.shortcuts import render
from django.shortcuts import get_object_or_404
from recipeapp.models import Recipe
from .forms import RecipeForm
from django.shortcuts import redirect
# Create your views here.


def recipe_list(request):
    category = request.GET.get('category')

    if category:
        recipes = Recipe.objects.filter(category__iexact=category)
    else:
        recipes = Recipe.objects.all()

    categories = Recipe.objects.values_list('category', flat=True).distinct()

    return render(request, 'recipeapp/recipe_list.html', {
        'recipes': recipes,
        'categories': categories,
        'selected_category': category
    })



def recipe_create(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('recipe_list')
    else:
        form = RecipeForm()

    return render(request, 'recipeapp/recipe_form.html', {
        'form': form
    })

def recipe_detail(request, id):
    recipe = get_object_or_404(Recipe, id=id)
    return render(request, 'recipeapp/recipe_detail.html', {
        'recipe': recipe
    })
    
def recipe_update(request, id):
    recipe = get_object_or_404(Recipe, id=id)

    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('recipe_detail', id=recipe.id)
    else:
        form = RecipeForm(instance=recipe)

    return render(request, 'recipeapp/recipe_form.html', {
        'form': form
    })

def recipe_delete(request, id):
    recipe = get_object_or_404(Recipe, id=id)

    if request.method == 'POST':
        recipe.delete()
        return redirect('recipe_list')

    return render(request, 'recipeapp/recipe_confirm_delete.html', {
        'recipe': recipe
    })

