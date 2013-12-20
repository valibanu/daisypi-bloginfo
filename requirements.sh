echo "Welcome to the 'Daisy Pi Blogger Analytics' installer"
echo "Installing the required packages ..."

echo "Installing pip (Python Package Manager) ..."
apt-get -q -y install python-setuptools
easy_install pip
echo "Finished installing pip!"

echo "Installing the rank_provider Python package ..."
sudo pip install rank_provider
echo "Finished installing rank_provider!"
