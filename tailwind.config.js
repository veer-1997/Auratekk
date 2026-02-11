/** @type {import('tailwindcss').Config} */
module.exports = {
    content: [
        "./**/*.html",
        "./**/*.js",
        "!./node_modules/**"
    ],
    darkMode: 'class',
    theme: {
        extend: {
            colors: {
                'accent-gold': '#C5A059',
                'background-dark': '#0a0a0a',
                'background-light': '#f8f9fa',
            },
            fontFamily: {
                'display': ['Space Grotesk', 'sans-serif'],
                'body': ['Inter', 'sans-serif'],
                'mono': ['Space Mono', 'monospace'],
            },
        },
    },
    plugins: [
        require('@tailwindcss/forms'),
    ],
}
