QGIS plugins
============

PCA maintains a growing collection of QGIS plugins designed to support
archaeological survey, field recording, data quality, post-excavation and
day-to-day GIS production.

The plugins are developed around PCA workflows and are intended to make common
tasks faster, safer and more consistent across projects.

.. note::

   PCA plugins are distributed through the internal PCA QGIS plugin repository.

   Use the PCA QGIS profile wherever possible so that the repository,
   permissions and related settings are configured automatically.

Keeping plugins up to date
--------------------------

Keeping plugins current ensures that you receive the latest bug fixes, workflow
improvements and compatibility updates.

#. Open QGIS.
#. Select :menuselection:`Plugins --> Manage and Install Plugins`.
#. Open the :guilabel:`Upgradeable` tab.
#. Review the available updates.
#. Select :guilabel:`Upgrade All`.
#. Restart QGIS if prompted.

.. image:: images/upgrade/open_plugins_window.png
   :alt: Opening the QGIS Manage and Install Plugins window
   :width: 760px
   :align: center
   :class: documentation-screenshot

.. image:: images/upgrade/plugins_upgradeable2.png
   :alt: Upgradeable plugins displayed in QGIS
   :width: 760px
   :align: center
   :class: documentation-screenshot

.. tip::

   The :guilabel:`Upgradeable` tab only appears when one or more installed
   plugins have an available update.

   If the tab is not displayed, your installed plugins are already up to date.

.. image:: images/upgrade/no_updates.png
   :alt: QGIS Plugin Manager with no outstanding updates
   :width: 760px
   :align: center
   :class: documentation-screenshot

Plugin directory
----------------

The catalogue below provides an overview of the tools currently distributed
through the PCA plugin repository.

.. container:: plugin-directory-intro

   Each plugin is designed for a specific part of the PCA geospatial workflow.
   Some are lightweight productivity tools, while others support complete
   archaeological survey, recording or post-excavation processes.

Raster and data conversion
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. container:: plugin-card

   .. image:: images/icons/raster-to-gpkg-converter.png
      :alt: Raster to GPKG Converter icon
      :width: 100px
      :class: plugin-icon

   **Raster to GPKG Converter**

   Converts raster datasets into GeoPackage raster layers and automatically
   builds pyramids for improved display performance.

   The plugin provides a consistent way to package orthophotos, survey imagery
   and other raster data into a portable GeoPackage format suitable for use in
   PCA QGIS and mobile GIS projects.

.. container:: plugin-card

   .. image:: images/icons/geopackage-to-shp-exporter.png
      :alt: GeoPackage to SHP Exporter icon
      :width: 100px
      :class: plugin-icon

   **GeoPackage to SHP Exporter**

   Exports each spatial layer contained in a GeoPackage into a separate ESRI
   Shapefile.

   Empty layers and non-spatial tables are excluded automatically, making the
   tool useful when preparing clean delivery folders or transferring selected
   datasets into legacy workflows.

Survey and fieldwork
~~~~~~~~~~~~~~~~~~~~

.. container:: plugin-card

   .. image:: images/icons/pca-geomax-survey-processing.png
      :alt: PCA Geomax Survey Processing icon
      :width: 100px
      :class: plugin-icon

   **PCA Geomax Survey Processing**

   Processes PCA survey data using the current Geomax code-list workflow and
   supports integration between survey data, GIS and the PCA DRS system.

   The plugin is a core component of the PCA survey-processing workflow. It
   works with raw survey data exported in Shapefile format and applies the
   structure required by the PCA Geomax code-list system.

   A dedicated help section is available from the plugin toolbar and provides
   additional information about processing steps and expected input data.

.. container:: plugin-card

   .. image:: images/icons/evaluation-trenches-generator.png
      :alt: Evaluation Trenches Generator icon
      :width: 600px
      :class: plugin-icon

   **Evaluation Trenches Generator**

   Generates archaeological evaluation trenches and prepares the supporting
   files required for GNSS setting-out.

   The tool provides a set of functions for creating evaluation trench layouts
   in QGIS and converting them into practical survey outputs for use in the
   field.

