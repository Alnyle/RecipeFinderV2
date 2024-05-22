
const firstNameElement = document.querySelector('#firstName')
const lastNameElement = document.querySelector('#lastName')
const emailElement = document.querySelector('#email')
const form = document.querySelector('#EditPersonalInfo')

const checkFirstName = () => {

    let valid = false;
    const min = 3, max = 25;

    const firstName = firstNameElement.value.trim();

    // check is the filed is Empty or not
    if (!isRequired(firstName)) {
        showError(firstNameElement ,'First name can not be blank');
    }
    else if (!isBetween(firstName.length, min, max)) {
        showError(firstNameElement ,`Last name must be between ${min} and ${max} characters`);
    }
    else {
        showSuccess(firstNameElement);
        valid = true;
    }
    return valid;
}
const checkLastName = () => {

    let valid = false;
    const min = 3, max = 25;

    const lastName = lastNameElement.value.trim();

    // check is the filed is Empty or not
    if (!isRequired(lastName)) {
        showError(lastNameElement ,'Name can not be blank');
    }
    else if (!isBetween(lastName.length, min, max)) {
        showError(lastNameElement ,`Name must be between ${min} and ${max} characters`);
    }
    else {
        showSuccess(lastNameElement);
        valid = true;
    }
    return valid;
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


form.addEventListener('submit', async (e) => {

    e.preventDefault();

    let isFirstNameValid = checkFirstName(), isLastNameValid = checkLastName(), isEmail = checkEmail();
    let isFormValid = isFirstNameValid && isLastNameValid && isEmail;

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
        case 'firstName':
            checkFirstName();
            break;
        case 'lastName':
            checkLastName();
            break;
        case 'email':
            checkEmail();
            break;
    }
}));