const deleteBtnEls = document.querySelectorAll('.delete_level_btn');
const deleteConfirmEl = document.querySelector('.delete-confirm');
const confirmBtnEl = document.querySelector('.confirm-btn');
const cancelBtnEl = document.querySelector('.cancel-btn');
const XBtn = document.querySelector('.x-btn');
const levelWrapper = document.querySelector('.level-wrapper')


// Even Listener for delete button
deleteBtnEls.forEach(deleteBtnEl => {
    deleteBtnEl.addEventListener('click', async (e) => {
        let deleteForm = e.target.closest('form');
        let serializeForm = new FormData(deleteForm);
        const data = new URLSearchParams(serializeForm);
        const url = deleteForm.getAttribute('data-action-url');
        const csrfToken = deleteForm.getAttribute('data-csrf-token');

        deleteConfirmEl.style.display = "flex";


        cancelBtnEl.addEventListener('click', () => {
            deleteConfirmEl.style.display = "none";
        });


        confirmBtnEl.addEventListener('click', async () => {
            await deleteLevel(data, url, csrfToken);
           let currentLevel = deleteForm.closest('.level');
            if (currentLevel) {
                currentLevel.remove();
            } else {
                console.error('Parent level element not found');
            }
            deleteConfirmEl.style.display = "none";
        });
        

        window.onclick = function (e) {
            const el = e.target;
            if (el == deleteConfirmEl || el == XBtn) {
                deleteConfirmEl.style.display = "none";
            }
        };
    });
});

async function deleteLevel(data, url, csrfToken) {
    try {
        const response = await fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
                'X-CSRFToken': csrfToken,
            },
            body: data,
        });

        if (response.ok) {
            console.log('Level deleted successfully');
        } else {
            console.error('Bad request');
        }
    } catch (error) {
        console.error(error);
    }
}