.. container:: plugin-card

   .. image:: images/icons/pca-fieldwalk-grid-generator.png
      :alt: PCA Fieldwalk Grid Generator icon
      :width: 100px
      :class: plugin-icon

   **PCA Fieldwalk Grid Generator**

   Creates standardised archaeological fieldwalking grids from a site boundary.

   The plugin generates a British National Grid-aligned 100-metre hectare grid
   together with an optional detailed collection grid using user-defined cell
   dimensions.

   Grid cells are labelled using a consistent PCA fieldwalking reference system
   and can be saved directly into the project GeoPackage with the required PCA
   styles.

.. container:: plugin-card

   .. image:: images/icons/uk-national-grid-reference-finder.png
      :alt: UK National Grid Map Reference Finder icon
      :width: 100px
      :class: plugin-icon

   **UK National Grid Map Reference Finder**

   Navigates directly to a location using a UK National Grid Reference.

   After a grid reference is entered, the map canvas zooms to the corresponding
   position and displays a temporary marker to highlight the location.

   This is particularly useful when working from coordinates supplied in field
   notes, reports, emails or project documentation.

Mergin Maps
~~~~~~~~~~~

.. container:: plugin-card

   .. image:: images/icons/mergin-projects-permits-adder.png
      :alt: Mergin Projects Permits Adder icon
      :width: 100px
      :class: plugin-icon

   **Mergin Projects Permits Adder**

   Adds and manages permitted Mergin Maps project folders within the QGIS
   settings.

   The plugin simplifies the configuration of approved project locations,
   prevents duplicated entries and allows existing paths to be updated through
   a dedicated interface.

Data quality and checking
~~~~~~~~~~~~~~~~~~~~~~~~~

.. container:: plugin-card

   .. image:: images/icons/pca-geometry-quality-control.png
      :alt: PCA Geometry Quality Control icon
      :width: 100px
      :class: plugin-icon

   **PCA Geometry Quality Control**

   Scans all vector layers in the current project for geometry problems that
   may affect editing, analysis or map production.

   The tool identifies null, empty and invalid geometries, summarises the
   results in a dedicated panel and provides quick actions for reviewing,
   selecting or removing problematic features.

   Layers can be excluded from the checks using the
   ``skip_geometry_check`` layer variable, and reports can be copied or
   exported for project records.

.. container:: plugin-card

   .. image:: images/icons/check-duplicated-features.png
      :alt: Check Duplicated Features icon
      :width: 100px
      :class: plugin-icon

   **Check Duplicated Features**

   Checks a vector layer for duplicated features.

   Duplicates can be identified using geometry alone or by combining geometry
   and attribute values. Once the check is complete, the results can be
   reviewed and, where appropriate, removed directly from the layer.

.. container:: plugin-card

   .. image:: images/icons/pca-drs-context-checks.png
      :alt: PCA DRS Context Checks icon
      :width: 100px
      :class: plugin-icon

   **PCA DRS Context Checks**

   Provides a collection of checks for PCA DRS context records during the
   post-excavation phase.

   The plugin can identify issues such as missing context sheets, duplicated
   context numbers and recorded features that do not match the site plan.

   Results are displayed in a dockable panel, allowing inconsistencies to be
   reviewed directly within QGIS.

Project and layer management
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. container:: plugin-card

   .. image:: images/icons/pca-data-source-explorer.png
      :alt: PCA Data Source Explorer icon
      :width: 100px
      :class: plugin-icon

   **PCA Data Source Explorer**

   Provides a structured overview of every data source used in the current QGIS
   project.

   File-based layers are grouped by folder and source file, making it easier to
   understand where project data is stored and how it is organised.

   The plugin distinguishes between project data, external files, missing
   sources, database connections and online services. Multi-layer formats such
   as GeoPackage and DXF can be expanded to show their internal layers.

   It can also identify repeated data sources and generate a text report
   containing the project name, project location and source summary.

.. container:: plugin-card

   .. image:: images/icons/search-value.png
      :alt: Search Value icon
      :width: 100px
      :class: plugin-icon

   **Search Value**

   Searches for values across a layer attribute table and navigates directly to
   matching geometries.

   When a result is found, the corresponding feature can be selected and the
   map canvas zoomed to its location.

   This is useful when locating context numbers, feature identifiers, drawing
   references or other recorded values in large datasets.

