.. Purpose: This chapter aims to describe how the user starts to use QGIS. It
.. should be kept short with only few steps to get QGIS working with two layers.

.. _`label.getstarted`:

***************
Getting Started
***************

.. only:: html

   .. contents::
      :local:

This chapter provides a quick overview of installing and configuring QGIS. 

On any PCA workstation, you will find an updated version of QGIS (if you need to install the software on a new computer, you can refer to our IT department or to our Geospatial Data department for support).

Whether you are using a pre-installed version of QGIS or you are installing a new version from scratch, it is very important to know how QGIS versions work. 

QGIS is a very prolific software with frequent updates and new version releases (every 4 months). This allows the developers to provide the community with constant support, both introducing new features and fixing in short time bugs and issues. 

This means that in a single year, 5 different versions of QGIS are available for download, but only one of them will be labelled as LTR (Longe Term Release), which is the suggested version for business use and that guarantees a longer continuity of features and tools along all the year, without big changes.

Furthermore, PCA's current QGIS workflow makes extensive use of add-ons and plugins specifically developed for our integrated DRS/GIS system.
For the functionality of each plugin to be guaranteed, it is important that all workstations use a version of QGIS previously tested by the Geospatial data department.

For these reasons, it is very important that all the workstations are using the same QGIS LTR version and that each update is previously authorized by the geospatial data team.

.. index:: Installation
.. _`label_installation`:

Installing QGIS
===============

As just described, several versions of QGIS exist at the same time and, often, the version currently chosen as the one to be used in our company is no longer among the versions available for download on the official software site.

On the understanding that the management of QGIS versions in corporate workstations is the responsibility of IT departments or geospatial data, to which reference can be made for any request for help, if, for a specific reason, you need to install a copy of QGIS in your own workstation, you can access to the current installation files in our server at the address *Z:\GeoSpatialData_Resources\QGIS_Resources\Current_QGIS_Installer*

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
.. _label~@~~~~~~~~~~~~~~~~~~~~~~~~~~
================================================




Let's now add some decorations in order to shape the map and export it out of
QGIS:

#. Select :menuselection:`View --> Decorations --> Scale Bar` menu
#. In the dialog that opens, check |checkbox| :guilabel:`Enable Scale Bar` option 
#. Customize the options of the dialog as you want
#. Press :guilabel:`Apply`
#. Likewise, from the decorations menu, add more items (north arrow, copyright...)
   to the map canvas with custom properties.
#. Click :menuselection:`Project --> Import/Export -->` |saveMapAsImage|
   :menuselection:`Export Map to Image...`
#. Press :guilabel:`Save` in the opened dialog
#. Select a file location, a format and confirm by pressing :guilabel:`Save`
   again.
#. Press :menuselection:`Project -->` |fileSave| :menuselection:`Save...` to
   store your changes as a :file:`.qgz` project file.

That's it! You can see how easy it is to visualize raster and vector layers in
QGIS, configure them and generate your map in an image format you can use in
other softwares. Let's move on to learn more about the available functionality,
features and settings, and how to use them.

.. note::
 To continue learning QGIS through step-by-step exercises, follow the
 :ref:`Training manual <QGIS-training-manual-index-reference>`.


.. Substitutions definitions - AVOID EDITING PAST THIS LINE
   This will be automatically updated by the find_set_subst.py script.
   If you need to create a new substitution manually,
   please add it also to the substitutions.txt file in the
   source folder.

.. |checkbox| image:: /static_images/qgis_common/checkbox.png
   :width: 1.3em
.. |dataSourceManager| image:: /static_images/qgis_common/mActionDataSourceManager.png
   :width: 1.5em
.. |fileSave| image:: /static_images/qgis_common/mActionFileSave.png
   :width: 1.5em
.. |labelingSingle| image:: /static_images/qgis_common/labelingSingle.png
   :width: 1.5em
.. |nix| image:: /static_images/qgis_common/nix.png
   :width: 1em
.. |osx| image:: /static_images/qgis_common/osx.png
   :width: 1em
.. |saveMapAsImage| image:: /static_images/qgis_common/mActionSaveMapAsImage.png
   :width: 1.5em
.. |symbology| image:: /static_images/qgis_common/symbology.png
   :width: 2em
.. |win| image:: /static_images/qgis_common/win.png
   :width: 1em
.. |zoomIn| image:: /static_images/qgis_common/mActionZoomIn.png
   :width: 1.5em
