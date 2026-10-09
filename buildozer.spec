[app]
title = Space Dodger
package.name = spacedodger
package.domain = org.spacedodger

source.dir = .
source.include_exts = py,png,jpg,kv,atlas
source.exclude_dirs = tests, bin, .github, __pycache__, .buildozer

version = 1.0.0
requirements = python3,kivy

orientation = portrait
fullscreen = 1

icon.filename = %(source.dir)s/icon.png
presplash.filename = %(source.dir)s/presplash.png
presplash.color = #0A0A0E

# --- Android ---------------------------------------------------------
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True
android.accept_sdk_license = True
android.api = 33
android.minapi = 24
android.ndk = 25b
android.sdk = 24.0

[buildozer]
log_level = 2
warn_on_root = 1
