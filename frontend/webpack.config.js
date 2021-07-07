/* eslint-disable */
const path = require("path");
const HtmlWebpackPlugin = require("html-webpack-plugin");
const CopyWebpackPlugin = require("copy-webpack-plugin");

const config = require('./config.js')

const plugins = [
  new HtmlWebpackPlugin({
    template: "src/index.html"
  }),
  new CopyWebpackPlugin({
    patterns: [
      {
        from: "public",
        to: "",
      }
    ]
  })
];

module.exports = () => ({
  plugins,
  module: {
    rules: [
      {
        test: /\.(js|jsx|tsx|ts)$/,
        exclude: /node_modules/,
        use: {
          loader: "babel-loader",
        }
      },
      {
        test: /\.css$/i,
        use: [
          "style-loader", 
          {
            loader: "css-loader",
            options: {
              modules: true,
            },
          },
        ],
      },
      {
        test: /\.scss$/i,
        use: [
          'style-loader',
          'css-loader',
          'sass-loader'
        ],
      }
    ],
  },
  resolve: {
    alias: {
      "css": path.join(__dirname, "src/css"),
      "sass": path.join(__dirname, "src/sass"),
      "scss": path.join(__dirname, "src/scss"),
      "views": path.join(__dirname, "src/pages"),
      "~mixins": path.join(__dirname, "src", "scss", "mixins")
    },
    extensions: ["*", ".js", ".jsx", ".tsx", ".ts"]
  },
  entry: {
    app: path.resolve(process.cwd(), "src", "index.tsx")
  },
  output: {
    filename: '[name].js',
    path: path.resolve(process.cwd(), 'dist'),
    publicPath: "/"
  },
  mode: process.env.NODE_ENV,
  // devtool: process.env.NODE_ENV === 'production' ? 'none' : 'source-map',
  devServer: {
    port: config.port,
    host: '0.0.0.0',
    historyApiFallback: true
  }
});
