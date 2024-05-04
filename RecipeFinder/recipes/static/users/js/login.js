
const usernameElement = document.querySelector('#username')
const passwordElement = document.querySelector('#password')
const form = document.querySelector('#login')

const checkUsername = () => {

    let valid = false;
    const min = 3, max = 25;

    const username = usernameElement.value.trim();

    // check is the filed is Empty or not
    if (!isRequired(username)) {
        showError(usernameElement ,'Name can not be blank');
    }
    else if (!isBetween(username.length, min, max)) {
        showError(usernameElement ,`Name must be between ${min} and ${max} characters`);
    }
    else {
        showSuccess(usernameElement);
        valid = true;
    }
    return valid;
}

const checkPassword = () => {

    let valid = false;
    const password = passwordElement.value.trim();

    if (!isRequired(password)) {
        showError(passwordElement, 'Password can not be blank.');
    }
    else if (!isPasswordSecure(password)) {
        showError(passwordElement, 'Password must has at least 8 characters that include at least 1 lowercase character, 1 uppercase characters, 1 number, and 1 special character in (!@#$%^&*)');
    }
    else {
        showSuccess(passwordElement);
        valid = true;
    }
    return valid
}


// check if the password has minimum secure requirement
const isPasswordSecure = (password) => {
    const res = new RegExp("^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#\$%\^&\*])(?=.{8,})");
    return res.test(password);
}


const isRequired = value => value === '' ? false : true;
const isBetween = (length, min, max) => length < min || length > max ? false : true;


const isEmailValid = (email) => {
    const reg = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return reg.test(email)
}
const showError = (input, message) => {

    const formField = input.parentElement;

    formField.classList.remove('success');
    formField.classList.add('error');

    const error = formField.querySelector('small');
    error.textContent = message;
};

const showSuccess = (input) => {
    const formField = input.parentElement;


    formField.classList.remove('error');
    formField.classList.add('success');


    const error = formField.querySelector('small');
    error.textContent = '';
}


form.addEventListener('submit', (e) => {

    e.preventDefault();

    let isUsernameValid = checkUsername(), isPasswordValid = checkPassword();
    let isFormValid = isUsernameValid && isPasswordValid;

    if (isFormValid) {
        form.submit();
    }

})


const debounce = (fn, delay = 500) => {
    let timeoutId;
    return (...args) => {

        if (timeoutId) {
            clearTimeout(timeoutId);
        }
        timeoutId = setTimeout(() => {
            fn.apply(null, args)
        }, delay);
    };
};

form.addEventListener('input', debounce(function (e) {

    switch(e.target.id) {
        case 'username':
            checkUsername();
            break;
        case 'password':
            checkPassword();
            break;
    }
}));