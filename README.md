# ABC iview shows recommender system
Research project for the MSc Applied Data Science course Personalisation for (public) media at Utrecht University.
Performed by Sander Engelberts in March 2022

A prototype recommender system for ABC iview shows is created which takes into account the public values: personalization, content- and representation diversity, autonomy, and justification. This is based on content similarity of short show descriptions and genre label(s), which are scraped from the [ABC iview website](https://iview.abc.net.au/) by the teachers of this course, analysed by me, and converted into a streamlit interface for visual inspection of show recommendations. 

For questions or remarks, please contact [s.engelberts@students.uu.nl](mailto:s.engelberts@students.uu.nl)<br>

## Repository
Below the paths to code- and other files in the repository can be found together with a short description of what these are about.  

| Path | Description
| :--- | :----------
| [PPM_ABC_recommender_system](https://github.com/SanderEngelberts/PPM_ABC_recommender_system) | Main repository
| &ensp;&ensp;&boxvr;&nbsp; [LICENSE](https://github.com/SanderEngelberts/PPM_ABC_recommender_system/blob/main/LICENSE) | GPL-3.0 License with copyright to autor
| &ensp;&ensp;&boxvr;&nbsp; [README.md](https://github.com/SanderEngelberts/PPM_ABC_recommender_system/blob/main/README.md) | This ReadMe giving information about the repository
| &ensp;&ensp;&boxvr;&nbsp; [PPM_research_project.pdf](https://github.com/SanderEngelberts/PPM_ABC_recommender_system/blob/main/PPM_research_project.pdf) | The report corresponding to this research
| &ensp;&ensp;&boxvr;&nbsp; [ABC_recommendations.ipynb](https://github.com/SanderEngelberts/PPM_ABC_recommender_system/blob/main/ABC_recommendations.ipynb) | The final code created for performing this research, which gathers meta data from scraped .html, cleans this, and creates show recommendations using tokenization, tf-idf vectorization, K-Means clustering, and cosine distance calculation
| &ensp;&ensp;&boxur;&nbsp; [streamlit](https://github.com/SanderEngelberts/PPM_ABC_recommender_system/blob/main/streamlit) | Folder containing all required content for running the streamlit interface that visualises the ABC iview recommendations
| &ensp;&ensp;&ensp;&boxvr;&nbsp; [app.py](https://github.com/SanderEngelberts/PPM_ABC_recommender_system/blob/main/streamlit/app.py) | Main file that is run for displaying the ABC iview recommender system prototype using streamlit
| &ensp;&ensp;&ensp;&boxur;&nbsp; [template.py](https://github.com/SanderEngelberts/PPM_ABC_recommender_system/blob/main/streamlit/template.py) | Supporting file containing functions that is used for running code in [app.py](https://github.com/SanderEngelberts/PPM_ABC_recommender_system/blob/main/streamlit/app.py)
| &ensp;&ensp;&ensp;&ensp;&boxur;&nbsp; [data/clustered_shows.csv](https://github.com/SanderEngelberts/PPM_ABC_recommender_system/blob/main/streamlit/data/clustered_shows.csv) | Fully processed show information obtained using [ABC_recommendations.ipynb](https://github.com/SanderEngelberts/PPM_ABC_recommender_system/blob/main/ABC_recommendations.ipynb), which among others contains show titles, unique ids, descriptions, genre names, and links to images
| &ensp;&ensp;&ensp;&boxur;&nbsp; [recommendations](https://github.com/SanderEngelberts/PPM_ABC_recommender_system/blob/main/streamlit/recommendations) | Folder containing files that store top 10 lists of show recommendations for different public values. These files consist of rows with the id of a show, the id of one of the top 10 shows it is most similar to (ordered from most to least similar) and the cosine distance between its description and genre label(s) contents
| &ensp;&ensp;&ensp;&ensp;&boxvr;&nbsp; [closest_within_cluster.csv](https://github.com/SanderEngelberts/PPM_ABC_recommender_system/blob/main/streamlit/recommendations/closest_within_cluster.csv) | Top 10 show recommendations that are most personalized due to being from the same K-Means cluster (most similar in content and genre type to the current show)
| &ensp;&ensp;&ensp;&ensp;&boxvr;&nbsp; [closest_outside_cluster.csv](https://github.com/SanderEngelberts/PPM_ABC_recommender_system/blob/main/streamlit/recommendations/closest_outside_cluster.csv) | Top 10 show recommendations that are most content diverse due to being from a different K-Means cluster (but still similar in content and genre type to the current show)
| &ensp;&ensp;&ensp;&ensp;&boxur;&nbsp; [closest_representation.csv](https://github.com/SanderEngelberts/PPM_ABC_recommender_system/blob/main/streamlit/recommendations/closest_representation.csv) | Top 10 show recommendations that are most representation diverse due to containing tokens in their show description that refer to minority or oppressed groups (but still similar in content and genre type to the current show)

## Requirements for running streamlit recommender system
Make sure to create a Conda environment with the following packages and its dependencies:
* Python 3.7 or above
* Streamlit
* os (typically standardly installed)
* pandas
* random (typically standardly installed)

## Running streamlit recommender system
The streamlit recommender system can be run via the command line by firstly getting in the location of the [streamlit](https://github.com/SanderEngelberts/PPM_ABC_recommender_system/blob/main/streamlit) folder (after downloading this folder to your own device) with the ```cd``` command, and activating your appropriate Conda environment there with the ```conda activate``` command. Lastly, the streamlit interface will simply be displayed in your webbrowser by running the [app.py](https://github.com/SanderEngelberts/PPM_ABC_recommender_system/blob/main/streamlit/app.py) file as follows:
```
streamlit run app.py
```
That is all, enjoy exploring my ABC iview recommender system prototype by clicking through different shows (using the popcorn buttons) and changing the content- and representation diversity settings in the sidebar on the left of the page. 
