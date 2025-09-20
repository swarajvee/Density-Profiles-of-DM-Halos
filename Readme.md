# Analysis of Dark Matter Halo Density Profiles
[![Ask DeepWiki](https://devin.ai/assets/askdeepwiki.png)](https://deepwiki.com/swarajvee/Density-Profiles-of-DM-Halos)

## Overview
This repository contains Python scripts for analyzing cosmological simulation data of dark matter (DM) halos from the AbacusSummit project. The primary goals are to calculate and study two fundamental properties of DM halos: the Halo Mass Function (HMF) and the Radial Density Profile. The analysis compares results from the simulation data with established theoretical models.

## Key Analyses

### 1. Halo Mass Function (HMF)
This part of the project focuses on determining the number density of halos as a function of their mass.

*   **Observational HMF from Simulation Data:**
    *   Scripts read halo catalogs from AbacusSummit's `.asdf` files using the `abacusnbody` library.
    *   Halo data (primarily mass, calculated from particle count `N`) is extracted and often processed into `.csv` files.
    *   The mass data is binned to calculate the number of halos per unit mass per unit volume (`dn/dM`), providing an "observed" HMF from the simulation.

*   **Theoretical HMF and Comparison:**
    *   The `colossus` and `hmf` Python libraries are used to compute theoretical HMFs based on models like Tinker08, Behroozi, and Warren.
    *   The analytically calculated HMF from the simulation is plotted against various theoretical models to assess agreement.
    *   These comparisons are performed across multiple redshifts (e.g., z=0.1, 2, 3, 5, 8) to study the evolution of the HMF.
    *   Key scripts for this analysis include `HMF/13_Theory_and_Observation_comparison (general_code).py` and `HMF/18_HMF_Using_differenet_models.py`.

### 2. Radial Density Profile
This section analyzes the internal structure of DM halos by calculating how their density varies with distance from the center.

*   **Data Extraction and Preparation:**
    *   Halos within specific particle number ranges (e.g., 30,000-31,000 or 100,000-101,000 particles) are identified across multiple simulation snapshots.
    *   For each selected halo, the central coordinates and the positions of its constituent subsample particles are extracted and saved to `.csv` files using scripts like `31_save_subsamples.py`.

*   **Profile Calculation and Averaging:**
    *   The radial distance of each subsample particle from its halo's center is calculated.
    *   Particles are binned into spherical shells based on their distance. The total mass in each shell is divided by the shell's volume to compute the density at that radius.
    *   The density profiles from multiple halos in the same mass range are averaged to produce a smoother, more representative profile, as demonstrated in `Optimized Codes/43_radial_density.py` and the associated Jupyter Notebook.

*   **Comparison with the NFW Profile:**
    *   The averaged density profile derived from the simulation data is compared against the theoretical Navarro-Frenk-White (NFW) profile.
    *   The `halomod` library is used to generate theoretical NFW profiles for halos of a given mass and redshift, allowing for a direct comparison, as seen in `45_NFW_profile.py`.

## Repository Structure

*   `Halo Mass Function/`: Contains all scripts related to calculating and plotting the HMF. It includes early exploratory codes and more developed scripts that perform detailed comparisons against theoretical models.
*   `Radial Density Profile/`: Houses scripts for calculating the spherically-averaged density profiles of halos.
    *   `1 Random Number Calculations/`: Preliminary scripts using simulated random particle distributions to develop and test methodologies.
    *   `2 Abacus Data Calculations/`: The core analysis scripts that process AbacusSummit data. This includes code to extract halo and subsample data, calculate radii, and compute/plot density profiles.
    *   `Optimized Codes/`: More refined and structured versions of the radial density profile analysis scripts.
*   `Thesis Plots/`: A collection of scripts used to generate the final figures for a thesis, drawing from the analyses in the other directories.

## Core Technologies and Libraries

This project is written in Python 3 and relies on several key scientific libraries:

*   **`abacusnbody`**: For reading the native `.asdf` format of the AbacusSummit simulation data.
*   **`numpy` & `pandas`**: For numerical operations and efficient data manipulation, particularly with the processed `.csv` files.
*   **`matplotlib`**: For all data visualization and plotting.
*   **`colossus`**: For cosmological calculations and generating theoretical halo mass functions.
*   **`hmf` & `halomod`**: A comprehensive framework for computing theoretical halo mass functions, halo concentrations, and density profiles (like the NFW profile).

## Setup and Usage

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/swarajvee/Density-Profiles-of-DM-Halos.git
    cd Density-Profiles-of-DM-Halos
    ```

2.  **Install dependencies:**
    Ensure you have Python installed. You can install the required packages using pip:
    ```bash
    pip install numpy pandas matplotlib asdf abacusnbody colossus hmf halomod
    ```

3.  **Running the Scripts:**
    The scripts in this repository are primarily for analysis and plotting. Most scripts contain hardcoded file paths to the simulation data. To run them, you will need to:
    *   Obtain the relevant AbacusSummit simulation data.
    *   Update the file paths within the Python scripts to point to the location of your local data.
    *   Execute a script from the command line, for example:
        ```bash
        python "Halo Mass Function/mass density function per unit volume/density function/HMF/19_HMF_of_selected_models.py"
