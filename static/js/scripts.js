function showDeletePopup() {
    document.getElementById('deletePopup').style.display = 'flex'
}

function hideDeletePopup() {
    document.getElementById('deletePopup').style.display = 'none'
}

setTimeout(function() {
    const messageElements = document.getElementsByClassName("message")
    for (let i = 0; i < messageElements.length; i++) {
        messageElements[i].style.display = "none"
    }
}, 5000)

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

const date = new Date()
document.getElementById("year").innerHTML = date.getFullYear()
