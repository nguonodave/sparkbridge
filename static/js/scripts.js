function showDeletePopup() {
    document.getElementById('deletePopup').style.display = 'flex'
}

function hideDeletePopup() {
    document.getElementById('deletePopup').style.display = 'none'
}

setTimeout(function() { 
    const messageElement = document.getElementById("message")
    if (messageElement) {
        messageElement.style.display = "none"
    }
}, 5000)