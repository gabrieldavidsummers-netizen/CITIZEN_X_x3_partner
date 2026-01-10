[app]
# (str) Title of your application
title = CITIZEN_X_PARTNER

# (str) Package name
package.name = citizen_x_partner

# (str) Package domain (needed for android packaging)
package.domain = org.sovereign

# (str) Source code where the main.py lives
source.dir = .

# (list) Source files to include (letting the database in is critical)
source.include_exts = py,png,jpg,kv,atlas,db

# (str) Application versioning
version = 4.8

# (list) Application requirements
# Note: kivy==2.3.0 is required for the Partner UI logic
requirements = python3,kivy==2.3.0,hostpython3,android,sqlite3

# (str) Supported orientation
orientation = portrait

# (bool) Indicate if the application should be fullscreen
fullscreen = 1

# (list) Permissions
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

# (list) Architecture Strike
# Covering both modern and legacy phone dialects
android.archs = arm64-v8a, armeabi-v7a

# (bool) Block external logic-gate backups
android.allow_backup = False

# (int) Android API to use
android.api = 31

# (int) Minimum API required
android.minapi = 21

# (str) Android NDK version (Force alignment with the runner)
android.ndk = 25b

# (bool) Accept the SDK license automatically
android.accept_sdk_license = True

[buildozer]
# (int) Log level (2 = high intensity detail)
log_level = 2

# (int) Display warning if buildozer is run as root (1 = True)
warn_on_root = 1
