// password match validation for signups 
document.addEventListener('DOMContentLoaded', function() {
    const passwordField = document.getElementById('password');
    const confirmPasswordField = document.getElementById('password_confirm');
    const passwordMismatchMessage = document.getElementById('password-mismatch');

    if (passwordField && confirmPasswordField && passwordMismatchMessage) {
        passwordField.addEventListener('input', validatePasswordMatch);
        confirmPasswordField.addEventListener('input', validatePasswordMatch);
    }

    function validatePasswordMatch() {
        if (passwordField.value !== confirmPasswordField.value) {
            passwordMismatchMessage.style.display = 'block';
        } else {
            passwordMismatchMessage.style.display = 'none';
        }
    }
});

// Pop-up notification code
function showNotification(message) {
    const notification = document.createElement('div');
    notification.className = 'notification';
    notification.innerText = message;
    document.body.appendChild(notification);
    setTimeout(() => {
        notification.remove();
    }, 3000);
}

// Collapsible sections of site
document.querySelectorAll('.collapsible').forEach(item => {
    item.addEventListener('click', function() {
        this.nextElementSibling.classList.toggle('collapsed');
    });
});

