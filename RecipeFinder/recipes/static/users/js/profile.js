

const Sub_selectContainer = document.querySelector('.sub-select-container');
const Sub_selectCategory = document.querySelector('.sub-select-category');
Sub_selectContainer.addEventListener('click', e => {
    if (Sub_selectCategory.style.display === 'none') {Sub_selectCategory.style.display = 'flex'}
    else {Sub_selectCategory.style.display= 'none'}
});


const Sub_selectContainer2 = document.querySelector('.sub-select-container-2');
const Sub_selectCategory2 = document.querySelector('.sub-select-category-2');
Sub_selectContainer2.addEventListener('click', e => {
    if (Sub_selectCategory2.style.display === 'none') {Sub_selectCategory2.style.display = 'flex'}
    else {Sub_selectCategory2.style.display= 'none'}
});


const Sub_selectContainer3 = document.querySelector('.sub-select-container-3');
const Sub_selectCategory3 = document.querySelector('.sub-select-category-3');
Sub_selectContainer3.addEventListener('click', e => {
    if (Sub_selectCategory3.style.display === 'none') {Sub_selectCategory3.style.display = 'flex'}
    else {Sub_selectCategory3.style.display= 'none'}
});
