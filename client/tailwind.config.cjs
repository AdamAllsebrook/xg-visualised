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
                secondary: '#588646',
                accent1: 'orange',
                accent2: 'red',
                white: {
                    900: '#eee',
                    800: '#bbb',
                },
                grey: '#999',
                black: '#060606',

                shot: '#777',
                goal: '#588646',
                xg: '#36827F',
                // shot: '#6c6c6c',
                // goal: '#558A40',
                // xg: '#416462'
                // C33C54 #FC814A #FFBC42
            },
        },
        fontFamily: {
            display: ['Merriweather', 'system-ui'],
            body: ['system-ui'],
        },
    },
    plugins: [],
};
