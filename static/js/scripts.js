function showDeletePopup() {
    document.getElementById('deletePopup').style.display = 'flex'
}

function hideDeletePopup() {
    document.getElementById('deletePopup').style.display = 'none'
}

// functionality for disappearing error messages in loginform
// the message is set to disappear after 5 seconds
setTimeout(function() {
    const messageElements = document.getElementsByClassName("login-error-message")
    for (let i = 0; i < messageElements.length; i++) {
        messageElements[i].style.display = "none"
    }
}, 5000)

// functionality for disappearing error messages in registerform
// the message is set to disappear when a user starts typing on the related input field
document.addEventListener('DOMContentLoaded', function() {
    const inputs = document.querySelectorAll('.register-form input')

    inputs.forEach(function(input) {
        input.addEventListener('input', function() {
            const errorMessages = input.parentElement.querySelectorAll('.error-message')

            errorMessages.forEach(function(errorMessage) {
                errorMessage.style.display = 'none'
            })
        })
    })
})

// dynamically get the current year to display it in the copyright text
const date = new Date()
document.getElementById("year").innerHTML = date.getFullYear()
