/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    '../core/templates/**/*.html',
    '../templates/**/*.html',
  ],
  theme: {
    extend: {},
  },
  plugins: [
    require('@tailwindcss/typography'),
  ],
}

