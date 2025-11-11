---
layout: page 
title : "Mathematica Stylesheet: CMU Article"
permalink: /teaching/Mathematica_Stylesheet
hide: true
---

## Introduction

The **CMU Article** stylesheet is a custom *Mathematica stylesheet* designed specifically for academic writing and publication. It is based on the Computer Modern Unicode (CMU) fonts, which are the digital versions of the classic Computer Modern fonts designed by Donald Knuth for the TeX typesetting system.

### Features

- **Professional Typography**: Uses Computer Modern Unicode fonts for publication-quality text
- **Academic Formatting**: Optimized for mathematical and scientific documents
- **Consistent Styling**: Predefined styles for titles, sections, equations, and references
- **Print-Ready**: Configured for high-quality printing and PDF export

### Font Requirements

The CMU Article stylesheet requires the **Computer Modern Unicode (CMU) fonts** to be installed on your system. These fonts are freely available and provide excellent mathematical typography.

## Installation Instructions

### Step 1: Install CMU Fonts

Before installing the stylesheet, you should install the CMU fonts on your system:

1. **Download the fonts**: The CMU fonts can be downloaded [here]({{site.baseurl}}/teaching/Mathematica/CMUfonts.zip).
2. **Install fonts on your operating system**:
   - **macOS**: Double-click each `.ttf` file and click "Install Font"
   - **Windows**: Right-click each `.ttf` file and select "Install"
   - **Linux**: Copy the `.ttf` files to `/usr/share/fonts/truetype/` or use your system's font manager

### Step 2: Download the Stylesheet

1. **Download the stylesheet**: The `CMU Article.nb` file is available for download [here]({{site.baseurl}}/teaching/Mathematica/CMU%20Article.nb).
2. **Extract the file**: Save the `CMU Article.nb` file to a location on your computer

### Step 3: Install the Stylesheet in Mathematica

1. **Open Mathematica**.

2. **Go to the Palettes menu**: In the top menu bar, click on **Palettes**.

3. **Select Install Palettes**: From the Palettes menu, choose **Install Palettes...**.

4. **In the Install Wolfram System Item dialog** (as shown below):
    <img src="{{site.baseurl}}/teaching/Mathematica/dialog.png" alt="Install Wolfram System Item dialog" width="500" /><br/>
    *Example: The dialog for installing the CMU Article stylesheet.*

    - **Type of Item to Install**: Select **Stylesheet** from the dropdown menu.
    - **Source**: Click the dropdown and select or browse to your downloaded `CMU Article.nb` file.
    - **Install Name**: This will usually auto-fill as “CMU Article”, but you can edit it if you wish.
    - **Install for this user only**: This is the default and recommended option for most users. If you want all users on the computer to have access, select the second option.
    - Click **OK** to complete the installation.

### Step 4: Apply the Stylesheet

After installation, you can apply the CMU Article stylesheet to any notebook:

1. **Open a notebook** in Mathematica

2. **Access Format menu**: Click on **Format** in the menu bar

3. **Select Stylesheet**: Choose **Stylesheet** from the Format menu

4. **Choose CMU Article**: From the stylesheet list, select **CMU Article**

## Verification

To verify that the installation was successful:

1. **Check font availability**: The text should display in Computer Modern Unicode fonts
2. **Test mathematical expressions**: Equations should render with proper mathematical typography
3. **Verify styles**: Different cell styles (Title, Section, etc.) should have distinct formatting

## Troubleshooting

### Font Issues
- **Problem**: Text appears in default fonts instead of CMU fonts
- **Solution**: Ensure CMU fonts are properly installed on your system and restart Mathematica

### Stylesheet Not Found
- **Problem**: CMU Article doesn't appear in the stylesheet list
- **Solution**: Verify the installation was completed successfully and restart Mathematica
- **Note**: If the installation succeeded, running the following in a Mathematica notebook should return a list of files containing `CMU Article.nb`:

  ```mathematica
  FileNames[All, FileNameJoin[{$UserBaseDirectory, "SystemFiles", "FrontEnd", "StyleSheets"}]]
  ```

### Installation Errors
- **Problem**: Installation dialog shows errors
- **Solution**: Check that the `CMU Article.nb` file is not corrupted and try downloading it again

## Additional Resources

- **Complete Package**: For the full Mathematica-for-physics package with additional tools, visit the [main documentation page]({{site.baseurl}}/teaching/Mathematica/)
- **Font Information**: Learn more about Computer Modern fonts on [Wikipedia](https://en.wikipedia.org/wiki/Computer_Modern){:target="_blank"}

---

<div style="text-align: center;">
  <img src="/assets/img/logos/Mathematica.png" alt="Mathematica" width="30%">
</div>

