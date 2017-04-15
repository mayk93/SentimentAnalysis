CURRENT_DIRECTORY=$(pwd)

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

cd $DIR

node_modules/webpack/bin/webpack.js

cp index.html ../Backend/static
cp bundle.js ../Backend/static
cp style/style.css ../Backend/static/style
cp -R images ../Backend/static

cp index.html ../Backend/static_serve
cp bundle.js ../Backend/static_serve
cp style/style.css ../Backend/static_serve/style
cp -R images ../Backend/static_serve

cd $CURRENT_DIRECTORY