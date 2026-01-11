[app]
# (Identity)
title = CITIZEN_X_x3
package.name = citizenx
package.domain = org.synthesis
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json,txt
version = 1.3.5.7.9

# (The Soul: Minimized to stop the 11-minute timeout)
# Removing extra libs ensures the linker doesn't hang.
requirements = python3,kivy,requests,certifi

# (The Interface)
orientation = portrait
fullscreen = 0
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, ACCESS_COARSE_LOCATION, ACCESS_FINE_LOCATION

# (The Forge: Hardware Alignment)
# API 33 matches the stable Ubuntu 22.04 toolchain
android.api = 33
android.minapi = 21
android.ndk = 25b
android.ndk_api = 21

# CRITICAL: arm64-v8a ONLY. 
# Building for multiple architectures is why the previous runs timed out.
android.archs = arm64-v8a

# (The Bridge)
p4a.branch = master
android.skip_update = True
android.accept_sdk_license = True
android.entrypoint = org.kivy.android.PythonActivity

# (Optimization)
# This prevents the compiler from spiraling into a loop
android.meta_data = com.google.android.gms.version=@integer/google_play_services_version

[buildozer]
log_level = 2
warn_on_root = 1
