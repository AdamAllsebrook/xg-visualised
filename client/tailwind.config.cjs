/** @type {import('tailwindcss').Config} */
module.exports = {
    content: ['./src/**/*.{html,js,svelte,ts}'],
    theme: {
        extend: {
            colors: {
                primary: {
                    900: '#0E0B23',
                    800: '#1C1934',
                    700: '#2A2745',
                },
                secondary: '#00ff7f',
                accent1: 'orange',
                accent2: 'red',
                white: 'white',
                grey: '#999',
                black: '#060606',
            },
        },
        fontFamily: {
            display: ['Merriweather', 'system-ui'],
        },
    },
    plugins: [],
};
