

const levelNameFieldEl = document.querySelector('#level_name')
const saveBtn = document.querySelector('#save-btn')
const saveMoreBtn = document.querySelector('#saveAndMore-btn')
const loginForm = document.querySelector('#login')

async function renderPage(url) {

    try {
        const response = await fetch(url);
        if (response.ok) {
            window.location = response.url;
        }
    }
    catch (error) {
        console.error("Can not render the:", error);
    }
}

async function sendData(data, url, anotherURL, csrfToken) {
    try {
        const response = await fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
                'X-CSRFToken': csrfToken,
            },
            body: data,
        });

        if (response.status === 200) {
            console.log("good request");
            await renderPage(anotherURL)
        } else if (response.status === 400) {
            const responseJson = await response.json()
            const message = responseJson.message
            showError(levelNameFieldEl, message);
        }
        else {
            console.log("bad request");
        }
    } catch (error) {
        console.error(error)
    }

}



saveMoreBtn.addEventListener('click', async (e) => {
    e.preventDefault()
    const value = levelNameFieldEl.value;
    if (value !== '') {

        let serializeForm  = new FormData(loginForm);
        const data = new URLSearchParams(serializeForm);
        const url = loginForm.getAttribute('data-action-url');
        const csrfToken = loginForm.getAttribute('data-csrf-token');
        await sendData(data , url, url, csrfToken);
    }

})


saveBtn.addEventListener('click', async (e) => {
    e.preventDefault()
    let serializeForm  = new FormData(loginForm);
    const data = new URLSearchParams(serializeForm);
    const url = loginForm.getAttribute('data-action-url');
    const url2 = loginForm.getAttribute('data-action-url2');
    const csrfToken = loginForm.getAttribute('data-csrf-token');
    await sendData(data , url, url2, csrfToken);
})

const showError = (input, message) => {

    const formField = input.parentElement;

    formField.classList.remove('success');
    formField.classList.add('error');

    const error = formField.querySelector('small');
    error.textContent = message;
};