/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "../ideNet/templates/*.html",
  ],
  theme: {
    extend: {},
  },
  plugins: [
    require('preline/plugin'),
  ],
}

