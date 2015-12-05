# Appium Proof-of-Concept

This is a proof-of-concept using the Appium framework to demonstrate testing a simple mobile application on Android. The tests are written in Python 3.4 using the Appium Python library and PyTest.

## Setting up
In order to run the tests you need the following:

* Appium (http://appium.io/getting-started.html?lang=en)
* Android Studio (http://tools.android.com/download/studio)

## Running the tests
To run Appium tests you need to have the Appium server running (see Appium documentation) and the Android emulator running.

After cloning the repository you can open a command prompt in the root of the repository and execute the following two commands to run the tests:

    setup
    run

This will create a new Python virtual environment, install PyTest and the Appium Python library and then run the tests.