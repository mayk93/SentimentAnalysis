#!/usr/bin/env bash

CURRED_DIR=$(pwd)

django-admin startproject Backend

cd Backend/Backend

touch views.py

cd $CURRED_DIR

mkdir Frontend

cd Frontend

echo "node_modules/webpack/bin/webpack.js" > buildwp.sh

echo '''
{
  "name": "simple_app",
  "version": "1.0.0",
  "description": "Simple app",
  "main": "index.js",
  "repository": "https://github.com/mayk93",
  "scripts": {
    "start": "node ./node_modules/webpack-dev-server/bin/webpack-dev-server.js",
    "test": "mocha --compilers js:babel-core/register --require ./test/test_helper.js --recursive ./test",
    "test:watch": "npm run test -- --watch"
  },
  "author": "",
  "license": "ISC",
  "devDependencies": {
    "babel-core": "^6.2.1",
    "babel-loader": "^6.2.0",
    "babel-preset-es2015": "^6.1.18",
    "babel-preset-react": "^6.1.18",
    "chai": "^3.5.0",
    "chai-jquery": "^2.0.0",
    "jquery": "^2.2.1",
    "jsdom": "^8.1.0",
    "mocha": "^2.4.5",
    "react-addons-test-utils": "^0.14.7",
    "webpack": "^1.12.9",
    "webpack-dev-server": "^1.14.0"
  },
  "dependencies": {
    "babel-preset-stage-1": "^6.1.18",
    "lodash": "^3.10.1",
    "react": "^0.14.3",
    "react-dom": "^0.14.3",
    "react-redux": "^4.0.0",
    "react-router": "^2.0.1",
    "redux": "^3.0.4",
    "redux-promise": "^0.5.3",
    "redux-thunk": "^2.1.0"
  }
}
''' > package.json

echo """
module.exports = {
  entry: [
    './src/index.js'
  ],
  output: {
    path: __dirname,
    publicPath: '/',
    filename: 'bundle.js'
  },
  module: {
    loaders: [{
      exclude: /node_modules/,
      loader: 'babel',
      query: {
        presets: ['react', 'es2015', 'stage-1']
      }
    }]
  },
  resolve: {
    extensions: ['', '.js', '.jsx']
  },
  devServer: {
    historyApiFallback: true,
    contentBase: './'
  }
};
""" > webpack.config.js

echo '''
{
  "presets": ["react", "es2015", "stage-1"]
}
''' > .babelrc

echo """
<!DOCTYPE html>
<html>
  <head>
    <link rel="stylesheet" href="/style/style.css">
    <link rel="stylesheet" href="https://cdn.rawgit.com/twbs/bootstrap/48938155eb24b4ccdde09426066869504c6dab3c/dist/css/bootstrap.min.css">
  </head>
  <body>
    <div class="container"></div>
  </body>
  <script src="/bundle.js"></script>
</html>
""" > index.html

mkdir style

mkdir src
cd src

echo """
import React from 'react';
import ReactDOM from 'react-dom';
import { Provider } from 'react-redux';
import { createStore, applyMiddleware, compose } from 'redux';
import thunk from 'redux-thunk';
import promiseMiddleware from 'redux-promise';

import App from './components/app';
import reducers from './reducers';

const createStoreWithMiddleware = compose(applyMiddleware(thunk, promiseMiddleware))(createStore);

ReactDOM.render(
  <Provider store={createStoreWithMiddleware(reducers)}>
    <App />
  </Provider>
  , document.querySelector('.container'));
""" > index.js

mkdir actions
touch actions/index.js

mkdir reducers
echo """
import {combineReducers} from 'redux';

const rootReducer = combineReducers({
});

export default rootReducer;
""" > reducers/index.js


mkdir components
echo """
import React from 'react';
import {Component} from 'react';

export default class App extends Component {
    render() {
        return (
            <div>Basic functionality established.</div>
        );
    }
}
""" > components/app.js

cd ..

yarn install

bash buildwp.sh

cd $CURRED_DIR