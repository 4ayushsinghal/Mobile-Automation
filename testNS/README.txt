Requirements.
The parameters that you need to run this project are the following:

Define Global environment variables on Jenkins.
To be able to execute the pipeline in any system you have configured your Jenkins, you need to define several environment variables on the global configuration in Jenkins.

Fist, go to Manage Jenkins -> Configure System -> and on the Global properties section, add the following environment variables:

ANDROID_HOME: Directory where the Android SDK is located.
GIT_CREDENTIAL: Git API Access Tokens. This key is generated from the User Settings.
Variables needed on the Initial Configuration.
Once we had this environment variables set, we need to define several variables inside the pipeline, some of them will use the environment variables we defined on Jenkins.
