/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{js,jsx,ts,tsx}",],
  theme: {
    extend: {
       fontFamily: {
          'poppins': ['Poppins'],
          'inter':['Inter']
       },
       colors: {
         'ytred':'#FF44336',
       }
    }
 },
  plugins: [],
}
