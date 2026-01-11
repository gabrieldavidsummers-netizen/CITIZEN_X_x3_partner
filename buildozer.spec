[app]
# (Section 1: Identity)
title = CITIZEN_X_Partner
package.name = citizen_x_partner
package.domain = org.sovereign.engine
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json
version = 1.3.5.7.9

# (Section 2: The Bypass)
# This excludes the legacy garbage that murdered your last build
source.exclude_patterns = tests/*, bin/*, lib2to3/*, **/test_*.py

# (Section 3: Requirements)
# Ensure these match your "One Project" dependencies exactly
requirements = python3,kivy,hostpython3,requests,urllib3

# (Section 4: Android Hardening)
orientation = portrait
fullscreen = 1
android.archs = arm64-v8a
android.api = 33
android.minapi = 21
android.ndk = 25b
android.skip_update = False
android.accept_sdk_license = True

# (Section 5: Permissions - The Body's Sensors)
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE,CAMERA

[buildozer]
log_level = 2
warn_on_root = 1
