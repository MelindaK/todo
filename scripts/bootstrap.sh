echo "Installing virtualenv"
sudo pip install virtualenv

virtualenv env
source ./env/bin/activate

echo "Installing requirements.txt"
pip install -r requirements.txt

npm install
