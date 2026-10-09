[app]
title = Space Dodger
package.name = spacedodger
package.domain = org.spacedodger

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json,txt
source.exclude_dirs = tests, bin, .github, __pycache__, .buildozer

version = 1.0.0
requirements = python3,kivy

orientation = portrait
fullscreen = 1

# آیکون‌ها: اگه فایلشون رو داری اینا رو نگه دار، وگرنه با # کامنت کن
icon.filename = %(source.dir)s/icon.png
presplash.filename = %(source.dir)s/presplash.png
presplash.color = #0A0A0E

# --- Android ---------------------------------------------------------
# فقط یک معماری برای کاهش زمان بیلد و جلوگیری از کمبود حافظه
android.archs = arm64-v8a

android.allow_backup = True
android.accept_sdk_license = True
android.api = 33
android.minapi = 24
android.ndk = 25b
android.sdk = 24.0

# --- مهم‌ترین بخش: پین کردن نسخه p4a ---
# به جای master (که Python 3.14 خرابکار میاره)، از یه نسخه پایدار استفاده می‌کنیم
p4a.branch = v2024.01.21

[buildozer]
log_level = 2
warn_on_root = 1
