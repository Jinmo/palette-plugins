## Overview

This plugin is process memory dumper for OllyDbg and Immunity Debugger.
Very simple overview:

**OllyDumpEx = OllyDump + PE Dumper - obsoleted + useful features**

### Features

Various debuggers supported
Select to dump debugee exe, loaded dll or non-listed module
Search PE File from memory
Multiple Dump mode. Rebuild for typical PE dump, Binary for PE Carving
PE32+ supported (Search and Binary Dump mode only available on 32bit debugger)
Native 64bit process supported (IDA Pro, WinDbg and x64dbg)
ELF supported (both of 32bit and 64bit)
Standalone version available
Dump any address space as section even if not in original section header
Auto calculate many parameters (RawSize, RawOffset, VirtualOffset, ...)

### Screenshot

![OllyDumpEx_32bit](https://low-priority.appspot.com/ollydumpex/ollydumpex_ss0.png)
![OllyDumpEx_64bit](https://low-priority.appspot.com/ollydumpex/ollydumpex_ss1.png)
![OllyDumpEx_ELF](https://low-priority.appspot.com/ollydumpex/ollydumpex_ss2.png)

### Supported Debugger

- OllyDbg version 1.10 (tested 1.10)
- OllyDbg version 2.01 (tested 2.01)
- Immunity Debugger version 1.8x or higher (tested 1.85)
- IDA Pro 32bit build version 5.0 or higher (tested 6.9)
- IDA Pro 64bit build version 7.0 or higher (tested 7.1)
- IDA Freeware 32bit build version 5.0 (tested 5.0)
- IDA Freeware 64bit build version 7.0 (tested 7.0.190307)
- WinDbg version 6.x (tested 6.2)
- x64dbg (tested 20170822 snapshot)

### Recent Changes & Archives
- v1.72 / 2019-03-14
  - Improve: Support IDA Freeware with debugger version 7.0.190307
- v1.70 / 2018-08-14
  - Bugfix: Dump feature not working when non-executable file loaded (IDA)
  - Bugfix: Readmemory sign extended issue (WinDbg)
  - Bugfix: Fix Virtual Offset not working on PE32
  - Bugfix: Fix duplicated entry in section list
  - Improve: Get EIP as OEP button disabled when debugger not active
  - Improve: Add EFI and windows driver type detection
  - Improve: Better fix for corrupted PE IMAGE_DIRECTORY_ENTRY
  - Improve: Add Cancel feature to search and dump
  - Add: Search All Occurrences option and Search Result list
- v1.64 / 2018-05-10
  - Improve: Follow IDA 7.1 changes which break callui backward compatibility layer
  - Improve: Dump feature available even if debuggee not running (IDA)
  - Add: Support IDA Freeware version 7.0 (EXPERIMENTAL)
- v1.62 / 2017-11-05
  - Bugfix: Rebuild dumpfile corrupted when ELF PT_PHDR entry not exist
  - Bugfix: Failed to load ELF header when sparse segment layout
  - Improve: Corrupted ELF structure handling
  - Improve: ELF Loader segment always aligned same as mmap behavior
- v1.60 / 2017-09-19
  - Add: ELF support
  - Add: Standalone version
  - Add: Support IDA Pro 64bit build plugin interface (7.0)
  - Improve: Image Size editable in binary dump mode for overlay data
  - Del: Drop old version of Immunity Debugger support (1.7x)
- v1.50 / 2015-07-03
  - Add: Fuzzy Search mode (for corrupted MZ/PE Signature)
  - Add: Fix Corrupted PE Header option (Fill Hole option is merged)
  - Add: Dump result dialog for copy and paste
  - Improve: Search method optimization
  - Improve: Corrupted PE Header handling
  - Improve: Binary dump mode support some options
  - Bugfix: Rebased PE handling (rebuild dump mode)
  - Bugfix: Debuggee filename error on attached process (IDA)
  - Bugfix: Get EIP does not work in recent version (x64dbg)
- v1.40 / 2014-12-17
  - Add: Support x64dbg plugin interface (both 32bit and 64bit)
  - Improve: Enable NXCOMPAT and DYNAMICBASE for plugin binaries
- v1.30 / 2013-06-28
  - Add: Support WinDbg plugin interface (both 32bit and 64bit)
  - Improve: Add plugin name and version directory to archive file
  - Bugfix: Data after section headers in PE Header has been ignored
  - Bugfix: Fix SizeOfHeaders inconsistency
- v1.20 / 2013-05-27
  - Add: Support IDA Pro plugin interface (both Retail and Freeware version)
  - Add: Support native 64bit process dump (IDA Pro only)
  - Improve: Change dialog position to center of parent window
  - Improve: Add debug toggle menu to dialog system menu
  - Improve: Section size handling single section belongs to multiple memory segments
  - Bugfix: Zero virtual size section handling
- v1.12 / 2013-04-02
  - Improve: Update to OllyDbg 2 latest version PDK (2.01h)
  - Improve: Tested with latest version of debuggers
  - Bugfix: Search greater than 0x7FFFFFFF memory address failed
- v1.10 / 2013-03-24
  - Add: Search type All Memory
  - Add: Binary dump mode (no rebuild PE header, for before load image)
  - Add: PE32+ support (Binary dump mode only)
  - Add: Memory Address/Size parameters editable (dump source address)
  - Improve: Add info message for Relocation Flag and EXE/DLL type
  - Improve: Large PE Header handling (larger than 0x1000)
  - Improve: Check SectionAlignment and FileAlignment consistency
  - Improve: Reduce search memory usage (not depend on target memory size)
  - Improve: Detect PE Header across different type pages (parse and search)
  - Bugfix: Improper owner window handle
  - Bugfix: Section not listed when belong memory range not exists
  - Bugfix: Almost features broken when memory window sort order changed
- v1.00 / 2013-03-12
  - Add: Selectable Base PE Header (Module/Memory/Address)
  - Add: Search PE Header from memory
  - Improve: PE Source default change Disk to Memory
  - Improve: ASLR aware (except PE Source from Disk mode)
  - Improve: Clear DynamicBase DllCharacteristics flag with Disable Relocation option
  - Improve: PE Header parse and modify more carefully (corrupt PE handling)
  - Improve: Inherit selected address from memory window
  - Bugfix: Fix Virtual Offset feature cause crash (divide by zero)
  - Bugfix: Parse invalid sections cause crash
- v0.92 / 2012-10-09
  - Improve: Support OllyDbg version 2 plugin new interface
- v0.90 / 2011-08-24
  - Add: Support OllyDbg version 2 plugin interface (EXPERIMENTAL)
  - Improve: Rewrite Wide/Multibyte-Character support code
  - Improve: Decode CopyOnWrite page attribute
  - Bugfix: Detect working directory
- v0.80 / 2011-07-15
  - Add: Support Immunity Debugger version 1.8x or higher
  - Improve: Data Directory rebuild option (check rewrite range)
  - Improve: Always round up PE header size to 0x1000 (ImportRec not extend itself)
  - Bugfix: TLS Data Directory ignored
