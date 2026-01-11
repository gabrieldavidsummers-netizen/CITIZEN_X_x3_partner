# (Force these specific versions to match the Docker Forge)
android.api = 33
android.minapi = 21
android.ndk = 25b
android.ndk_api = 21

# (CRITICAL: Only build for the architecture of the phone to save RAM/Time)
android.archs = arm64-v8a

# (Ensure these are stripped for the Partner build)
android.permissions = INTERNET, ACCESS_COARSE_LOCATION, ACCESS_FINE_LOCATION

# (Disable the auto-update of requirements that bricks the build)
p4a.branch = master
