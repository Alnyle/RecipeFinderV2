
const searchForm = document.querySelector('#searchForm')

searchForm.addEventListener('submit', async(e) => {
    e.preventDefault();

    if (e.target) {
        // console.log(e.target.value.trim());
        // const value = e.target.value.trim();
        let serializeForm = new FormData(searchForm);
        const data = new URLSearchParams(serializeForm);
        const url = searchForm.getAttribute('data-action-url');
        const csrfToken = searchForm.getAttribute('data-csrf-token');

        await SearchRecipe(data, url, csrfToken);
    }
})


async function SearchRecipe(data, url, csrfToken){
    try {
        const response = await fetch(url, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
                'X-CSRFToken': csrfToken,
            },
            body: data,
        })
    }
    catch (error) {
        console.error(error)
    }
}