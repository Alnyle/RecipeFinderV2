
const passwordElement = document.querySelector('#password')
const confirmPasswordElement = document.querySelector('#confirm-password')
const form = document.querySelector('#UpdatePassword')




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

const checkConfirmPassword = () => {

    let valid = false;
    const confirmPassword = confirmPasswordElement.value.trim();
    const password = passwordElement.value.trim()

    if (!isRequired(confirmPassword)) {
        showError(confirmPasswordElement, 'Please Enter Password again.');
    }
    else if (confirmPassword !== password) {
        showError(confirmPasswordElement, 'The password does not match');
    }
    else {
        showSuccess(confirmPasswordElement);
        valid = true;
    }
    return valid
}


const checkEmail = () => {

    let valid = false;

    const email = emailElement.value.trim();

    if (!isRequired(email)) {
        showError(emailElement, 'Email can not be blank.');
    }
    else if (!isEmailValid(email)) {
        showError(emailElement, 'Email is not valid.');
    }
    else {
        showSuccess(emailElement);
        valid = true;
    }
    return valid;
}


// check if the password has minimum secure requirement
const isPasswordSecure = (password) => {
    const res = new RegExp("^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#\$%\^&\*])(?=.{8,})");
    return res.test(password);
}


const isRequired = value => value !== '';
const isBetween = (length, min, max) => !(length < min || length > max);

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




form.addEventListener('submit',  (e) => {

    e.preventDefault();

    let isPasswordValid = checkPassword(), isConfirmPasswordValid = checkConfirmPassword();


    let isFormValid =  isPasswordValid && isConfirmPasswordValid;

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
        case 'password':
            checkPassword();
            break;
        case 'confirm-password':
            checkConfirmPassword();
            break;
    }
}));