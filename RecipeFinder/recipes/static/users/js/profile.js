

const Sub_selectContainer = document.querySelector('.sub-select-container');
const Sub_selectCategory = document.querySelector('.sub-select-category');
Sub_selectContainer.addEventListener('click', e => {
    if (Sub_selectCategory.style.display === 'none') {Sub_selectCategory.style.display = 'flex'}
    else {Sub_selectCategory.style.display= 'none'}
});
