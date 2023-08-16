const path = require('path');
const ReactSlider = require('react-slider');

module.exports = {
  entry: ['./src/index.js'],
  output: {
    filename: 'main.js',
    path: path.resolve(__dirname, 'dist'),
  },
  resolve: [
    '.css', '.json', '.js', '.html', '.csv'
  ]
};
