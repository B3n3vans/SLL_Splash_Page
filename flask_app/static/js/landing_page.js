// Email regex pattern
const EMAIL_REGEX = /^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$/;

// Validate name
function validateName(name) {
    return name.trim().length >= 2;
}

// Validate email
function validateEmail(email) {
    return EMAIL_REGEX.test(email.toLowerCase().trim());
}

// Update field validation state
function updateFieldValidation(fieldId, isValid, errorMessage) {
    const field = document.getElementById(fieldId);
    const errorElement = document.getElementById(fieldId + 'Error');
    
    if (isValid) {
        field.classList.remove('error');
        errorElement.classList.remove('show');
        errorElement.textContent = '';
    } else {
        field.classList.add('error');
        errorElement.classList.add('show');
        errorElement.textContent = errorMessage;
    }
}

// Form submission handler
document.getElementById('waitlistForm').addEventListener('submit', async function(e) {
    e.preventDefault();
    
    const name = document.getElementById('name').value.trim();
    const email = document.getElementById('email').value.trim().toLowerCase();
    
    // Final validation before submit
    const isNameValid = validateName(name);
    const isEmailValid = validateEmail(email);
    
    updateFieldValidation('name', isNameValid, 'Name must be at least 2 characters');
    updateFieldValidation('email', isEmailValid, 'Invalid email address');
    
    // Don't submit if validation fails
    if (!isNameValid || !isEmailValid) {
        return;
    }
    
    const submitBtn = document.getElementById('submitBtn');
    const btnText = document.getElementById('btnText');
    const formContainer = document.getElementById('formContainer');
    const successMessage = document.getElementById('successMessage');
    
    // Disable button and show loading state
    submitBtn.disabled = true;
    btnText.innerHTML = '<div class="spinner"></div>';
    
    try {
        // Submit to Flask backend
        const response = await fetch('/splash_signup', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: new URLSearchParams({
                name: name,
                email: email
            })
        });
        
        const result = await response.json();
        
        if (result.success) {
            // Show success message
            formContainer.style.display = 'none';
            successMessage.style.display = 'block';
        } else {
            // Show error on fields even if backend validation fails
            updateFieldValidation('email', false, result.message || 'Something went wrong. Please try again.');
            submitBtn.disabled = false;
            btnText.textContent = 'Join the Waitlist';
        }
        
    } catch (error) {
        console.error('Error:', error);
        updateFieldValidation('email', false, 'Something went wrong. Please try again.');
        submitBtn.disabled = false;
        btnText.textContent = 'Join the Waitlist';
    }
});

// Add smooth scroll behavior for footer links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth'
            });
        }
    });
});