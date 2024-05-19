const menuBtn = document.querySelector('.menu')
const exitBtn = document.querySelector('.exit')
const menu = document.querySelector('aside')

menuBtn.addEventListener('click', function (e) {
    e.preventDefault();
    menu.classList.toggle('toggle-menu');
})
exitBtn.addEventListener('click', function (e) {
    e.preventDefault();
    menu.classList.toggle('toggle-menu')
})

const formId = document.querySelectorAll('.like-icon')
const bookMarks = document.querySelectorAll('.favorite-icon');
const formID = document.getElementById('form')


formId.forEach(form => {
    form.addEventListener('click', e => {
        const el = e.target;
        el.submit();
    })
})

bookMarks.forEach(bookMark => {
    bookMark.addEventListener('click', (e) => {
        const element = e.target;
        const form = element.closest('form')
        const recipeID = element.getAttribute('recipeID');

        console.log(form, recipeID)


        const formID = document.getElementById('form')

        console.log("worked");
        const url = recipeID;
        const data = {
            recipe: element.classList[1],
        }
        const list = element.classList;
        if (element.classList.contains('marked')) {
            list.remove("marked");
            list.remove("fa-solid");
            list.add("fa-regular");
            form.submit()
        } else {
            list.add("marked");
            list.add("fa-solid");
            list.remove("fa-regular");
            form.submit()
        }
    });
});

const selectContainer = document.querySelector('.select-container');
const selectCategory = document.querySelector('.select-category');
selectContainer.addEventListener('click', e => {
    if (selectCategory.style.display === 'none') {
        selectCategory.style.display = 'flex'
    } else {
        selectCategory.style.display = 'none'
    }
});

// for mobile navbar category section
const selectContainerM = document.querySelector('.subCategories');
const selectCategoryM = document.querySelector('.select-category-m');
const arrow = document.querySelector('.select-arrow')

selectContainerM.addEventListener('click', e => {

    const list = arrow.classList;
    const SelectCategoryList = selectCategoryM.classList;
    if (SelectCategoryList.contains('showCategory')) {
        SelectCategoryList.remove('showCategory')
        list.remove('fa-arrow-up');
        list.add('fa-arrow-down')
    } else {
        SelectCategoryList.add('showCategory')
        list.add('fa-arrow-up');
        list.remove('fa-arrow-down')
    }
});

const searchForm = document.querySelector('#searchForm')
const searchFieldEl = document.querySelector('#searchField');
const value = searchFieldEl.value.trim();
searchForm.addEventListener('submit', async (e) => {
    e.preventDefault();

    if (e.target && value) {

        if (value) {
            let serializeForm = new FormData(searchForm);
            const data = new URLSearchParams(serializeForm);
            const url = searchForm.getAttribute('data-action-url');
            const csrfToken = searchForm.getAttribute('data-csrf-token');

            await SearchRecipe(data, url, csrfToken);
        }
    }
})


async function SearchRecipe(data, url, csrfToken) {
    try {
        const response = await fetch(url, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
                'X-CSRFToken': csrfToken,
            },
        })
    } catch (error) {
        console.error(error)
    }
}