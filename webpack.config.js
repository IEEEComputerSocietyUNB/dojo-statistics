let path = require('path')
let webpack = require('webpack')

module.exports = {
    entry: './app/index.js',
    output: {
        path: path.resolve(__dirname, './dist'),
        filename: 'build.js'
    },
    module: {
        loaders: [
            {
                test: /\.vue$/,
                loader: 'vue'
            },
            {
                test: /\.js$/,
                loader: 'babel',
                exclude: /node_modules/
            }
        ]
    },
    babel: {
        "presets": ["es2015"],
        "plugins": ["transform-runtime"]
    },
    plugins: [
        new webpack.ExternalsPlugin('commonjs', [
            'electron'
        ])
    ]
}
