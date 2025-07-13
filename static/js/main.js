 // C:\Users\ashok_wsg2ds5\my-pythonDjango1\static\js\main.js

    document.addEventListener('DOMContentLoaded', function() {
        // Get references to the elements by their IDs
        const toggle = document.getElementById('theme-toggle');
        const body = document.body; // The <body> element is directly accessible
        const icon = document.getElementById('theme-icon');
        const label = document.getElementById('theme-label');

        // Function to apply the theme (dark or light)
        function setTheme(theme) {
            if (theme === 'dark') {
                body.classList.add('dark-mode'); // Add dark-mode class to body
                if (icon) icon.textContent = '☀️'; // Change icon to sun, check if icon exists
                if (label) label.textContent = 'Light Mode'; // Label should say "Light Mode" when dark mode is ON
            } else { // theme is 'light'
                body.classList.remove('dark-mode'); // Remove dark-mode class from body
                if (icon) icon.textContent = '🌙'; // Change icon to moon, check if icon exists
                if (label) label.textContent = 'Dark Mode'; // Label should say "Dark Mode" when dark mode is OFF
            }
            localStorage.setItem('theme', theme); // Save preference in browser's local storage
        }

        // --- Initialization on page load ---
        // Get saved theme from localStorage, default to 'light' if no preference is saved
        const savedTheme = localStorage.getItem('theme') || 'light';
        // Apply the saved theme immediately when the page loads
        setTheme(savedTheme);

        // --- Event Listener for Toggle Button ---
        // Only attach the event listener if the toggle button element is found
        if (toggle) {
            toggle.addEventListener('click', () => {
                // Determine the NEW theme based on the *current* state of the body
                // If body currently has 'dark-mode', the new theme will be 'light'.
                // If body currently does NOT have 'dark-mode', the new theme will be 'dark'.
                const newTheme = body.classList.contains('dark-mode') ? 'light' : 'dark';
                setTheme(newTheme); // Apply the new theme
            });
        } else {
            console.warn("Theme toggle button with ID 'theme-toggle' not found.");
        }
    });
    