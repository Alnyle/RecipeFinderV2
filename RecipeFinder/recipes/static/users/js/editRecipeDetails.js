

const ingredients = document.querySelector(".ingredients");
const addBtn = document.querySelector("#add_Ingredient");
const deleteBtnEls = document.querySelectorAll('.delete_Ingredient');




const recipeDescriptionEl = document.querySelector('#recipe_description');
const recipeIDEl = document.querySelector('#recipe_id')
const recipeNameEl = document.querySelector('#recipe_name')
const courseNameEls = document.querySelector('#course_name')


document.addEventListener('click', function(event) {
    if (event.target.classList.contains('delete_Ingredient')) {
        let ele = event.target;
        let ingredientElement = ele.closest('.ingredient');
        ingredientElement.parentNode.removeChild(ingredientElement);
    }
});






// deleteBtnEls.forEach(deleteBtnEl => {
//   deleteBtnEl.addEventListener('click', e => {
//     // e.target.preventDefault();
//         let ele = e.currentTarget;
//
//     // if (ingredients.childElementCount >= 2) {
//         let ingredientElement = ele.parentNode.parentNode.parentNode;
//         ingredientElement.removeChild(ele.parentNode.parentNode)
//         // console.log(ingredientElement)// Get the parent ingredient element
//         // removeNode(ingredientElement); // Remove the ingredient
//     // }
//   })
//
// })



// form.addEventListener('submit', (e) => {
//
//     e.preventDefault();
//     const recipeID = recipeIDEl.value;
//
// })





addBtn.addEventListener("click", (e) => {

  e.preventDefault();


  const ingredientElement = document.createElement("div");
  ingredientElement.classList.add("ingredient");


  const formField = document.createElement("div");
  formField.classList.add("form-field");
  formField.classList.add("ingred");





  // Creating and appending input fields for Ingredient Name
  const ingredientNameLabel = document.createElement("label");
  ingredientNameLabel.textContent = "Ingredient Name";
  const ingredientNameInput = document.createElement("input");
  ingredientNameInput.setAttribute("type", "text");
  ingredientNameInput.setAttribute("name", "ingredient_name");
  ingredientNameInput.classList.add("ingredient_name");
  const sm = document.createElement('small');
  sm.textContent = '';

  formField.appendChild(ingredientNameLabel);
  formField.appendChild(ingredientNameInput);
  formField.appendChild(sm);

  // Appending the first row to the ingredient container
  ingredientElement.appendChild(formField);

  // Creating and appending the second row of inputs
  const formField2 = document.createElement("div");
  formField2.classList.add("form-field");
  formField2.classList.add("ingred");


  // Creating and appending input fields for Ingredient Quantity
  const ingredientQuantityLabel = document.createElement("label");
  ingredientQuantityLabel.textContent = "Ingredient Quantity";
  const ingredientQuantityInput = document.createElement("input");
  ingredientQuantityInput.setAttribute("type", "text");
  ingredientQuantityInput.setAttribute("name", "ingredient_quantity");
  ingredientQuantityInput.classList.add("ingredient_quantity");
  formField2.appendChild(ingredientQuantityLabel);
  formField2.appendChild(ingredientQuantityInput);

  const formField3 = document.createElement("div");
  formField3.classList.add("form-field");
  formField3.classList.add("ingred");

  const ingredientDescLabel = document.createElement("label");
  ingredientDescLabel.textContent = "Ingredient Description(optional)";
  const ingredientDescInput = document.createElement("textarea");
  ingredientDescInput.setAttribute("placeholder", "Describe your recipe here");
  ingredientDescInput.setAttribute("name", "ingredient_description");
  ingredientDescInput.setAttribute("rows", "15");
  ingredientDescInput.setAttribute("cols", "50");
  ingredientDescInput.classList.add("ingredient_desc");

  formField3.appendChild(ingredientDescLabel);
  formField3.appendChild(ingredientDescInput);
  formField3.appendChild(sm);


  const deleteBtnDiv = document.createElement('div');
  deleteBtnDiv.classList.add('delete-btn');
  const deleteBtn = document.createElement('button')
  deleteBtn.setAttribute('type', 'button');
  deleteBtn.classList.add('delete_Ingredient')
  deleteBtn.textContent = 'remove Ingredient'
  deleteBtnDiv.appendChild(deleteBtn);



  const line = document.createElement('hr');

  // Appending the second row to the ingredient container
  ingredientElement.appendChild(formField);
  ingredientElement.appendChild(formField2);
  ingredientElement.appendChild(formField3);
  ingredientElement.appendChild(deleteBtnDiv);
  ingredientElement.appendChild(line);



  // Appending the new ingredient container to the ingredients container
  ingredients.appendChild(ingredientElement);

});




// form.addEventListener('submit', (e) => {
//
//     e.preventDefault();
//
// })



menuBtn.addEventListener('click', function(e) {
    console.log('ehhfs');
    e.preventDefault();
    menu.classList.toggle('toggle-menu');
})
exitBtn.addEventListener('click', function(e) {
    e.preventDefault();
    menu.classList.toggle('toggle-menu')
})