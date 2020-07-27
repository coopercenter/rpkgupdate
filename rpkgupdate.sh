
sudo apt install -y build-essential libcurl4-gnutls-dev libxml2-dev libssl-dev 

sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E298A3A825C0D65DFD57CBB651716619E084DAB9

sudo add-apt-repository 'deb https://cloud.r-project.org/bin/linux/ubuntu bionic-cran35/'

sudo add-apt-repository sudo add-apt-repository 'deb ppa:ubuntugis/ppa'

sudo apt update -y

sudo apt-get install -y libssl-dev libcurl4-openssl-dev libudunits2-dev r-base

python /src/rpkgupdate.py

