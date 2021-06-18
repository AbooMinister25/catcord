/* eslint-disable camelcase */
const path = require('path')
const CopyPlugin = require('copy-webpack-plugin')
const WebpackPwaManifest = require('webpack-pwa-manifest')

const {
  meta, 
  port,
} = require('./config')

const plugins = [
  new CopyPlugin({
    patterns: [
      {
        from: 'public',
        to: '', 
      },
    ],

    options: {
      concurrency: 100,
    },
  }),
]

if (process.env.NODE_ENV === 'production') {
  plugins.push(    
    new WebpackPwaManifest({
      name: meta.title,
      short_name: meta.title,
      start_url: '/',
      description: meta.description,
      background_color: meta.themeColor,
      crossorigin: 'use-credentials',
      // icons: [
      //   {
      //     src: path.resolve('src/assets/logo.png'),
      //     sizes: [96, 128, 192, 256, 384, 512], // multiple sizes
      //   },
      //   {
      //     src: path.resolve('src/assets/large-icon.png'),
      //     size: '1024x1024', // you can also use the specifications pattern
      //   },
      //   {
      //     src: path.resolve('src/assets/maskable-icon.png'),
      //     size: '1024x1024',
      //     purpose: 'maskable',
      //   },
      // ],
    }),
  )
}

const sassLoader = [
  'css-loader',
  {
    loader: 'sass-loader',
    options: {
      sassOptions: {
        indentedSyntax: true,
        includePaths: [path.resolve(__dirname, 'src', 'sass')],
      },
    },
  },
]

module.exports = () => ({
  plugins,

  module: {
    rules: [
      {
        test: /\.tsx?$/,
        use: 'ts-loader',
        exclude: /node_modules/,
      },
      {
        test: /\.sass$/,
        use: sassLoader,
      },
      {
        test: /\.(mp4|webm|webp|png|jpg|gif|woff|woff2|eot|ttf|otf)$/,
        use: [
          {
            loader: 'file-loader',
            options: {
              esModule: false,
            },
          },
        ],
      },
    ],
  },

  resolve: {
    alias: {
      '@': path.resolve(__dirname, 'src'),
      'config': path.resolve(__dirname, 'config.js'),
      'css': path.resolve(__dirname, 'src/css'),
      'sass': path.resolve(__dirname, 'src/sass'),
      'assets': path.resolve(__dirname, 'src/assets'),
    },
    extensions: ['.tsx', '.ts', '.js', '.jsx'],
  },

  entry: {
    index: './src/pages/index.tsx',
  },

  output: {
    path: path.resolve(__dirname, 'dist'),
    filename: "bundle.js",
  },

  devtool: 'source-map',

  devServer: {
    port: port,
    host: '0.0.0.0',
    historyApiFallback: true,
  },
})