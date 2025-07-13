// C:\Users\ashok_wsg2ds5\my-pythonDjango1\static\js\main.js

    document.addEventListener('DOMContentLoaded', function() {
        console.log("main.js: DOMContentLoaded fired."); // Log on DOM ready

        const toggle = document.getElementById('theme-toggle');
        const body = document.body;
        const icon = document.getElementById('theme-icon');
        const label = document.getElementById('theme-label');

        console.log("main.js: toggle element found?", !!toggle); // Log if toggle is found
        console.log("main.js: body element found?", !!body); // Log if body is found

        function setTheme(theme) {
            console.log("main.js: setTheme called with theme:", theme); // Log when setTheme is called
            if (theme === 'dark') {
                body.classList.add('dark-mode');
                if (icon) icon.textContent = '☀️';
                if (label) label.textContent = 'Light Mode';
            } else {
                body.classList.remove('dark-mode');
                if (icon) icon.textContent = '🌙';
                if (label) label.textContent = 'Dark Mode';
            }
            localStorage.setItem('theme', theme);
            console.log("main.js: body classes after setTheme:", body.classList.value); // Log body classes
        }

        const savedTheme = localStorage.getItem('theme') || 'light';
        setTheme(savedTheme); // Initial theme application
        console.log("main.js: Initial theme applied:", savedTheme);

        if (toggle) {
            toggle.addEventListener('click', () => {
                console.log("main.js: Toggle button clicked!"); // Log on click
                const newTheme = body.classList.contains('dark-mode') ? 'light' : 'dark';
                setTheme(newTheme);
            });
        } else {
            console.warn("Theme toggle button with ID 'theme-toggle' not found.");
        }
    });
    