# Type these in Terminal for help in python
'''
help()
help> modules
help> keywords
help> symbols
help> topics

help> LISTS
help> TUPULS
help> STRINGS
help> TYPES
help> keywords if
help> if
help> lambda
help> while
help> with
help> !=
help> module os

# when you want to print the sub-groups
(.*) python (.*)
print(a.groups())
'''
"""
help> modules

Please wait a moment while I gather a list of all available modules...

OpenSSL             brain_dataclasses   jinja2              sshtunnel
__future__          brain_dateutil      jmespath            ssl
_abc                brain_fstrings      jsmin               sspi
_ast                brain_functools     json                sspicon
_asyncio            brain_gi            jsondiff            stat
_bisect             brain_hashlib       jwt                 statistics
_blake2             brain_http          keyword             string
_bootlocale         brain_io            knack               stringprep
_bz2                brain_mechanize     lazy_object_proxy   struct
_cffi_backend       brain_multiprocessing lib2to3             subprocess
_codecs             brain_namedtuple_enum linecache           sunau
_codecs_cn          brain_nose          locale              symbol
_codecs_hk          brain_numpy_core_fromnumeric logging             symtable
_codecs_iso2022     brain_numpy_core_function_base lzma                sys
_codecs_jp          brain_numpy_core_multiarray mailbox             sysconfig
_codecs_kr          brain_numpy_core_numeric mailcap             tabnanny
_codecs_tw          brain_numpy_core_numerictypes markupsafe          tabulate
_collections        brain_numpy_core_umath marshal             tarfile
_collections_abc    brain_numpy_ndarray math                telnetlib
_compat_pickle      brain_numpy_random_mtrand mccabe              tempfile
_compression        brain_numpy_utils   mimetypes           test
_contextvars        brain_pkg_resources mmap                tests
_csv                brain_pytest        mmapfile            textwrap
_ctypes             brain_qt            mmsystem            this
_ctypes_test        brain_random        mock                threading
_datetime           brain_re            modulefinder        time
_decimal            brain_six           msilib              timeit
_dummy_thread       brain_ssl           msrest              timer
_elementtree        brain_subprocess    msrestazure         tkinter
_functools          brain_threading     msvcrt              token
_hashlib            brain_typing        multiprocessing     tokenize
_heapq              brain_uuid          nacl                trace
_imp                builtins            netbios             traceback
_io                 bz2                 netrc               tracemalloc
_json               cProfile            nntplib             tty
_locale             calendar            nt                  turtle
_lsprof             certifi             ntpath              turtledemo
_lzma               cffi                ntsecuritycon       types
_markupbase         cgi                 nturl2path          typing
_md5                cgitb               numbers             unicodedata
_msi                chardet             oauthlib            unittest
_multibytecodec     chunk               odbc                urllib
_multiprocessing    cmath               opcode              urllib3
_opcode             cmd                 operator            uu
_operator           code                optparse            uuid
_osx_support        codecs              os                  venv
_overlapped         codeop              paramiko            vsts
_pickle             collections         parser              vsts_cd_manager
_py_abc             colorama            pathlib             vsts_info_provider
_pydecimal          colorsys            pdb                 warnings
_pyio               commctrl            perfmon             wave
_queue              compileall          pickle              wcwidth
_random             concurrent          pickletools         weakref
_sha1               configparser        pip                 webbrowser
_sha256             contextlib          pipes               websocket
_sha3               contextvars         pkg_resources       wheel
_sha512             continuous_delivery pkginfo             win2kras
_signal             copy                pkgutil             win32api
_sitebuiltins       copyreg             platform            win32clipboard
_socket             crypt               plistlib            win32com
_sqlite3            cryptography        poplib              win32con
_sre                csv                 portalocker         win32console
_ssl                ctypes              portalocker_tests   win32cred
_stat               curses              posixpath           win32crypt
_statistics         dataclasses         pprint              win32cryptcon
_string             datetime            profile             win32event
_strptime           dateutil            prompt_toolkit      win32evtlog
_struct             dbi                 pstats              win32evtlogutil
_symtable           dbm                 pty                 win32file
_testbuffer         dde                 py_compile          win32gui
_testcapi           decimal             pyclbr              win32gui_struct
_testconsole        difflib             pycparser           win32help
_testimportmultiple dis                 pydoc               win32inet
_testmultiphase     distutils           pydoc_data          win32inetcon
_thread             doc                 pyexpat             win32job
_threading_local    doctest             pygments            win32lz
_tkinter            dummy_threading     pylint              win32net
_tracemalloc        easy_install        pyreadline          win32netcon
_warnings           email               pythoncom           win32pdh
_weakref            encodings           pytz                win32pdhquery
_weakrefset         ensurepip           pywin               win32pdhutil
_win32sysloader     enum                pywin32_bootstrap   win32pipe
_winapi             errno               pywin32_testutil    win32print
_winxptheme         fabric              pywintypes          win32process
_xxsubinterpreters  faulthandler        queue               win32profile
_yaml               filecmp             quopri              win32ras
abc                 fileinput           random              win32rcparser
adal                fnmatch             rasutil             win32security
adodbapi            formatter           re                  win32service
aex_accounts        fractions           readline            win32serviceutil
afxres              ftplib              regcheck            win32timezone
aifc                functools           regutil             win32trace
antigravity         gc                  reprlib             win32traceutil
antlr4              genericpath         requests            win32transaction
applicationinsights getopt              requests_oauthlib   win32ts
argcomplete         getpass             rlcompleter         win32ui
argparse            gettext             runpy               win32uiole
array               glob                samples             win32verstamp
ast                 gzip                sched               win32wnet
astroid             hashlib             scp                 winerror
asynchat            heapq               secrets             winioctlcon
asyncio             hmac                select              winnt
asyncore            html                selectors           winperf
atexit              http                servicemanager      winreg
audioop             humanfriendly       setuptools          winsound
azclishell          idlelib             shelve              winxpgui
azure               idna                shlex               winxptheme
azure_functions_devops_build imaplib             shutil              wrapt
base64              imghdr              signal              wsgiref
bcrypt              imp                 site                xdrlib
bdb                 importlib           six                 xml
binascii            inspect             smtpd               xmlrpc
binhex              invoke              smtplib             xmltodict
bisect              io                  sndhdr              xxsubtype
brain_argparse      ipaddress           socket              yaml
brain_attrs         isapi               socketserver        zipapp
brain_builtin_inference isodate             sqlite3             zipfile
brain_collections   isort               sre_compile         zipimport
brain_crypt         itertools           sre_constants       zlib
brain_curses        javaproperties      sre_parse

Enter any module name to get more help.  Or, type "modules spam" to search
for modules whose name or summary contain the string "spam".

"""
'''
import email
from email import message
from email import *

pip search <module>
pip download <module>
pip install <module>
'''
