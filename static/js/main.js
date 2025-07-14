// C:\Users\ashok_wsg2ds5\my-pythonDjango1\static\js\main.js

document.addEventListener('DOMContentLoaded', function() {
    console.log("main.js: DOMContentLoaded fired.");

    // --- REMOVE THIS LINE: localStorage.clear(); ---
    // This line was for debugging only and should NOT be present in production or normal use.
    // localStorage.clear();
    // console.log("main.js: localStorage cleared for debugging.");
    // --- END REMOVAL ---

    const toggle = document.getElementById('theme-toggle');
    const body = document.body;
    const icon = document.getElementById('theme-icon');
    const label = document.getElementById('theme-label');

    // Get all elements that should change background/text color
    const contentCards = document.querySelectorAll('.content-card');
    const postArticleCards = document.querySelectorAll('.post-article-card');
    const categoryTagSpans = document.querySelectorAll('.category-tag-span');
    const commentCards = document.querySelectorAll('.comment-card');

    // Get all headings and labels that might need color adjustment
    const headings = document.querySelectorAll('h1, h2, h3, h4, h5, h6');
    const labels = document.querySelectorAll('label'); // Select label elements


    console.log("main.js: toggle element found?", !!toggle);
    console.log("main.js: body element found?", !!body);

    // Define theme colors directly in JS (matching style.css variables)
    const themes = {
        light: {
            bodyBg: '#f3f4f6', // Light gray background for body
            bodyText: '#000000', // Black text for body
            cardBg: '#ffffff', // White background for cards
            cardText: '#374151', // Dark gray text for cards
            link: '#007bff', // Blue link color
            navBg: '#f1f1f1', // Navbar light background
            inputBg: '#ffffff',
            inputText: '#374151',
            inputBorder: '#d1d5db',
            buttonBg: '#4a5568',
            buttonText: '#ffffff',
        },
        dark: {
            bodyBg: '#121212', // Dark background for body
            bodyText: '#f1f1f1', // Light text for body
            cardBg: '#1a202c', // Darker background for cards
            cardText: '#e2e8f0', // Lighter text for dark cards
            link: '#80d0ff', // Lighter blue link color
            navBg: '#1f1f1f', // Navbar dark background
            inputBg: '#2d3748',
            inputText: '#f1f1f1',
            inputBorder: '#4a5568',
            buttonBg: '#6366f1',
            buttonText: '#ffffff',
        }
    };

    // Function to apply the theme (dark or light)
    function setTheme(theme) {
        console.log("main.js: setTheme called with theme:", theme);
        const currentThemeColors = themes[theme];

        // Apply to body
        body.style.backgroundColor = currentThemeColors.bodyBg;
        body.style.color = currentThemeColors.bodyText;

        // Apply to navbar
        const navBar = document.querySelector('.navbar');
        if (navBar) {
            navBar.style.backgroundColor = currentThemeColors.navBg;
            navBar.style.color = currentThemeColors.bodyText;
            navBar.style.borderColor = currentThemeColors.inputBorder;
        }

        // Apply to content cards
        contentCards.forEach(card => {
            card.style.backgroundColor = currentThemeColors.cardBg;
            card.style.color = currentThemeColors.cardText;
            card.style.borderColor = currentThemeColors.inputBorder;
        });

        // Apply to post article cards
        postArticleCards.forEach(card => {
            card.style.backgroundColor = currentThemeColors.cardBg;
            card.style.color = currentThemeColors.cardText;
            card.style.borderColor = currentThemeColors.inputBorder;
        });

        // Apply to category/tag spans
        categoryTagSpans.forEach(span => {
            span.style.backgroundColor = currentThemeColors.link;
            span.style.color = currentThemeColors.bodyBg;
        });

        // Apply to comment cards
        commentCards.forEach(card => {
            card.style.backgroundColor = currentThemeColors.cardBg;
            card.style.color = currentThemeColors.cardText;
            card.style.borderColor = currentThemeColors.inputBorder;
        });

        // Apply to inputs, selects, textareas
        document.querySelectorAll('input:not([type="checkbox"]):not([type="radio"]), select, textarea').forEach(input => {
            input.style.backgroundColor = currentThemeColors.inputBg;
            input.style.color = currentThemeColors.inputText;
            input.style.borderColor = currentThemeColors.inputBorder;
        });

        // Apply to labels
        labels.forEach(labelElem => {
            labelElem.style.color = currentThemeColors.cardText;
        });

        // Apply to headings
        headings.forEach(heading => {
            heading.style.color = currentThemeColors.cardText;
        });

        // Apply to theme toggle button
        if (toggle) {
            toggle.style.backgroundColor = currentThemeColors.buttonBg;
            toggle.style.color = currentThemeColors.buttonText;
            toggle.style.borderColor = currentThemeColors.inputBorder;
        }

        localStorage.setItem('theme', theme);
        console.log("main.js: localStorage 'theme' after set:", localStorage.getItem('theme'));
        console.log("main.js: body background after setTheme:", body.style.backgroundColor);
    }

    // --- Initialization on page load ---
    const savedTheme = localStorage.getItem('theme') || 'light';
    setTheme(savedTheme);
    console.log("main.js: Initial theme applied:", savedTheme);

    // --- Event Listener for Toggle Button ---
    if (toggle) {
        toggle.addEventListener('click', () => {
            console.log("main.js: Toggle button clicked!");
            const currentTheme = localStorage.getItem('theme') || 'light';
            const newTheme = (currentTheme === 'dark') ? 'light' : 'dark';
            console.log("main.js: Calculated newTheme (based on localStorage):", newTheme);
            setTheme(newTheme);
        });
    } else {
        console.warn("Theme toggle button with ID 'theme-toggle' not found.");
    }
});
