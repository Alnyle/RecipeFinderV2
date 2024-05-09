


const deleteRecipeForm = document.querySelectorAll('.deleteRecipe_form')
deleteRecipeForm.forEach(form => {
    form.addEventListener('submit', e => {
        console.log("worked")
        const el = e.target;
        el.submit();
    })
})