Editing tools
~~~~~~~~~~~~~

.. container:: plugin-card

   .. image:: images/icons/replace-clipped-geometry.png
      :alt: Replace Clipped Geometry icon
      :width: 100px
      :class: plugin-icon

   **Replace Clipped Geometry**

   Replaces the geometry of an existing feature while preserving all of its
   attributes and metadata.

   The plugin supports point, line and polygon layers and uses native QGIS
   snapping and advanced digitising tools.

   Optional clipping can constrain the replacement geometry to a selected or
   intersecting polygon, making the tool suitable for detailed archaeological
   and CAD-style editing workflows.

.. container:: plugin-card

   .. image:: images/icons/add-save-all-edits-shortcut.png
      :alt: Add Save All Edits Shortcut icon
      :width: 100px
      :class: plugin-icon

   **Add Save All Edits Shortcut**

   Adds quick access to the QGIS :guilabel:`Save Edits for All Layers`
   function.

   The plugin reduces the risk of leaving edits unsaved when working with
   several editable layers at the same time.

Post-excavation
~~~~~~~~~~~~~~~

.. container:: plugin-card

   .. image:: images/icons/pca-post-excavation-toolbar.png
      :alt: PCA Post-excavation icon
      :width: 700px
      :class: plugin-icon

   **PCA Post-excavation**

   Supports the management of archaeological post-excavation data directly
   within QGIS.

   The plugin helps maintain consistent groups, entities, periods, sub-periods
   and phases, updates related Interventions and DRS records, and prepares
   standardised exports for reporting and analysis.

   It is designed for routine archaeological GIS use and helps keep
   post-excavation datasets structured and consistent throughout the project.

.. container:: plugin-card

   .. image:: images/icons/pca-export-phased-features.png
      :alt: PCA Export Phased Features icon
      :width: 100px
      :class: plugin-icon

   **PCA Export Phased Features**

   Exports polygons from the ``Features_for_PostEx`` layer into separate phased
   ESRI Shapefiles.

   Features are grouped using post-excavation phasing fields. The workflow
   includes export validation, geometry safety checks, an export preview and QA
   logging.

.. container:: plugin-card

   .. image:: images/icons/pca-finds-distribution-generator.png
      :alt: PCA Finds Distribution Generator icon
      :width: 100px
      :class: plugin-icon

   **PCA Finds Distribution Generator**

   Creates archaeological finds-distribution layers directly from finds
   catalogues.

   The tool can also generate grouped summaries for contexts, cuts or other
   recording units, including combined quantities and weights.

   It is intended to make the preparation of finds-distribution outputs faster
   and more consistent.

Reporting and record output
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. container:: plugin-card

   .. image:: images/icons/pca-report-description-generator.png
      :alt: PCA Report Description Generator icon
      :width: 100px
      :class: plugin-icon

   **PCA Report Description Generator**

   Creates draft archaeological report descriptions directly from PCA DRS
   context records.

   The plugin supports cut, group and individual context descriptions and uses
   dedicated templates for fills, layers, masonry, skeletons, cremations and
   structures.

   Text is generated only from information recorded on the relevant context
   sheet, helping maintain consistency between field records and reporting.
   Generated descriptions should always be reviewed and refined before use in
   a final report.

.. container:: plugin-card

   .. image:: images/icons/pca-drs-context-sheet-printer.png
      :alt: PCA DRS Context Sheet Printer icon
      :width: 100px
      :class: plugin-icon

   **PCA DRS Context Sheet Printer**

   Generates clean, printable PDF recording sheets directly from PCA DRS
   databases.

   The plugin supports context, trench, cremation and skeleton records and uses
   native QGIS print layouts to create compact one-page outputs.

   It is designed as part of the integrated PCA DRS and GIS workflow.

Need help?
----------

.. container:: documentation-callout

   If a plugin is missing, does not update correctly or produces an unexpected
   result, contact the Geospatial Data Team and include:

   * the plugin name;
   * the QGIS version being used;
   * a screenshot of the problem;
   * the project location;
   * a brief description of the action that caused the issue.

   Providing these details will make it easier to investigate the problem
   quickly.
