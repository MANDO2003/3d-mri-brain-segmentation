# Web-Based 3D MRI Brain Segmentation and Visualization Tool

A web-based medical imaging application designed to perform 3D MRI volumetric segmentation and interactive 3D rendering directly inside the browser. By leveraging client-side deep learning models (MeshNet) powered by TensorFlow.js and WebGL/WebAssembly acceleration, this tool eliminates the need for expensive dedicated GPUs, cloud server dependencies, or specialized software installations while preserving 100% data privacy.

---

## 📌 Project Overview

Traditional neuroimaging tools require high-performance hardware, complex local software setup, or server-side data processing that can compromise patient privacy under regulations like GDPR. This project provides an accessible, browser-based, client-side solution that allows clinicians, radiologists, and researchers to process 3D NIfTI (`.nii`, `.nii.gz`) structural MRI scans locally on standard devices.

---

## ✨ Key Features

- **Client-Side Browser Processing**: All deep learning inference and calculations occur locally on the user's device using TensorFlow.js and WebAssembly (WASM). Medical data never leaves your computer.
- **Lightweight 3D Deep Learning Model**: Integrates optimized **MeshNet** architectures capable of performing full-volume 3D brain segmentation in a single pass.
- **Interactive 3D Volume Rendering**: Uses WebGL and Three.js to render 3D brain structures interactively with slice-by-slice navigation, opacity controls, and region highlighting.
- **Tissue & Label Segmentation**: Delineates white matter, gray matter, cerebrospinal fluid (CSF), and brain tumor regions (using datasets like BraTS 2020).
- **Volumetric Analysis & Export**: Calculates exact tissue volumes and offers options to export label masks and statistical reports.
- **Cross-Platform Accessibility**: Works smoothly on any standard web browser (Chrome, Firefox, Edge, Safari) across Windows, macOS, and Linux without extra plugins.

---

## 📁 Repository Documents

- **Project Presentation**: [3D_MRI_Brain_Segmentation_Presentation.pdf](3D_MRI_Brain_Segmentation_Presentation.pdf)
- **Final Project Report**: [3D_MRI_Brain_Segmentation_Final_Report.pdf](3D_MRI_Brain_Segmentation_Final_Report.pdf)

---

## 🛠️ System Architecture & Workflow

1. **Input & Upload**: Load structural MRI scans in NIfTI format (`.nii` / `.nii.gz`).
2. **Preprocessing**: Normalization, intensity scaling, and spatial resampling performed client-side.
3. **Deep Learning Inference**: In-browser MeshNet execution using TensorFlow.js and WebGL GPU acceleration.
4. **3D Rendering & Post-Processing**: Surface and volumetric 3D reconstruction via WebGL and Papaya/Three.js viewers.
5. **Analysis & Export**: Slice navigation, 3D structure inspection, and label output export.

---

## 👥 Project Group & Guidance

- **Project Title**: Web-Based 3D MRI Brain Segmentation and Visualization Tool
- **Guided By**: Asst. Prof. Jisha Raju
- **Group 12 Members**:
  - **Afridi S** (YCE21CS005)
  - **Akarsh B Varnu** (YCE21CS007)
  - **Ammu Asok B** (YCE21CS014)
  - **Gayathri Mohan** (YCE21CS026)
- **Department**: Department of Computer Science and Engineering
- **Institution / Academic Year**: YCET 2024-2025
