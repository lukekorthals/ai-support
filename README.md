# ai-support
Pipeline of AI support systems for grading and feedback in programming and math courses as piloted in the PIPS 2025 course.

## cite conference paper as
Korthals, L., Rosenbusch, H., Grasman, R., Visser, I. (2025). Grading University Students with LLMs: Performance and Acceptance of a Canvas-Based Automation. In: Cristea, A.I., Walker, E., Lu, Y., Santos, O.C., Isotani, S. (eds) Artificial Intelligence in Education. Posters and Late Breaking Results, Workshops and Tutorials, Industry and Innovation Tracks, Practitioners, Doctoral Consortium, Blue Sky, and WideAIED. AIED 2025. Communications in Computer and Information Science, vol 2591 . Springer, Cham. [https://doi.org/10.1007/978-3-031-99264-3_5](https://doi.org/10.1007/978-3-031-99264-3_5)

## usage
You can use the `[EXAMPLE]environment.yml` file to create a virtual environment with all package dependencies:  

The `settings.yml`controls important settings such as Canvas identifiers, file paths, llm settings such as the model to use, global rubrics, and when grades in canvas should no longer be overwritten by this integration. 

The `resources` folder contains assignments, rubrics, and example solutions for the respective assignments (here PIPS 2025 assignments). Paths to the relevant files are specified in `settings.yml` and they are accessed by the code in `main.ipynb`.

The `scripts` folder contains utility functions for connecting to Canvas, downloading student submissions, grading them with LLMs, and uploading grades and feedback back to Canvas.

The `main.ipynb` contains all functionality to load the settings, connect to Canvas, download submissions, grade them with LLMs, and upload grades and feedback.

## paper specific folders
The folder `Grading University Students with LLMs (Korthals et al., 2025)` contains all materials specific to the AIED 2025 paper, such as the assignments, rubrics, and solutions used in the PIPS 2025 course.