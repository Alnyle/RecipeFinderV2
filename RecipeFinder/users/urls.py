from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    path('login/', views.login_view, name='login_view'),
    path('resgister/', views.sign_up, name='register'),
    path('logout/', views.logout_view, name='logout_view'),
    path('profile/', views.profile, name='profile'),
    path('updatePassword_view/', views.updatePassword_view, name='updatePassword_view'),
    path('addRecipe/', views.addRecipePage, name='addRecipePage'),
    path('EditRecipe/', views.editRecipePage, name='editRecipePage'),
    path('deleteRecipe/<int:recipe_id>', views.deleteRecipe, name='deleteRecipe'),
    path('editRecipeDetails/<int:recipe_id>', views.editRecipeDetails, name='editRecipeDetails'),
    path('addLevel/', views.addLevel_view, name='addLevel_view'),
    path('EditLevel/', views.EditLevel_view, name='EditLevel_view'),
    path('EditLevelForm/', views.EditLevelForm_view, name='EditLevelForm_view'),
    path('deleteLevel/', views.deleteLevel_view, name='deleteLevel_view'),
    path('AddCategory/', views.AddCategory_view, name='AddCategory_view'),
    path('deleteDategory/', views.deleteCategory_view, name='deleteCategory_view'),
    path('EditCategory/', views.EditCategory_view, name='EditCategory_view'),
    path('EditCategoryForm/<int:category_id>', views.EditCategoryForm_view, name='EditCategoryForm_view'),
    path('addPublisher/', views.addPublisher_view, name='addPublisher_view'),
    path('EditPublisher/', views.EditPublisher_view, name='EditPublisher_view'),
    path('deletePublisher/', views.deletePublisher_view, name='deletePublisher_view'),
    path('EditPublisherDetails/<int:pub_id>', views.EditPublisherDetails_view, name='EditPublisherDetails_view'),
    path('EditPublisherDetails/<int:pub_id>', views.EditPublisherDetails_view, name='EditPublisherDetails_view'),
    path('EditPersonalInfo/<int:user_id>', views.EditPersonalInfo_view, name='EditPersonalInfo_view'),
    path('saveUpdatePersonalInfo_view/', views.saveUpdatePersonalInfo_view, name='saveUpdatePersonalInfo_view'),

]