[app]
title = Calculator
package.name = system_calc_v4
package.domain = org.sovereign.tools
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,db
version = 4.8
requirements = python3,kivy==2.3.0,hostpython3,android,sqlite3
orientation = portrait
fullscreen = 1
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = False
android.api = 31
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
