# NISAR S-band SAR Backscatter Analysis and Urban/Non-Urban Classification

## About the Project

This project presents a simple practical analysis using NISAR S-band SAR data for the Kolkata study area.

## Aim

The aim of this practical work is to analyse NISAR SAR backscatter data and perform a simple urban and non-urban classification.

## Study Area

Kolkata was selected as the study area. A smaller Area of Interest (AOI) was used for easier processing and visualization.

## Dataset

NISAR S-band SAR HHHH polarization data was used for the analysis.

The original data was available in HDF5 format. A smaller spatial subset was prepared and converted into GeoTIFF format.

## Software Used

- QGIS
- ArcGIS Pro

## Methodology

NISAR Data → HHHH Extraction → Spatial Subsetting → GeoTIFF → dB Conversion → Urban/Non-Urban Classification → Cleaning → Final Overlay

## Technical Study

This project includes a basic study of the NISAR mission, data products, data processing workflow, applications, and the Bhoonidhi Portal.

## Practical Demonstration

The practical demonstration was carried out using NISAR S-band HHHH data for the Kolkata study area. The data was processed to prepare backscatter, dB, urban/non-urban classification, and final overlay maps.

## Results

Four main maps were prepared:

1. Original NISAR SAR Backscatter Map
2. NISAR SAR Backscatter Map in dB
3. Initial and Cleaned Urban/Non-Urban Classification
4. Final NISAR Backscatter and Urban Classification Overlay

## Limitations

The classification uses a simple threshold-based method. Therefore, some classification errors may occur.

## Future Work

Future work can include:

- Using multiple NISAR observations
- Using additional SAR polarizations
- Using multi-temporal NISAR data
- Combining NISAR with Sentinel-2 data
- Applying machine learning methods
- Using reference or ground-truth data
- Performing accuracy assessment
- Conducting urban change detection

## Documentation

The detailed technical report, methodology, and processing steps are provided in this repository.

## Author

Ankita Acharjee
