# stop script on error
set -e

# Check to see if root CA file exists, download if not
if [ ! -f ./root-CA.crt ]; then
  printf "\nDownloading AWS IoT Root CA certificate from Symantec...\n"
  curl https://www.symantec.com/content/en/us/enterprise/verisign/roots/VeriSign-Class%203-Public-Primary-Certification-Authority-G5.pem > root-CA.crt
fi

# install AWS Device SDK for NodeJS if not already installed
if [ ! -d ./node_modules ]; then
  printf "\nInstalling AWS SDK...\n"
  npm install aws-iot-device-sdk
fi

# run pub/sub sample app using certificates downloaded in package
printf "\nRuning pub/sub sample application...\n"
node node_modules/aws-iot-device-sdk/examples/device-example.js --host-name=a3qke5w34jrfmn.iot.ap-southeast-1.amazonaws.com --private-key=Rpi_iot_test.private.key --client-certificate=Rpi_iot_test.cert.pem --ca-certificate=root-CA.crt