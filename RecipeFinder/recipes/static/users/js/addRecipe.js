
const form = document.querySelector('form');

const ingredients = document.querySelector(".ingredients");
const addBtn = document.querySelector("#add_Ingredient");



const recipeDescriptionEl = document.querySelector('#recipe_description');
const recipeIDEl = document.querySelector('#recipe_id')
const recipeNameEl = document.querySelector('#recipe_name')
const courseNameEl = document.querySelector('#course_name')

console.log(addBtn);



// form.addEventListener('submit', (e) => {
//
//     e.preventDefault();
//     const recipeID = recipeIDEl.value;
//
// })
//




addBtn.addEventListener("click", (e) => {

  e.preventDefault();

  // Creating a new ingredient container element
  const ingredientElement = document.createElement("div");
  ingredientElement.classList.add("ingredient");

  // Creating and appending the first row of inputs
  const formField = document.createElement("div");
  formField.classList.add("form-field");





  // Creating and appending input fields for Ingredient Name
  const ingredientNameLabel = document.createElement("label");
  ingredientNameLabel.textContent = "Ingredient Name";
  const ingredientNameInput = document.createElement("input");
  ingredientNameInput.setAttribute("type", "text");
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

  // Creating and appending input fields for Ingredient Quantity
  const ingredientQuantityLabel = document.createElement("label");
  ingredientQuantityLabel.textContent = "Ingredient Quantity";
  const ingredientQuantityInput = document.createElement("input");
  ingredientQuantityInput.setAttribute("type", "text");
  ingredientQuantityInput.classList.add("ingredient_quantity");
  formField2.appendChild(ingredientQuantityLabel);
  formField2.appendChild(ingredientQuantityInput);

  const ingredientDescLabel = document.createElement("label");
  ingredientDescLabel.textContent = "Ingredient Description(optional)";
  const ingredientDescInput = document.createElement("textarea");
  ingredientDescInput.setAttribute("placeholder", "Describe your recipe here");
  ingredientDescInput.setAttribute("rows", "15");
  ingredientDescInput.setAttribute("cols", "50");
  ingredientDescInput.classList.add("ingredient_desc");

  formField2.appendChild(ingredientDescLabel);
  formField2.appendChild(ingredientDescInput);
  formField2.appendChild(sm);

  const line = document.createElement('hr');

  // Appending the second row to the ingredient container
  ingredientElement.appendChild(formField);
  ingredientElement.appendChild(formField2);
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