--- lib/setup.py.orig	Fri Jan  4 08:08:55 2002
+++ lib/setup.py	Fri Jan  4 08:11:04 2002
@@ -18,23 +18,23 @@
 			author = "Robin Becker",
 			author_email = "robin@reportlab.com",
 			url = "http://www.reportlab.com",
-			packages = [],
-			ext_modules =	[Extension(	'_rl_accel',
-										['_rl_accel.c'],
+			packages = ['reportlab'],
+			ext_modules =	[Extension(	'reportlab.lib._rl_accel',
+										['reportlab/lib/_rl_accel.c'],
 										include_dirs=[],
 										define_macros=[],
 										library_dirs=[],
 										libraries=LIBS,	# libraries to link against
 										),
-							Extension(	'sgmlop',
-										['sgmlop.c'],
+							Extension(	'reportlab.lib.sgmlop',
+										['reportlab/lib/sgmlop.c'],
 										include_dirs=[],
 										define_macros=[],
 										library_dirs=[],
 										libraries=LIBS,	# libraries to link against
 										),
-							Extension(	'pyHnj',
-										['pyHnjmodule.c','hyphen.c', 'hnjalloc.c'],
+							Extension(	'reportlab.lib.pyHnj',
+										['reportlab/lib/pyHnjmodule.c','reportlab/lib/hyphen.c', 'reportlab/lib/hnjalloc.c'],
 										include_dirs=[],
 										define_macros=[],
 										library_dirs=[],
