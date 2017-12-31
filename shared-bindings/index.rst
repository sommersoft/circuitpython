Core Modules
========================================

These core modules are intended on being consistent across ports. Currently
they are only implemented in the SAMD21 and ESP8266 ports. A module may not exist
in a port if no underlying hardware support is present or if flash space is
limited. For example, a microcontroller without analog features will not have
`analogio`.

.. _module-support-matrix:

Support Matrix
---------------

=================  =======  ==============  =======  =======  =======  =======
Module / Port      SAMD21   SAMD21 Express  SAMD51   ESP8266  nRF51    nFR52
=================  =======  ==============  =======  =======  =======  =======
`analogio`         **Yes**  **Yes**         **Yes**  **Yes**
`audiobusio`       **Yes**  **Yes**         **Yes**  No
`audioio`          No       **Yes**         No       No
`bitbangio`        No       **Yes**         No       **Yes**
`board`            **Yes**  **Yes**         **Yes**  **Yes**
`busio`            **Yes**  **Yes**         **Yes**  **Yes**
`digitalio`        **Yes**  **Yes**         **Yes**  **Yes**
`gamepad`          No       **Yes**         No       No
`math`             **Yes**  **Yes**         **Yes**  **Yes**
`microcontroller`  **Yes**  **Yes**         **Yes**  **Yes**
`multiterminal`    No       No              No       **Yes**
`neopixel_write`   **Yes**  **Yes**         **Yes**  **Yes**
`nvm`              No       **Yes**         No       No
`os`               **Yes**  **Yes**         **Yes**  **Yes**
`pulseio`          **Yes**  **Yes**         **Yes**  No
`random`           **Yes**  **Yes**         **Yes**  **Yes**
`storage`          **Yes**  **Yes**         **Yes**  **Yes**
`struct`           **Yes**  **Yes**         **Yes**  **Yes**
`supervisor`       **Yes**  **Yes**         **Yes**  No
`time`             **Yes**  **Yes**         **Yes**  **Yes**
`touchio`          **Yes**  **Yes**         **Yes**  No
`uheap`            Debug    Debug           Debug    Debug
`usb_hid`          **Yes**  **Yes**         **Yes**  No
=================  =======  ==============  =======

Modules
---------

.. toctree::
    :glob:
    :maxdepth: 3

    */__init__
    help
