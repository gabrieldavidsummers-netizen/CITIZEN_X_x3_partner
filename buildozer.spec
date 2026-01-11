[app]

# (Basic Identity)
title = CITIZEN_X_x3
package.name = citizenx
package.domain = org.synthesis
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json,txt
version = 1.3.5.7.9

# (The Soul: Requirements)
requirements = python3,kivy,requests,certifi

# (The Body: Interface)
orientation = portrait
fullscreen = 0
android.permissions = INTERNET, ACCESS_COARSE_LOCATION, ACCESS_FINE_LOCATION, WRITE_EXTERNAL_STORAGE

# (The Forge: Hardware Alignment)
# API 33 is the stable baseline for Android 13/14
android.api = 33
android.minapi = 21
# Force NDK 25b to match the Docker workshop
android.ndk = 25b
android.ndk_api = 21
# CRITICAL: arm64-v8a covers 99% of modern phones. Reduces build time/RAM.
android.archs = arm64-v8a

# (The Bridge: Python-for-Android)
p4a.branch = master

# (The Interface: Visuals)
# icon.filename = %(source.dir)s/data/icon.png
# presplash.filename = %(source.dir)s/data/presplash.png

# (The Logic: Build Options)
android.skip_update = False
android.accept_sdk_license = True
android.entrypoint = org.kivy.android.PythonActivity

[buildozer]
# High intensity logging to see every strike on the anvil
log_level = 2
warn_on_root = 0
