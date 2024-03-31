# Evaluating State of the Art Upscaling Technologies: Performance, Image Quality and Gaming Scenario Suitability

## Introduction

Modern video games feature advanced graphics with complex particle physics and real-time ray-traced lighting effects, setting new industry standards. These graphics demand significant processing power, provided by GPUs from major companies like Nvidia, Intel, and AMD. However, increasing GPU power to support these graphics faces challenges like miniaturization limits and rising energy consumption, which also raises sustainability and environmental concerns.

To address these issues, companies are focusing on upscaling technologies like Nvidia’s Deep Learning Super Sampling (DLSS), which employs AI to upscale graphics efficiently. These technologies aim to render graphics at lower resolutions for better performance and then upscale to higher resolutions, maintaining high detail levels. Nvidia's DLSS, notably, even enhances image quality and details in games.

For example, using DLSS 3.0 in Cyberpunk 2077 significantly increased frame rates from 20 to 100 FPS, with 30 FPS generally considered smooth. DLSS 3.0 also reduces power consumption by up to 40%. Other key upscaling technologies in gaming include Intel's XeSS, which uses machine learning, and AMD's FSR, which operates differently without AI reliance.

## Reserach Question

How do various state-of-the-art upscaling technologies compare in terms of performance, image quality and suitability in the context of modern video games?
- The aim of the research is to conduct a comparative analysis of state-of-the-art upscaling technologies.  The focus lies on the performance measurement and image quality. Furthermore, a very important aspect is to the assess the suitability for optimal gaming experiences.

## Methodology

This master thesis conducts a benchmark test to compare the performance, image quality, and gaming scenario suitability of Nvidia DLSS, AMD FSR, and Intel XeSS against native rendering. The test uses two Nvidia graphics cards: the RTX 3060 (supporting DLSS 2.0) and the RTX 4060 (supporting DLSS 3.0), chosen based on their popularity in the Steam Hardware Survey. Metrics like FPS, GPU utilization, and energy consumption are measured across various game genres, including titles like Cyberpunk 2077 and Call of Duty Modern Warfare III, which support all three upscaling technologies. The methodology involves extensive data collection and processing, utilizing Python for analysis.

## Benchmark Scenes

To ensure transparency and reproducibility, I've provided benchmark videos demonstrating the exact testing scenarios. These videos showcase diverse visual challenges and the specific in-game locations used for performance and image quality evaluation.

Access the benchmark videos here: https://drive.google.com/drive/folders/1unBSgl-6xzqBpOYpT08KNWz3lpTowTzM?usp=sharing

## Benchmark Results (Performance, Energy Consumption and Frametimes)

The benchmark results are available here: https://drive.google.com/drive/folders/1GCy3Qm5CpW8PrsRGy1mzGRU0HU9LupEZ?usp=sharing. 

Please note that the benchmark results are not completed yet. All benchmark results are validated with another run using the MSI Afterburner application as well as Nvidia Frame View. Please be aware that the Minimum FPS and Maximum FPS cannot be validated using Nvidia Frame View.

## Contents of this Repository

This repository contains the Exposé of the Master Thesis, the Master Thesis and the Python Scripts used in the Benchmark Process.

## List of used AI assistance tools

- Chatgpt (GPT-4)
- Gemini Advanced (Formerly known as Google Bard)
- ChatPDF
- DeepL

## Python Scripts for Benchmark Data Processing and Analysis

- energy_consumption_HWInfo: This Python scripts extracts the information provided by HWInfo into a clearly readable excel file. The excel file only contains information necessasry for the benchmark analysis which are the GPU energy consumption and GPU utilization.
- frame_times_CapFrameX: This Python script extracts the frametimes from a json file which is the output CapFrameX provides. Data is analyzed, cleaned and stored into an xlsx file where the graphs are created and the data is further analyzed.
- performance_benchmark_MSI_Afterburner: This Python script extracts the performance metrics (Average FPS, Min FPS, 0.1 % Low FPS and more) from the MSI Afterburner benchmark.txt file. The data is processed and stored into an xlsx file where graphs are created and the data is furhter analyzed.
