.. Purpose: This chapter aims to describe how the user starts to use QGIS. It
.. should be kept short with only few steps to get QGIS working with two layers.

.. _`label.getstarted`:

***************
Getting Started
***************

.. only:: html

   .. contents::
      :local:

This chapter provides a quick overview of installing QGIS, downloading QGIS
sample data, and running a first simple session visualizing raster and vector
data.

.. index:: Installation
.. _`label_installation`:

Installing QGIS
===============

QGIS project provides different ways to install QGIS depending on your platform.

Installing from binaries
------------------------

Standard installers are available for |win| MS Windows and |osx| macOS. Binary
packages (rpm and deb) or software repositories are provided for many flavors of
GNU/Linux |nix|.

For more information and instructions for your operating system check 
https://download.qgis.org.

Installing from source
----------------------

If you need to build QGIS from source, please refer to the installation
instructions. They are distributed with the QGIS source code in a file
called :file:`INSTALL`. You can also find them online at :source:`INSTALL.md`.


If you want to build a particular release and not the version in development,
you should replace ``master`` with the release branch (commonly in the
``release-X_Y`` form) in the above-mentioned link (installation instructions may differ).

Installing on external media
----------------------------

It is possible to install QGIS (with all plugins and settings) on a flash drive.
This is achieved by defining a :ref:`--profiles-path <profiles-path_option>` option
that overrides the default :ref:`user profile <user_profiles>` path and forces
**QSettings** to use this directory, too.
See section :ref:`env_options` for additional information.

.. Todo: Expand a bit on the process because the linked chapter does not tell
  more or find a more informative section.


.. index:: Data sample
.. _label_sampledata:
