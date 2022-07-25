<div id="top"></div>

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/github_username/repo_name">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">Excel Connect</h3>

  <p align="center">
    This project is used for get contactability info in excel getting the most repeated Phones and Emails for each unique user regardless of ID repetitions
  </p>
</div>

<!-- ABOUT THE PROJECT -->
## About The Project

Excel to Analize 
![Product Name Screen Shot][product-screenshot1]

Result
![Product Name Screen Shot][product-screenshot2]


<p align="right">(<a href="#top">back to top</a>)</p>



### Built With

* [![Anaconda][Anaconda-b]][Anaconda-url]


<p align="right">(<a href="#top">back to top</a>)</p>

### Prerequisites

This project was developed using Anaconda 4.12.0

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/KevinGuzmanH/ExcelAnalyse.git
   ```
2. Install python packages
   ```sh
   pip install pandas
   ```
   Optional dependency to Excel files in the historical .xls format
   ```sh
   pip install xlrd
   ```

<p align="right">(<a href="#top">back to top</a>)</p>


## Usage
### Arguments
* `-f`: Input file path
* `-i`: ID name column
* `-p`: Phone name column
* `-e`: Email name column
* `-s`: The name of the sheet in the excel file

### Example

<!-- USAGE EXAMPLE -->

 ```sh
python.exe .\main.py -f C:\Users\kevin\OneDrive\Escritorio\uno.xls -i ID -p Phone -e Email -s Contactos
 ```
 
When the file is processed you will see Done! in console

Make sure to close the new file before you run the program again
<p align="right">(<a href="#top">back to top</a>)</p>


<!-- MARKDOWN LINKS & IMAGES -->
[Anaconda-b]: https://anaconda.org/conda-forge/mlconjug/badges/version.svg
[Anaconda-url]: https://www.anaconda.com/products/distribution
[product-screenshot1]: images/about_img1.png
[product-screenshot2]: images/about_img2.png