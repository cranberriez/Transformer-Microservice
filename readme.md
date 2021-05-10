# Transformer Service for CS 361
#### By Jacob Vilevac

This application uses electron to create a node-js based application to run the code and provide and application style web-page.

## Installation
#### Requirements:
- Node.js
- Npm

#### Running the Application in a Dev State
1. `npm i` Installs required node packages including electron, and electron-forge/cli
2. `npm start` This will run the application, opening the electron app with full functionality

#### Generating Application Distributable
1. `npm make` This packages the application and creates an out/ directory, containing the application.
- Installer file is located in out/make/ directory. The installer for windows creates a shortcut on the desktop and install files to `%APPDATA%/local/Transformer/`
- A less packaged but functioning version for windows is found in `out/transformer-win32-x64`